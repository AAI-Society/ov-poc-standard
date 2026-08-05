#!/usr/bin/env python3
"""Generate the audit checklist, coverage matrix, and CSV/JSON exports
from the requirement chapters.

Usage:  python3 tools/generate_checklist.py

Outputs (overwritten in place):
  0.1/en/0x94-Appendix-E_Audit-Checklist.md
  checklist/poc-checklist.csv
  checklist/poc-checklist.json
"""

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "0.1" / "en"
OUT_MD = SPEC / "0x94-Appendix-E_Audit-Checklist.md"
OUT_DIR = ROOT / "checklist"

LEVEL_META = {
    "1": ("🗣️", "Recorded"),
    "2": ("📋", "Attested"),
    "3": ("🔍", "Independently Verifiable"),
    "4": ("🔒", "Self-Enforcing / Continuous"),
}

ROW_RE = re.compile(r"^\| \*\*(\d+\.\d+\.\d+)\*\* \| (.+) \| (\d) \|\s*$")
CHAPTER_RE = re.compile(r"^# (C\d+) (.+)$")
SECTION_RE = re.compile(r"^## (C\d+\.\d+) (.+)$")


def plain_text(md: str) -> str:
    """Strip markdown emphasis and links for CSV/JSON export."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    text = text.replace("**", "").replace("&#8211;", "-")
    return text.strip()


def parse():
    chapters = []
    for path in sorted(SPEC.glob("0x10-C*.md")):
        chapter_id = chapter_title = None
        section_id = section_title = None
        reqs = []
        for line in path.read_text().splitlines():
            if m := CHAPTER_RE.match(line):
                chapter_id, chapter_title = m.group(1), m.group(2)
            elif m := SECTION_RE.match(line):
                section_id, section_title = m.group(1), m.group(2)
            elif m := ROW_RE.match(line):
                reqs.append({
                    "id": m.group(1),
                    "chapter": chapter_id,
                    "chapter_title": chapter_title,
                    "section": section_id,
                    "section_title": section_title,
                    "level": int(m.group(3)),
                    "text_md": m.group(2),
                    "file": path.name,
                })
        chapters.append((chapter_id, chapter_title, path.name, reqs))
    return chapters


def write_markdown(chapters):
    all_reqs = [r for *_, reqs in chapters for r in reqs]
    counts = {lvl: sum(1 for r in all_reqs if r["level"] == int(lvl)) for lvl in LEVEL_META}
    total = len(all_reqs)

    lines = [
        "# Appendix E: Audit Checklist (generated)",
        "",
        "> **Generated file — do not edit by hand.** Rebuild with"
        " `python3 tools/generate_checklist.py` after changing any requirement chapter."
        " Machine-readable exports live in [`checklist/`](../../checklist).",
        "",
        "Tick items as you close them out; each chapter's *Auditor evidence* notes say what to"
        " collect and what to test per requirement. Levels are cumulative and align 1:1 with the"
        " Verifiability Tiers — clearing every Level 1–3 item in the claimed domains is the"
        " minimum for a Proof-of-Control claim"
        " ([Using Proof-of-Control](0x03-Using-Proof-of-Control.md)).",
        "",
        "**Level key:** "
        + " · ".join(f"L{lvl} {icon} {name}" for lvl, (icon, name) in LEVEL_META.items()),
        "",
        "## Coverage Matrix",
        "",
        "| Chapter | " + " | ".join(f"L{lvl} {LEVEL_META[lvl][0]}" for lvl in LEVEL_META)
        + " | Total |",
        "| --- | " + " | ".join(":---:" for _ in range(5)) + " |",
    ]
    for chapter_id, chapter_title, fname, reqs in chapters:
        row = [f"[{chapter_id} {chapter_title}]({fname})"]
        for lvl in LEVEL_META:
            n = sum(1 for r in reqs if r["level"] == int(lvl))
            row.append(str(n) if n else "—")
        row.append(f"**{len(reqs)}**")
        lines.append("| " + " | ".join(row) + " |")
    lines.append(
        "| **All chapters** | "
        + " | ".join(f"**{counts[lvl]}**" for lvl in LEVEL_META)
        + f" | **{total}** |"
    )

    write_level_chart(counts, total)
    lines += [
        "",
        "## Requirements by Level",
        "",
        '<p align="center">',
        '  <picture>',
        '    <source media="(prefers-color-scheme: dark)"'
        ' srcset="../../images/diagrams/checklist-levels-dark.svg">',
        f'    <img alt="{total} requirements by level:'
        + ", ".join(f" {counts[lvl]} at Level {lvl} ({LEVEL_META[lvl][1]})" for lvl in LEVEL_META)
        + '" src="../../images/diagrams/checklist-levels-light.svg" width="620">',
        '  </picture>',
        '</p>',
        "",
    ]

    for chapter_id, chapter_title, fname, reqs in chapters:
        lines += [f"## {chapter_id} {chapter_title}", ""]
        current_section = None
        for r in reqs:
            if r["section"] != current_section:
                current_section = r["section"]
                lines += [f"### {r['section']} {r['section_title']}", ""]
            icon = LEVEL_META[str(r["level"])][0]
            lines.append(f"- [ ] **{r['id']}** `L{r['level']}` {icon} — {r['text_md']}")
        lines.append("")
        lines.append(f"*Auditor evidence for these items: see [{chapter_id}]({fname}).*")
        lines.append("")

    lines += [
        "---",
        "",
        "*Proof-of-Control is stewarded by the"
        " [Advanced AI Society](https://advancedaisociety.org/) —"
        " **[join at advancedaisociety.org](https://advancedaisociety.org/)**.*",
        "",
    ]
    OUT_MD.write_text("\n".join(lines))


CHART_THEMES = {
    "light": {
        "text": "#1f2328", "muted": "#57606a",
        "bars": {"1": ("#ffebe9", "#cf222e", "#58151c"),
                 "2": ("#fff8c5", "#bf8700", "#664d03"),
                 "3": ("#dafbe1", "#1a7f37", "#0a3622"),
                 "4": ("#ddf4ff", "#0969da", "#052c65")},
    },
    "dark": {
        "text": "#e6edf3", "muted": "#8b949e",
        "bars": {"1": ("#2d1418", "#f85149", "#ffa198"),
                 "2": ("#272115", "#bb8009", "#f2cc60"),
                 "3": ("#12261e", "#2ea043", "#aff5b4"),
                 "4": ("#121d2f", "#388bfd", "#79c0ff")},
    },
}

FONT = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"


def write_level_chart(counts, total):
    """Emit the branded requirements-by-level bar chart (light/dark SVGs)."""
    out_dir = ROOT / "images" / "diagrams"
    out_dir.mkdir(parents=True, exist_ok=True)
    max_count = max(counts.values())
    for variant, theme in CHART_THEMES.items():
        w, bar_h, gap, label_w, top = 640, 36, 14, 220, 46
        h = top + 4 * (bar_h + gap) + 6
        parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" font-family="{FONT}">',
            f'<text x="{w / 2}" y="26" font-size="14.5" font-weight="600" '
            f'fill="{theme["text"]}" text-anchor="middle">'
            f'{total} requirements by level</text>',
        ]
        for i, (lvl, (icon, name)) in enumerate(LEVEL_META.items()):
            y = top + i * (bar_h + gap)
            fill, stroke, text = theme["bars"][lvl]
            blen = max(28, int((w - label_w - 70) * counts[lvl] / max_count))
            parts.append(
                f'<text x="{label_w - 12}" y="{y + bar_h / 2 + 4.5}" font-size="12.5" '
                f'fill="{theme["text"]}" text-anchor="end">L{lvl} · {name}</text>'
            )
            parts.append(
                f'<rect x="{label_w}" y="{y}" width="{blen}" height="{bar_h}" rx="8" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
            )
            parts.append(
                f'<text x="{label_w + blen + 12}" y="{y + bar_h / 2 + 4.5}" '
                f'font-size="13" font-weight="600" fill="{theme["text"]}" '
                f'text-anchor="start">{counts[lvl]}</text>'
            )
        parts.append("</svg>")
        (out_dir / f"checklist-levels-{variant}.svg").write_text("\n".join(parts) + "\n")


def write_exports(chapters):
    OUT_DIR.mkdir(exist_ok=True)
    all_reqs = [r for *_, reqs in chapters for r in reqs]
    rows = [
        {
            "id": r["id"],
            "chapter": r["chapter"],
            "chapter_title": r["chapter_title"],
            "section": r["section"],
            "section_title": r["section_title"],
            "level": r["level"],
            "level_name": LEVEL_META[str(r["level"])][1],
            "requirement": plain_text(r["text_md"]),
            "source_file": f"0.1/en/{r['file']}",
            "status": "",
            "auditor_notes": "",
        }
        for r in all_reqs
    ]
    with open(OUT_DIR / "poc-checklist.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    (OUT_DIR / "poc-checklist.json").write_text(json.dumps(rows, indent=2) + "\n")


def main():
    chapters = parse()
    total = sum(len(reqs) for *_, reqs in chapters)
    write_markdown(chapters)
    write_exports(chapters)
    print(f"Generated checklist for {total} requirements across {len(chapters)} chapters.")


if __name__ == "__main__":
    main()
