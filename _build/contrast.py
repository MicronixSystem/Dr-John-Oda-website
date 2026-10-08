"""WCAG contrast check (rule D17) for every visible text element on a page.

Walks up from each element with its own text to the first opaque background
colour, computes the contrast ratio, and lists anything under AA
(4.5:1 normal text, 3:1 for 24px+ or 18.66px+ bold). Also prints the lowest
ratios found so the margins are visible.

Run: python contrast.py http://localhost:8765/index.html [width]
"""
import sys

from playwright.sync_api import sync_playwright

JS = r"""
() => {
  const parse = c => { const m = c.match(/[\d.]+/g); return m ? m.map(Number) : [0,0,0,0]; };
  const lin = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  const lum = ([r,g,b]) => 0.2126*lin(r) + 0.7152*lin(g) + 0.0722*lin(b);
  const blend = (fg, bg) => { const a = fg[3] === undefined ? 1 : fg[3];
    return [0,1,2].map(i => fg[i]*a + bg[i]*(1-a)); };
  const bgOf = el => {
    const stack = [];
    for (let n = el; n; n = n.parentElement) {
      const c = parse(getComputedStyle(n).backgroundColor);
      const a = c[3] === undefined ? 1 : c[3];
      if (a > 0) { stack.push(c); if (a >= 1) break; }
    }
    let bg = [255,255,255];
    for (let i = stack.length - 1; i >= 0; i--) bg = blend(stack[i], bg);
    return bg;
  };
  const out = [];
  for (const el of document.querySelectorAll('body *')) {
    const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (!own) continue;
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    if (!r.width || !r.height || cs.visibility === 'hidden' || cs.display === 'none') continue;
    if (el.closest('.sr-only, .skip-link, svg')) continue;
    const bg = bgOf(el);
    const fg = blend(parse(cs.color), bg);
    const L1 = lum(fg), L2 = lum(bg);
    const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
    const size = parseFloat(cs.fontSize), weight = parseInt(cs.fontWeight, 10);
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const text = [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').slice(0, 48);
    out.push({text, ratio: Math.round(ratio * 100) / 100, need: large ? 3 : 4.5, size, cls: el.className && el.className.baseVal === undefined ? el.className : el.tagName});
  }
  return out;
}
"""

url = sys.argv[1]
width = int(sys.argv[2]) if len(sys.argv) > 2 else 1440
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": width, "height": 900}, reduced_motion="reduce")
    pg.goto(url, wait_until="networkidle")
    rows = pg.evaluate(JS)
    b.close()

fails = [r for r in rows if r["ratio"] < r["need"]]
print(f"{width}px: {len(rows)} text elements checked, {len(fails)} below AA")
for r in fails:
    print(f"  FAIL {r['ratio']:>5} (need {r['need']}) {r['size']}px  {r['cls']!s:28.28}  {r['text']}")
low = sorted(rows, key=lambda r: r["ratio"] - r["need"])[:6]
print("  lowest margins:")
for r in low:
    print(f"    {r['ratio']:>5} (need {r['need']}) {r['size']}px  {r['cls']!s:28.28}  {r['text']}")
sys.exit(1 if fails else 0)
