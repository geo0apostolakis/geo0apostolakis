#!/usr/bin/env python3
"""Builds banner.svg: the name drawn out of 3D candlesticks, printed left to right
like a live chart, with the story as a price line underneath. Pure SVG + SMIL so it
animates inside a GitHub README (no scripts, no web fonts)."""
import random
from pathlib import Path

W, H = 880, 360
X0, CW, CH = 44, 12, 12
ROWS = [("GEORGE", 64), ("APOSTOLAKIS", 170)]
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

GLYPHS = {
    "G": [".###.", "#...#", "#....", "#.###", "#...#", "#...#", ".###."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "K": ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"],
    "I": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "#####"],
}

rnd = random.Random(4011)  # fixed seed: same banner every build


def candles(word, y0):
    """Every vertical run of lit cells in a column becomes one candle."""
    out, col = [], 0
    for ch in word:
        g = GLYPHS[ch]
        for c in range(5):
            r = 0
            while r < 7:
                if g[r][c] == "#":
                    s = r
                    while r < 7 and g[r][c] == "#":
                        r += 1
                    out.append((col + c, s, r - 1))
                else:
                    r += 1
        col += 6
    res = []
    for c, r0, r1 in out:
        cx = X0 + c * CW + CW / 2
        top, bot = y0 + r0 * CH + 1.5, y0 + (r1 + 1) * CH - 1.5
        res.append(dict(cx=cx, top=top, bot=bot, down=rnd.random() < 0.2,
                        wt=rnd.uniform(2, 6), wb=rnd.uniform(2, 6)))
    return res


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


