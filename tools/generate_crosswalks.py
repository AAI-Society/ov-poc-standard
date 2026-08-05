#!/usr/bin/env python3
"""Inject the requirement-level mapping tables into the crosswalk pages.

Reads mappings/coding_sheet.csv and checklist/poc-checklist.json, and rewrites
the block between the GENERATED markers in each coded crosswalk page:

    <!-- BEGIN GENERATED MAPPING (tools/generate_crosswalks.py) -->
    ...
    <!-- END GENERATED MAPPING -->

Edit the coding sheet, not the generated block. Usage::

    python3 tools/generate_crosswalks.py
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "EU_AI_Act": "eu-ai-act.md",
    "NIST_AI_RMF": "nist-ai-rmf.md",
    "ISO_42001": "iso-iec-42001.md",
    "SOC_2": "soc-2.md",
    "OWASP_AISVS": "owasp.md",
    "MITRE_ATLAS": "mitre-atlas.md",
    "CSA_AARM": "csa-aarm.md",
    "NIST_SP_800_207": "zero-trust.md",
}

CHAPTER_FILES = {
    "C1": "0x10-C01-Provenance.md", "C2": "0x10-C02-Privacy.md",
    "C3": "0x10-C03-Portability.md", "C4": "0x10-C04-Authorization.md",
    "C5": "0x10-C05-Identity.md", "C6": "0x10-C06-Security.md",
    "C7": "0x10-C07-Evidence-Generation-and-Properties.md",
    "C8": "0x10-C08-Verifiability-Tiers.md",
    "C9": "0x10-C09-System-Surface-MAESTRO.md",
    "C10": "0x10-C10-Conformance-and-Disclosure.md",
}

BEGIN = "<!-- BEGIN GENERATED MAPPING (tools/generate_crosswalks.py) -->"
END = "<!-- END GENERATED MAPPING -->"
BADGE = {"EM": "Exact", "PM": "Partial", "NM": "None"}


def section_sort_key(sec):
    ch, s = sec[1:].split(".")
    return (int(ch), int(s))


def main():
    reqs = json.loads((ROOT / "checklist" / "poc-checklist.json").read_text())
    sections = {}
    sec_reqs = defaultdict(list)
    for r in reqs:
        sections[r["section"]] = r["section_title"]
        sec_reqs[r["section"]].append(r["id"])

    rows = list(csv.DictReader(open(ROOT / "mappings" / "coding_sheet.csv")))
    by_fw = defaultdict(dict)  # fw -> section -> row (rows share coding per section)
    counts = defaultdict(lambda: defaultdict(int))
    for row in rows:
        by_fw[row["source_framework"]][row["poc_section"]] = row
        counts[row["source_framework"]][row["match_type"]] += 1

    total = len(reqs)
    for fw, page in PAGES.items():
        c = counts[fw]
        cov = round(100 * (c["EM"] + c["PM"]) / total)
        lines = [
            BEGIN,
            "",
            f"**Coverage: {cov}%** of the {total} Proof-of-Control requirements "
            f"({c['EM']} exact matches, {c['PM']} partial matches, {c['NM']} not covered), computed per "
            f"the [mapping rubric](rubric.md) from the row-level "
            f"[coding sheet](coding_sheet.csv). *Draft seed coding — pending working-group "
            f"validation.* To change this table, edit the coding sheet and run "
            f"`python3 tools/generate_crosswalks.py`.",
            "",
            "**How to read the Match column** ([full rubric](rubric.md)): "
            "**Exact** — the framework has a clause equivalent in scope and intent. "
            "**Partial** — the framework covers the topic, but not with PoC's "
            "operator-independent evidence (or not at the same depth). "
            "**None** — the framework has no analogous provision.",
            "",
            "| PoC section | Reqs | Match | Closest framework clause(s) | Rationale |",
            "| --- | :---: | :---: | --- | --- |",
        ]
        gaps = []
        for sec in sorted(by_fw[fw], key=section_sort_key):
            row = by_fw[fw][sec]
            ids = sec_reqs[sec]
            chapter = sec.split(".")[0]
            link = f"[{sec} {sections[sec]}](../0.1/en/{CHAPTER_FILES[chapter]})"
            if row["match_type"] == "NM":
                gaps.append((sec, sections[sec], row["rationale"]))
            lines.append(
                f"| {link} | {len(ids)} | {BADGE[row['match_type']]} | "
                f"{row['framework_clause']} | {row['rationale']} |"
            )
        lines += [
            "",
            "### Gap Analysis (what this framework does not cover)",
            "",
        ]
        if gaps:
            for sec, title, rationale in gaps:
                lines.append(f"* **{sec} {title}** — {rationale}")
        else:
            lines.append("* No gaps at section level.")
        lines += [
            "",
            "*Match granularity is the PoC section; every requirement in a section carries its "
            "section's coding in the [coding sheet](coding_sheet.csv). Requirement-level "
            "refinement is the working group's next pass.*",
            "",
            END,
        ]
        block = "\n".join(lines)

        path = ROOT / "mappings" / page
        text = path.read_text()
        pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.DOTALL)
        if not pattern.search(text):
            raise SystemExit(f"{page}: GENERATED markers not found")
        path.write_text(pattern.sub(lambda _: block, text))
        print(f"{page}: injected mapping ({cov}% coverage, {len(by_fw[fw])} sections)")


if __name__ == "__main__":
    main()
