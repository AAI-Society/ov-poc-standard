#!/usr/bin/env python3
"""Compute external-framework coverage of Proof-of-Control from the coding sheet.

Coverage per framework = (EM + PM) / total PoC requirements x 100
(see mappings/rubric.md for the EM/PM/NM definitions).

Usage::

    python3 mappings/compute_coverage.py
    python3 mappings/compute_coverage.py --markdown       # emit the README table
    python3 mappings/compute_coverage.py --svg            # regenerate the coverage chart
    python3 mappings/compute_coverage.py --sheet mappings/coding_sheet.csv

The script also validates the sheet against checklist/poc-checklist.json:
every requirement must be coded exactly once per framework.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DISPLAY_NAMES = {
    "EU_AI_Act": "EU AI Act",
    "NIST_AI_RMF": "NIST AI RMF",
    "ISO_42001": "ISO/IEC 42001",
    "SOC_2": "SOC 2",
    "OWASP_AISVS": "OWASP AISVS",
    "MITRE_ATLAS": "MITRE ATLAS",
    "CSA_AARM": "CSA AARM",
    "NIST_SP_800_207": "Zero Trust (NIST SP 800-207)",
}

CROSSWALKS = {
    "EU_AI_Act": "eu-ai-act.md",
    "NIST_AI_RMF": "nist-ai-rmf.md",
    "ISO_42001": "iso-iec-42001.md",
    "SOC_2": "soc-2.md",
    "OWASP_AISVS": "owasp.md",
    "MITRE_ATLAS": "mitre-atlas.md",
    "CSA_AARM": "csa-aarm.md",
    "NIST_SP_800_207": "zero-trust.md",
}

FONT = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
CHART_THEMES = {
    "light": {"text": "#1f2328", "muted": "#57606a", "track": "#f6f8fa",
              "track_stroke": "#d0d7de", "em": "#6f42c1", "pm": "#c4b1e8"},
    "dark": {"text": "#e6edf3", "muted": "#8b949e", "track": "#161b22",
             "track_stroke": "#30363d", "em": "#a371f7", "pm": "#5a4b7d"},
}


def load(sheet_path: Path):
    with open(sheet_path, newline="") as f:
        rows = list(csv.DictReader(f))
    req_ids = {r["id"] for r in json.loads(
        (ROOT / "checklist" / "poc-checklist.json").read_text())}
    errors = []
    seen = defaultdict(set)
    for row in rows:
        rid, fw, mt = row["poc_requirement_id"], row["source_framework"], row["match_type"]
        if rid not in req_ids:
            errors.append(f"unknown requirement id {rid} ({fw})")
        if mt not in {"EM", "PM", "NM"}:
            errors.append(f"invalid match_type {mt!r} for {rid} x {fw}")
        if rid in seen[fw]:
            errors.append(f"duplicate coding for {rid} x {fw}")
        seen[fw].add(rid)
    for fw, ids in seen.items():
        missing = req_ids - ids
        if missing:
            errors.append(f"{fw}: {len(missing)} requirements uncoded "
                          f"(e.g., {sorted(missing)[:3]})")
    if errors:
        print("Coding-sheet validation FAILED:", file=sys.stderr)
        for e in errors[:20]:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)
    return rows, len(req_ids)


def coverage(rows, total):
    counts = defaultdict(lambda: defaultdict(int))
    for row in rows:
        counts[row["source_framework"]][row["match_type"]] += 1
    result = {}
    for fw, c in counts.items():
        result[fw] = {
            "EM": c["EM"], "PM": c["PM"], "NM": c["NM"],
            "coverage": round(100 * (c["EM"] + c["PM"]) / total),
        }
    return dict(sorted(result.items(), key=lambda kv: -kv[1]["coverage"]))


def print_table(cov, total):
    print(f"Coverage of {total} Proof-of-Control requirements "
          f"(EM+PM)/total; see mappings/rubric.md\n")
    print(f"{'Framework':<30} {'EM':>4} {'PM':>4} {'NM':>4} {'Coverage':>9}")
    for fw, c in cov.items():
        print(f"{DISPLAY_NAMES.get(fw, fw):<30} {c['EM']:>4} {c['PM']:>4} "
              f"{c['NM']:>4} {c['coverage']:>8}%")


def markdown_table(cov):
    lines = ["| Framework | EM | PM | NM | Coverage | Crosswalk |",
             "| --- | :---: | :---: | :---: | :---: | --- |"]
    for fw, c in cov.items():
        name = DISPLAY_NAMES.get(fw, fw)
        xw = CROSSWALKS.get(fw)
        link = f"[{name}]({xw})" if xw else name
        lines.append(f"| {link} | {c['EM']} | {c['PM']} | {c['NM']} | "
                     f"**{c['coverage']}%** | [{xw}]({xw}) |" if xw else
                     f"| {name} | {c['EM']} | {c['PM']} | {c['NM']} | "
                     f"**{c['coverage']}%** | — |")
    return "\n".join(lines)


def write_svg(cov, total):
    out = ROOT / "images" / "diagrams"
    out.mkdir(parents=True, exist_ok=True)
    for variant, t in CHART_THEMES.items():
        w, bar_h, gap, label_w, top = 760, 30, 12, 250, 74
        h = top + len(cov) * (bar_h + gap) + 6
        track_w = w - label_w - 80
        p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
             f'viewBox="0 0 {w} {h}" font-family="{FONT}">',
             f'<text x="{w / 2}" y="26" font-size="14.5" font-weight="600" '
             f'fill="{t["text"]}" text-anchor="middle">How much of Proof-of-Control '
             f'each framework already addresses</text>',
             f'<text x="{w / 2}" y="46" font-size="11.5" fill="{t["muted"]}" '
             f'text-anchor="middle">(EM + PM) / {total} requirements — '
             f'darker: exact match · lighter: partial match · '
             f'gap: what only PoC covers</text>']
        for i, (fw, c) in enumerate(cov.items()):
            y = top + i * (bar_h + gap)
            em_w = track_w * c["EM"] / total
            pm_w = track_w * c["PM"] / total
            p.append(f'<text x="{label_w - 12}" y="{y + bar_h / 2 + 4}" font-size="12" '
                     f'fill="{t["text"]}" text-anchor="end">'
                     f'{DISPLAY_NAMES.get(fw, fw)}</text>')
            p.append(f'<rect x="{label_w}" y="{y}" width="{track_w}" height="{bar_h}" '
                     f'rx="7" fill="{t["track"]}" stroke="{t["track_stroke"]}"/>')
            if em_w:
                p.append(f'<rect x="{label_w}" y="{y}" width="{em_w:.1f}" '
                         f'height="{bar_h}" rx="7" fill="{t["em"]}"/>')
            if pm_w:
                p.append(f'<rect x="{label_w + em_w:.1f}" y="{y}" width="{pm_w:.1f}" '
                         f'height="{bar_h}" fill="{t["pm"]}"/>')
            p.append(f'<text x="{label_w + track_w + 10}" y="{y + bar_h / 2 + 4}" '
                     f'font-size="12.5" font-weight="600" fill="{t["text"]}">'
                     f'{c["coverage"]}%</text>')
        p.append("</svg>")
        (out / f"mapping-coverage-{variant}.svg").write_text("\n".join(p) + "\n")
    print(f"wrote mapping-coverage-{{light,dark}}.svg to {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", default=str(ROOT / "mappings" / "coding_sheet.csv"))
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--svg", action="store_true")
    args = ap.parse_args()
    rows, total = load(Path(args.sheet))
    cov = coverage(rows, total)
    if args.markdown:
        print(markdown_table(cov))
    else:
        print_table(cov, total)
    if args.svg:
        write_svg(cov, total)


if __name__ == "__main__":
    main()