parts = []
add = parts.append
add(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="George Apostolakis">')
add("<title>George Apostolakis</title>")
add("<defs>")
add('<linearGradient id="up" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd59a"/><stop offset=".45" stop-color="#ff8a2a"/><stop offset="1" stop-color="#ff5f03"/></linearGradient>')
add('<linearGradient id="dn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2571b"/><stop offset="1" stop-color="#8a2a0c"/></linearGradient>')
add('<radialGradient id="bgglow" cx=".82" cy=".18" r=".7"><stop offset="0" stop-color="#ff5f03" stop-opacity=".16"/><stop offset="1" stop-color="#ff5f03" stop-opacity="0"/></radialGradient>')
add('<linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff7a1a" stop-opacity=".28"/><stop offset="1" stop-color="#ff7a1a" stop-opacity="0"/></linearGradient>')
add('<linearGradient id="edge" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe2b8" stop-opacity="0"/><stop offset=".5" stop-color="#ffe2b8"/><stop offset="1" stop-color="#ffe2b8" stop-opacity="0"/></linearGradient>')
add('<filter id="glow" x="-10%" y="-40%" width="120%" height="180%"><feGaussianBlur stdDeviation="7"/></filter>')
add('<filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2"/></filter>')

rows = []
for i, (word, y0) in enumerate(ROWS):
    cs = candles(word, y0)
    rows.append((word, y0, cs))
    add(f'<g id="b{i}">' + "".join(
        f'<rect x="{f(c["cx"]-4)}" y="{f(c["top"])}" width="8" height="{f(c["bot"]-c["top"])}" rx="1.2"/>' for c in cs) + "</g>")
    end = X0 + (len(word) * 6 - 1) * CW + 30
    begin, dur = (0.25, 1.1) if i == 0 else (1.0, 1.6)
    add(f'<clipPath id="c{i}"><rect x="0" y="0" width="0" height="{H}">'
        f'<animate attributeName="width" from="0" to="{end}" begin="{begin}s" dur="{dur}s" fill="freeze" calcMode="spline" keySplines=".45 0 .25 1" keyTimes="0;1"/></rect></clipPath>')
add('<clipPath id="cl"><rect x="0" y="0" width="0" height="360"><animate attributeName="width" from="0" to="880" begin="2.4s" dur="2s" fill="freeze" calcMode="spline" keySplines=".4 0 .2 1" keyTimes="0;1"/></rect></clipPath>')
add("</defs>")

# card + grid
add(f'<rect width="{W}" height="{H}" rx="18" fill="#0c0a09"/>')
add(f'<rect width="{W}" height="{H}" rx="18" fill="url(#bgglow)"/>')
grid = "".join(f'<line x1="24" x2="{W-24}" y1="{y}" y2="{y}"/>' for y in range(52, 340, 24))
grid += "".join(f'<line y1="44" y2="340" x1="{x}" x2="{x}"/>' for x in range(44, W - 20, 72))
add(f'<g stroke="#ffffff" stroke-opacity=".045" stroke-width="1">{grid}</g>')
add(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="17.5" fill="none" stroke="#ffffff" stroke-opacity=".08"/>')

# top bar
add(f'<g font-family="{MONO}" font-size="12" fill="#8c8178">'
    f'<text x="44" y="32">geo0apostolakis <tspan fill="#5d554f">/ chart: name, 1D</tspan></text>'
    f'<text x="{W-44}" y="32" text-anchor="end">ATHENS, GR <tspan fill="#ff7a1a" dx="10">●<animate attributeName="fill-opacity" values="1;.15;1" dur="1.4s" repeatCount="indefinite"/></tspan><tspan fill="#ffb066"> LIVE</tspan></text>'
    "</g>")

# name rows: extrusion, glow, wicks, bodies
for i, (word, y0, cs) in enumerate(rows):
    add(f'<g clip-path="url(#c{i})">')
    for k, col in zip(range(6, 0, -1), ["#1a0802", "#240b03", "#2f0f04", "#3d1405", "#4f1a06", "#652207"]):
        add(f'<use href="#b{i}" xlink:href="#b{i}" fill="{col}" transform="translate({f(k*1.15)} {f(k*1.15)})"/>')
    add(f'<use href="#b{i}" xlink:href="#b{i}" fill="#ff6a00" filter="url(#glow)" opacity=".5">'
        f'<animate attributeName="opacity" values=".32;.78;.32" dur="3.6s" begin="{i*0.9}s" repeatCount="indefinite"/></use>')
    wicks = "".join(f'<line x1="{f(c["cx"])}" x2="{f(c["cx"])}" y1="{f(c["top"]-c["wt"])}" y2="{f(c["bot"]+c["wb"])}"/>' for c in cs)
    add(f'<g stroke="#ffb066" stroke-opacity=".75" stroke-width="1.5" stroke-linecap="round">{wicks}</g>')
    for c in cs:
        anim = ""
        if rnd.random() < 0.22:
            anim = (f'<animate attributeName="opacity" values="1;.35;1" dur="{rnd.uniform(2.2,5.5):.2f}s" '
                    f'begin="{rnd.uniform(2.6,7):.2f}s" repeatCount="indefinite"/>')
        fill = "url(#dn)" if c["down"] else "url(#up)"
        add(f'<rect x="{f(c["cx"]-4)}" y="{f(c["top"])}" width="8" height="{f(c["bot"]-c["top"])}" rx="1.2" fill="{fill}">{anim}</rect>')
    add("</g>")
    # bright leading edge that prints the row
    end = X0 + (len(word) * 6 - 1) * CW + 30
    begin, dur = (0.25, 1.1) if i == 0 else (1.0, 1.6)
    add(f'<rect x="0" y="{y0-14}" width="2" height="{7*CH+28}" fill="url(#edge)" opacity="0">'
        f'<animate attributeName="x" from="0" to="{end}" begin="{begin}s" dur="{dur}s" fill="freeze" calcMode="spline" keySplines=".45 0 .25 1" keyTimes="0;1"/>'
        f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.85;1" begin="{begin}s" dur="{dur}s" fill="freeze"/></rect>')

# whoami panel to the right of the first row
lines = [("$ whoami", "#ff8a2a"), ("15 · athens, greece", "#d8cfc7"), ("builds ai software", "#b3a89e"),
         ("invests in the ai stack", "#b3a89e"), ("next company: loading", "#b3a89e")]
add(f'<g font-family="{MONO}" font-size="13" text-anchor="end" opacity="0">'
    '<animate attributeName="opacity" from="0" to="1" begin="1.3s" dur=".6s" fill="freeze"/>')
for j, (t, col) in enumerate(lines):
    add(f'<text x="{W-50}" y="{74+j*17}" fill="{col}">{t}</text>')
add("</g>")
add(f'<rect x="{W-40}" y="{74+4*17-11}" width="7" height="13" fill="#ff8a2a" opacity="0">'
    '<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1s" begin="1.9s" repeatCount="indefinite"/></rect>')

# story line: a price chart of the path so far
base, top = 330, 276
miles = [("origami '20", 0.06, 0.12), ("python '24", 0.27, 0.34), ("first sales '24", 0.43, 0.5),
         ("ai agency '25", 0.62, 0.72), ("investing '26", 0.8, 0.66), ("next", 0.97, 1.0)]
xs = lambda t: X0 + t * (W - 2 * X0)
ys = lambda v: base - v * (base - top)
pts, prev = [(xs(0), ys(0.05))], (0, 0.05)
for _, t, v in miles:
    steps = 6
    for s in range(1, steps):
        tt = prev[0] + (t - prev[0]) * s / steps
        vv = prev[1] + (v - prev[1]) * s / steps + rnd.uniform(-0.09, 0.09)
        pts.append((xs(tt), ys(max(0.0, min(1.0, vv)))))
    pts.append((xs(t), ys(v)))
    prev = (t, v)
path = " ".join(f"{f(x)},{f(y)}" for x, y in pts)
add('<g clip-path="url(#cl)">')
add(f'<polygon points="{f(pts[0][0])},{base} {path} {f(pts[-1][0])},{base}" fill="url(#area)"/>')
add(f'<polyline points="{path}" fill="none" stroke="#ff8a2a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
add(f'<polyline points="{path}" fill="none" stroke="#ff6a00" stroke-width="5" opacity=".35" filter="url(#soft)"/>')
add(f'<g font-family="{MONO}" font-size="10.5" fill="#8c8178">')
for name, t, v in miles:
    x, y = xs(t), ys(v)
    anchor = "end" if t > 0.9 else "middle"
    add(f'<circle cx="{f(x)}" cy="{f(y)}" r="3" fill="#0c0a09" stroke="#ffb066" stroke-width="1.5"/>')
    add(f'<text x="{f(x)}" y="{base+18}" text-anchor="{anchor}">{name}</text>')
add("</g></g>")
ex, ey = xs(miles[-1][1]), ys(miles[-1][2])
add(f'<circle cx="{f(ex)}" cy="{f(ey)}" r="4" fill="#ffb066" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="4.3s" dur=".3s" fill="freeze"/></circle>')
add(f'<circle cx="{f(ex)}" cy="{f(ey)}" r="4" fill="none" stroke="#ff8a2a" stroke-width="1.5" opacity="0">'
    '<animate attributeName="r" values="4;14" dur="1.8s" begin="4.4s" repeatCount="indefinite"/>'
    '<animate attributeName="opacity" values=".9;0" dur="1.8s" begin="4.4s" repeatCount="indefinite"/></circle>')
add("</svg>")

out = Path(__file__).resolve().parent.parent / "banner.svg"
out.write_text("\n".join(parts) + "\n")
print(out, out.stat().st_size, "bytes")
