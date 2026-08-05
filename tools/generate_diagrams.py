#!/usr/bin/env python3
"""Generate the standard's branded SVG diagrams in light and dark variants.

Usage:  python3 tools/generate_diagrams.py

Outputs images/diagrams/<name>-{light,dark}.svg for each diagram.
Embed with a <picture> element so GitHub serves the right variant:

    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".../<name>-dark.svg">
      <img alt="..." src=".../<name>-light.svg" width="...">
    </picture>
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "images" / "diagrams"

# Advanced AI Society brand (advancedaisociety.org): near-black #0a0a0a,
# electric lime #cfff04, warm off-white #f0edea, reds #ff6568/#bf000f,
# Montserrat headings / Source Sans 3 body.
FONT = "Montserrat,'Source Sans 3',-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"

THEMES = {
    # Semantic keys kept from the previous palette; values are brand-mapped:
    #   purple -> the accent inversion (black box/lime text on light; lime/black on dark)
    #   red    -> brand red (Tier 1 / not-PoC)
    #   yellow -> warm neutral from the #f0edea family (Tier 2)
    #   green  -> lime tint (Tier 3 / evidence)
    #   blue   -> solid lime, the brand moment (Tier 4 / Proof-of-Control)
    "light": {
        "text": "#0a0a0a", "muted": "#6b665f", "line": "#6b665f",
        "box_fill": "#f0edea", "box_stroke": "#d8d3cc",
        "purple": "#0a0a0a", "purple_text": "#cfff04",
        "green_fill": "#f2ffb8", "green_stroke": "#7a9900", "green_text": "#3d4d00",
        "yellow_fill": "#e7e3dd", "yellow_stroke": "#8a857e", "yellow_text": "#3d3a36",
        "red_fill": "#ffe3e4", "red_stroke": "#bf000f", "red_text": "#7a000a",
        "blue_fill": "#cfff04", "blue_stroke": "#0a0a0a", "blue_text": "#0a0a0a",
    },
    "dark": {
        "text": "#f0edea", "muted": "#8f8a82", "line": "#8f8a82",
        "box_fill": "#161616", "box_stroke": "#2e2e2e",
        "purple": "#cfff04", "purple_text": "#0a0a0a",
        "green_fill": "#222b00", "green_stroke": "#cfff04", "green_text": "#e3ff66",
        "yellow_fill": "#1d1c1a", "yellow_stroke": "#6e6a63", "yellow_text": "#b5b0a8",
        "red_fill": "#2a1214", "red_stroke": "#ff6568", "red_text": "#ff9a9c",
        "blue_fill": "#cfff04", "blue_stroke": "#cfff04", "blue_text": "#0a0a0a",
    },
}


class SVG:
    def __init__(self, w, h, theme):
        self.w, self.h, self.t = w, h, theme
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" font-family="{FONT}">'
        ]

    def text(self, x, y, s, size=13, fill=None, bold=False, anchor="middle"):
        weight = ' font-weight="600"' if bold else ""
        fill = fill or self.t["text"]
        self.parts.append(
            f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}"{weight} '
            f'text-anchor="{anchor}">{s}</text>'
        )

    def box(self, x, y, w, h, lines, fill=None, stroke=None, text_fill=None,
            dashed=False, rx=10, lh=17):
        fill = fill or self.t["box_fill"]
        stroke = stroke or self.t["box_stroke"]
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"{dash}/>'
        )
        n = len(lines)
        start = y + h / 2 - (n - 1) * lh / 2 + 4.5
        for i, spec in enumerate(lines):
            s, size, bold, fill_ = spec
            self.text(x + w / 2, start + i * lh, s, size=size,
                      fill=fill_ or text_fill or self.t["text"], bold=bold)

    def line(self, x1, y1, x2, y2, dashed=False, color=None, width=1.5):
        color = color or self.t["line"]
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        self.parts.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="{width}"{dash}/>'
        )

    def arrow(self, x1, y1, x2, y2, dashed=False, color=None):
        color = color or self.t["line"]
        self.line(x1, y1, x2, y2, dashed=dashed, color=color)
        if x1 == x2:  # vertical
            s = 1 if y2 > y1 else -1
            pts = f"{x2},{y2} {x2 - 5},{y2 - s * 9} {x2 + 5},{y2 - s * 9}"
        else:  # horizontal
            s = 1 if x2 > x1 else -1
            pts = f"{x2},{y2} {x2 - s * 9},{y2 - 5} {x2 - s * 9},{y2 + 5}"
        self.parts.append(f'<polygon points="{pts}" fill="{color}"/>')

    def save(self, name, variant):
        self.parts.append("</svg>")
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"{name}-{variant}.svg").write_text("\n".join(self.parts) + "\n")


def L(s, size=13, bold=False, fill=None):
    return (s, size, bold, fill)


# ---------------------------------------------------------------- diagrams

def standard_at_a_glance(t, v):
    s = SVG(1060, 330, t)
    s.text(135, 24, "WHAT — the six domains", 12, t["muted"], bold=True)
    s.box(20, 34, 230, 262, [], rx=12)
    for i, d in enumerate(["C1  Provenance", "C2  Privacy", "C3  Portability",
                           "C4  Authorization", "C5  Identity", "C6  Security"]):
        s.box(38, 48 + i * 40, 194, 32, [L(d, 12.5, True)], rx=8)
    s.box(300, 90, 215, 150, [
        L("HOW — C7", 11.5, True, t["purple_text"]),
        L("Action Interception Gateway", 13, True, t["purple_text"]),
        L("binary · contemporaneous", 11.5, False, t["purple_text"]),
        L("tamper-evident · transparent", 11.5, False, t["purple_text"]),
    ], fill=t["purple"], stroke=t["purple"])
    s.box(565, 90, 200, 150, [
        L("HOW MUCH — C8", 11.5, True, t["muted"]),
        L("Verifiability Tiers 1–4", 13, True),
        L("binary threshold", 11.5),
        L("at Tier 3", 11.5),
    ])
    s.box(815, 90, 225, 150, [
        L("CHECKED — C10", 11.5, True, t["muted"]),
        L("Self-Declared", 12.5),
        L("Third-Party Assessed", 12.5),
        L("Continuously Monitored", 12.5),
    ])
    s.arrow(250, 165, 298, 165)
    s.arrow(515, 165, 563, 165)
    s.arrow(765, 165, 813, 165)
    s.box(300, 268, 465, 42, [
        L("WHERE — C9 · evidence located on MAESTRO Layers 1–7", 12, False, t["muted"]),
    ], dashed=True, rx=8)
    s.line(407, 240, 407, 268, dashed=True)
    s.line(665, 240, 665, 268, dashed=True)
    s.save("standard-at-a-glance", v)


def tier_ladder(t, v):
    s = SVG(780, 480, t)
    boxes = [
        ("T4", 22, t["blue_fill"], t["blue_stroke"], t["blue_text"],
         ["Tier 4 — Self-Enforcing", "trust: no one — cannot run if integrity breaks",
          "✓ Proof-of-Control"]),
        ("T3", 128, t["green_fill"], t["green_stroke"], t["green_text"],
         ["Tier 3 — Independently Verifiable", "trust: the mathematics — anyone can check",
          "✓ Proof-of-Control"]),
        ("T2", 282, t["yellow_fill"], t["yellow_stroke"], t["yellow_text"],
         ["Tier 2 — Attestation", "trust: a third party or root-keeper",
          "✕ not Proof-of-Control"]),
        ("T1", 388, t["red_fill"], t["red_stroke"], t["red_text"],
         ["Tier 1 — Assertion", "trust: the operator's word",
          "✕ not Proof-of-Control"]),
    ]
    for _, y, fill, stroke, text, lines in boxes:
        s.box(150, y, 480, 84, [
            L(lines[0], 14.5, True, text),
            L(lines[1], 12, False, text),
            L(lines[2], 12, True, text),
        ], fill=fill, stroke=stroke)
    s.arrow(105, 460, 105, 34, color=t["muted"])
    s.parts.append(
        f'<text x="88" y="250" font-size="11.5" fill="{t["muted"]}" text-anchor="middle" '
        f'transform="rotate(-90 88 250)">less trust required</text>'
    )
    s.line(60, 237, 720, 237, dashed=True, color=t["purple"], width=2.5)
    s.box(230, 218, 320, 40, [
        L("THE BINARY THRESHOLD", 13, True, t["purple_text"]),
    ], fill=t["purple"], stroke=t["purple"], rx=20)
    s.text(390, 274, "below: authenticated documentation — above: mechanism-generated evidence",
           11.5, t["muted"])
    s.save("tier-ladder", v)


def conformance_stages(t, v):
    s = SVG(960, 290, t)
    s.box(20, 40, 270, 120, [
        L("Self-Declared", 14.5, True),
        L("operator publishes a", 12, False, t["muted"]),
        L("standardized statement", 12, False, t["muted"]),
        L("C10.1", 11, True, t["purple"] if v == "light" else t["purple"]),
    ])
    s.box(345, 40, 270, 120, [
        L("Third-Party Assessed", 14.5, True),
        L("accredited assessor examines", 12, False, t["muted"]),
        L("and confirms conformance", 12, False, t["muted"]),
        L("", 11),
    ])
    s.box(670, 40, 270, 120, [
        L("Continuously Monitored", 14.5, True),
        L("every in-scope action validated", 12, False, t["muted"]),
        L("as it occurs", 12, False, t["muted"]),
        L("C10.3", 11, True, t["purple"]),
    ])
    s.arrow(290, 100, 343, 100)
    s.arrow(615, 100, 668, 100)
    s.box(170, 212, 620, 48, [
        L("Trust-assumption disclosure — C10.2 · required at every stage", 12.5, True,
          t["yellow_text"]),
    ], fill=t["yellow_fill"], stroke=t["yellow_stroke"])
    for x in (155, 480, 805):
        s.line(x, 160, x if 170 < x < 790 else (200 if x == 155 else 760), 212, dashed=True)
    s.save("conformance-stages", v)


def document_map(t, v):
    s = SVG(960, 440, t)
    s.box(20, 20, 560, 400, [], rx=12)
    s.text(300, 46, "THE STANDARD — normative · 0.1/en/", 13, t["text"], bold=True)
    s.box(45, 66, 510, 84, [
        L("C1–C6 · The six domains", 13, True),
        L("Provenance · Privacy · Portability", 11.5, False, t["muted"]),
        L("Authorization · Identity · Security", 11.5, False, t["muted"]),
    ])
    s.box(45, 182, 510, 84, [
        L("C7–C10 · Cross-cutting requirements", 13, True),
        L("Evidence generation · Verifiability Tiers", 11.5, False, t["muted"]),
        L("System surface · Conformance", 11.5, False, t["muted"]),
    ])
    s.box(45, 298, 510, 84, [
        L("Appendices A–E", 13, True),
        L("Glossary · Mechanisms · Threat model", 11.5, False, t["muted"]),
        L("Open issues · Audit checklist", 11.5, False, t["muted"]),
    ])
    s.arrow(300, 150, 300, 180)
    s.arrow(300, 266, 300, 296)
    s.box(650, 66, 290, 120, [
        L("THE CASE — informative", 12.5, True),
        L("docs/", 12, True, t["purple"]),
        L("Introduction · Why it matters", 11.5, False, t["muted"]),
        L("Use cases · Roadmap · Governance", 11.5, False, t["muted"]),
    ])
    s.box(650, 254, 290, 120, [
        L("CROSSWALKS", 12.5, True),
        L("mappings/", 12, True, t["purple"]),
        L("MAESTRO · AARM · OWASP · ATLAS", 11.5, False, t["muted"]),
        L("NIST · ISO 42001 · SOC 2 · EU AI Act", 11.5, False, t["muted"]),
    ])
    s.arrow(580, 126, 648, 126, dashed=True)
    s.arrow(580, 314, 648, 314, dashed=True)
    s.text(610, 116, "explained by", 10.5, t["muted"])
    s.text(610, 304, "aligned via", 10.5, t["muted"])
    s.save("document-map", v)


def first_claim_journey(t, v):
    s = SVG(1080, 160, t)
    steps = [
        ("1", "Choose", "domains", "C1–C6"),
        ("2", "Locate on", "the stack", "C9"),
        ("3", "Choose", "mechanisms", "App. B"),
        ("4", "Meet the four", "properties", "C7"),
        ("5", "Grade on", "the Tiers", "C8"),
        ("6", "Disclose trust", "assumptions", "C10.2"),
        ("7", "Publish the", "statement", "C10.1"),
    ]
    for i, (n, l1, l2, ref) in enumerate(steps):
        x = 15 + i * 152
        last = i == len(steps) - 1
        fill = t["green_fill"] if last else t["box_fill"]
        stroke = t["green_stroke"] if last else t["box_stroke"]
        text = t["green_text"] if last else t["text"]
        s.box(x, 30, 130, 100, [
            L(n, 15, True, t["purple"]),
            L(l1, 12.5, True, text),
            L(l2, 12.5, True, text),
            L(ref, 11, False, t["muted"] if not last else text),
        ], fill=fill, stroke=stroke, lh=19)
        if not last:
            s.arrow(x + 130, 80, x + 150, 80)
    s.save("first-claim-journey", v)


def evidence_flow(t, v):
    s = SVG(940, 360, t)
    s.box(20, 60, 180, 90, [
        L("Agent", 14, True),
        L("plans an action", 12, False, t["muted"]),
    ])
    s.box(290, 45, 240, 120, [
        L("Action Interception", 14, True, t["purple_text"]),
        L("Gateway", 14, True, t["purple_text"]),
        L("out-of-band · C7.1", 11.5, False, t["purple_text"]),
    ], fill=t["purple"], stroke=t["purple"])
    s.box(660, 60, 180, 90, [
        L("Tool / effect", 14, True),
        L("executes", 12, False, t["muted"]),
    ])
    s.box(290, 235, 240, 100, [
        L("Evidence", 14, True, t["green_text"]),
        L("binary · contemporaneous", 11.5, False, t["green_text"]),
        L("tamper-evident · transparent", 11.5, False, t["green_text"]),
    ], fill=t["green_fill"], stroke=t["green_stroke"])
    s.box(640, 240, 280, 90, [
        L("Any verifier", 14, True),
        L("auditor · insurer · regulator", 11.5, False, t["muted"]),
        L("no privileged access", 11.5, False, t["muted"]),
    ])
    s.arrow(200, 95, 288, 95)
    s.text(244, 87, "action", 10.5, t["muted"])
    s.arrow(530, 90, 658, 90)
    s.text(594, 82, "authorized", 10.5, t["muted"])
    s.arrow(658, 125, 530, 125, dashed=True)
    s.text(594, 140, "result", 10.5, t["muted"])
    s.arrow(410, 165, 410, 233)
    s.text(495, 195, "before · during · after", 10.5, t["muted"])
    s.text(495, 210, "out of scope: rejected + evidenced", 10.5,
           t["red_stroke"])
    s.arrow(530, 285, 638, 285)
    s.save("evidence-flow", v)


def maestro_stack(t, v):
    s = SVG(660, 486, t)
    layers = [
        ("L7 · Agent Ecosystem", "marketplaces · registries · other agents"),
        ("L6 · Security, Governance & Compliance", "policy · change management · audit"),
        ("L5 · Evaluation & Observability", "tamper-evident logging · forensics"),
        ("L4 · Deployment & Infrastructure", "containers · networks · secrets · TEEs"),
        ("L3 · Agent Framework", "planning · tools · workflows · memory"),
        ("L2 · Data Operations", "ingestion · embeddings · RAG"),
        ("L1 · Foundation Model", "weights · serving · behavioral policy"),
    ]
    for i, (title, sub) in enumerate(layers):
        y = 20 + i * 64
        hl = title.startswith("L5")
        title = title.replace("&", "&amp;")
        if hl:
            s.box(50, y, 560, 56, [
                L(title, 13.5, True, t["purple_text"]),
                L(sub, 11.5, False, t["purple_text"]),
            ], fill=t["purple"], stroke=t["purple"])
        else:
            s.box(50, y, 560, 56, [
                L(title, 13.5, True),
                L(sub, 11.5, False, t["muted"]),
            ])
    s.text(330, 472, "L5 highlighted: without tamper-evident records, no post-hoc proof is possible",
           11.5, t["muted"])
    s.save("maestro-stack", v)


def risk_value_quadrant(t, v):
    s = SVG(680, 430, t)
    x0, y0, cw, ch = 110, 40, 260, 155
    s.text(370, 24, "The agent risk-to-value bind", 14, t["text"], bold=True)
    cells = [
        (x0, y0, t["red_fill"], t["red_stroke"], t["red_text"],
         ["Failed deployment", ""]),
        (x0 + cw, y0, t["yellow_fill"], t["yellow_stroke"], t["yellow_text"],
         ["Unleash", "value, but unquantifiable risk"]),
        (x0, y0 + ch, t["box_fill"], t["box_stroke"], t["muted"],
         ["Constrain", "safe, but can't do the job"]),
        (x0 + cw, y0 + ch, t["green_fill"], t["green_stroke"], t["green_text"],
         ["Proof-of-Control", "value up, risk down"]),
    ]
    for x, y, fill, stroke, text, lines in cells:
        s.box(x + 4, y + 4, cw - 8, ch - 8, [
            L(lines[0], 14, True, text),
            L(lines[1], 11.5, False, text),
        ], fill=fill, stroke=stroke, rx=8)
    s.text(x0 - 25, y0 + 18, "High", 11.5, t["muted"], anchor="end")
    s.text(x0 - 25, y0 + 32, "risk", 11.5, t["muted"], anchor="end")
    s.text(x0 - 25, y0 + 2 * ch - 30, "Low", 11.5, t["muted"], anchor="end")
    s.text(x0 - 25, y0 + 2 * ch - 16, "risk", 11.5, t["muted"], anchor="end")
    s.text(x0 + 40, y0 + 2 * ch + 28, "Low value", 11.5, t["muted"])
    s.text(x0 + 2 * cw - 40, y0 + 2 * ch + 28, "High value", 11.5, t["muted"])
    s.arrow(x0 - 60, y0 + 2 * ch, x0 - 60, y0, color=t["muted"])
    s.arrow(x0, y0 + 2 * ch + 46, x0 + 2 * cw, y0 + 2 * ch + 46, color=t["muted"])
    s.save("risk-value-quadrant", v)


def smart_leash(t, v):
    s = SVG(1080, 300, t)
    s.text(540, 30, "THE LEASH EVOLVES", 13, t["muted"], bold=True)
    s.text(540, 52, "trust me  →  trust my auditor  →  trust the math  →  the leash locks itself",
           13.5, t["text"], bold=True)
    nodes = [
        (20, t["yellow_fill"], t["yellow_stroke"], t["yellow_text"], "Iₐ", "PREREQUISITE",
         ["Whose dog is this?"], ["Collar tag and owner registration:", "identity, provenance, liability."]),
        (290, t["red_fill"], t["red_stroke"], t["red_text"], "T1", "TIER 1 · ASSERTION",
         ["The owner's word"], ["“My dog is friendly and stays in", "the yard.” They also write the", "incident report."]),
        (560, t["yellow_fill"], t["yellow_stroke"], t["yellow_text"], "T2", "TIER 2 · ATTESTATION",
         ["The inspector's badge"], ["A yearly paper stamp. It can't stop", "the dog jumping the fence today."]),
        (830, t["blue_fill"], t["blue_stroke"], t["blue_text"], "✓", "TIER 3–4 · PROOF-OF-CONTROL",
         ["The smart, tamper-proof leash"], ["Anyone can check the proof — and the", "leash locks before the boundary", "is crossed."]),
    ]
    # leash line across node centers
    s.parts.append(
        f'<defs><linearGradient id="leash" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{t["muted"]}"/>'
        f'<stop offset="0.35" stop-color="{t["red_stroke"]}"/>'
        f'<stop offset="0.65" stop-color="{t["yellow_stroke"]}"/>'
        f'<stop offset="1" stop-color="{"#7a9900" if v == "light" else "#cfff04"}"/>'
        f'</linearGradient></defs>'
        f'<rect x="60" y="94" width="960" height="4" rx="2" fill="url(#leash)"/>'
    )
    for x, fill, stroke, text, dot, tier, q, an in nodes:
        cx = x + 42
        s.parts.append(f'<circle cx="{cx}" cy="96" r="17" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        s.text(cx, 101, dot, 12.5, text, bold=True)
        s.text(x, 138, tier, 10.5, stroke if fill != t["blue_fill"] else ("#7a9900" if v == "light" else "#cfff04"), bold=True, anchor="start")
        s.text(x, 160, q[0], 14.5, t["text"], bold=True, anchor="start")
        for i, line in enumerate(an):
            s.text(x, 181 + i * 17, line, 11.5, t["muted"], anchor="start")
    s.text(540, 262, "as you move right — verifiability rises, trust required falls", 12, t["muted"])
    s.parts.append(
        f'<rect x="330" y="274" width="420" height="2" fill="{t["box_stroke"]}"/>'
    )
    s.save("smart-leash", v)


DIAGRAMS = [standard_at_a_glance, tier_ladder, conformance_stages, document_map,
            first_claim_journey, evidence_flow, maestro_stack, risk_value_quadrant,
            smart_leash]


def main():
    for variant, theme in THEMES.items():
        for fn in DIAGRAMS:
            fn(theme, variant)
    print(f"Generated {len(DIAGRAMS)} diagrams x {len(THEMES)} variants into {OUT}")


if __name__ == "__main__":
    main()
