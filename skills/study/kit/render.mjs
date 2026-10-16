// Usage: node render.mjs in.html [out.png] [--scale 2] [--full] [--figures] [--steps] [--gif]
// --full: whole page; --figures: also each <figure> -> out-figN.png; --steps: each .ve-steps -> out-stepK.png + out-strip.png (+ --gif out.gif via ffmpeg)
// Renders #fig (or body) with headless Chrome, waits for window.__READY, then self-checks:
// text-box overlaps, labels crossed by lines (opt out: data-cross-ok), edges passing through nodes, elements overflowing #fig, KaTeX errors, unresolved {{placeholders}}.
import { chromium } from 'playwright-core';
import path from 'node:path';
const args = process.argv.slice(2);
const inp = path.resolve(args[0]); const out = args[1] && !args[1].startsWith('--') ? args[1] : inp.replace(/\.html?$/, '.png');
const scale = Number(args[args.indexOf('--scale') + 1]) || 2;
import fs0 from 'node:fs';
// Chrome: $CHROME, else the first existing default for macOS / Linux / Windows
const exe = process.env.CHROME || ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser', 'C:/Program Files/Google/Chrome/Application/chrome.exe'].find(f => fs0.existsSync(f));
if (!exe) { console.log(JSON.stringify({ out: null, warnings: ['no Chrome found: set CHROME=/path/to/chrome'] })); process.exit(3); }
const t0 = Date.now();
const b = await chromium.launch({ executablePath: exe, args: ['--allow-file-access-from-files'] });
const p = await b.newPage({ deviceScaleFactor: scale, viewport: { width: 1200, height: 800 } });
const errs = []; p.on('pageerror', e => errs.push(e.message));
await p.goto('file://' + inp);
await p.waitForFunction(() => window.__READY !== false, null, { timeout: 15000 }).catch(() => errs.push('timeout waiting __READY'));
await p.evaluate(() => document.fonts.ready);
// tall viewport so elementsFromPoint works for every point of the page (occlusion test below)
const fullH = await p.evaluate(() => Math.ceil(document.documentElement.scrollHeight));
await p.setViewportSize({ width: 1200, height: Math.min(Math.max(800, fullH), 12000) });
const report = await p.evaluate(() => {
  const fig = document.querySelector('#fig') || document.body; const F = fig.getBoundingClientRect();
  // tight text bounds: an HTML label's box can be far wider than its text (flex containers, foreignObject)
  const tight = e => { if (e instanceof SVGElement || e.classList.contains("katex") || e.querySelector(".katex")) return e.getBoundingClientRect(); const rg = document.createRange(); rg.selectNodeContents(e);
    const r = rg.getBoundingClientRect(); return r.width > 0 ? r : e.getBoundingClientRect(); };
  const W = [];
  const boxes = [...fig.querySelectorAll('text, .label, .katex, h1,h2,h3,p,li,span.t')].filter(e => !e.closest('.katex-html') || e.classList.contains('katex'))
    .map(e => ({ e, r: tight(e), s: (e.textContent || '').trim().slice(0, 20) })).filter(o => o.r.width > 0 && o.s && !o.e.closest('.off') && getComputedStyle(o.e).visibility !== 'hidden');
  for (let i = 0; i < boxes.length; i++) {
    const a = boxes[i].r;
    if (a.left < F.left - 1 || a.right > F.right + 1 || a.top < F.top - 1 || a.bottom > F.bottom + 1) W.push(`overflow: "${boxes[i].s}"`);
    for (let j = i + 1; j < boxes.length; j++) {
      if (boxes[i].e.contains(boxes[j].e) || boxes[j].e.contains(boxes[i].e)) continue;
      const c = boxes[j].r; const ox = Math.min(a.right, c.right) - Math.max(a.left, c.left), oy = Math.min(a.bottom, c.bottom) - Math.max(a.top, c.top);
      if (ox > 2 && oy > 2) W.push(`overlap: "${boxes[i].s}" × "${boxes[j].s}"`);
    }
  }
  // text-on-line: sample points along visible SVG strokes; a point inside a label box means a line runs through text
  const strokes = [...fig.querySelectorAll('svg line, svg path, svg polyline')].filter(g => !g.closest('defs, marker, pattern, [data-cross-ok]')
    && getComputedStyle(g).stroke !== 'none' && getComputedStyle(g).visibility !== 'hidden' && !g.closest('.off') && typeof g.getTotalLength === 'function');
  // a stroke point is hidden when an opaque box or label background is stacked above it
  const opaque = el => { for (let e = el; e && e !== fig; e = e.parentElement) { const cs = getComputedStyle(e);
      const bg = cs.backgroundColor; if (bg && !/rgba\(.*,\s*0\)$|transparent/.test(bg)) return true;
      if (/^(rect|circle|ellipse|polygon)$/.test(e.tagName) && cs.fill !== 'none' && !/rgba\(.*,\s*0\)$/.test(cs.fill) && Number(cs.fillOpacity) > 0.8) return true; }
    return false; };
  const visible = (g, x, y) => { const st = document.elementsFromPoint(x, y); const k = st.findIndex(e => e === g || g.contains(e));
    const above = k < 0 ? st : st.slice(0, k); return !above.some(e => !g.contains(e) && opaque(e)); };
  const labels = boxes.filter(o => !o.e.closest('[data-cross-ok]')).map(o => ({ s: o.s, r: o.r }));
  const shapes = [...fig.querySelectorAll('svg circle, svg ellipse, svg rect')].filter(e => !e.closest('defs, marker, pattern') && opaque(e)
    && e.getBoundingClientRect().width >= 16 && e.getBoundingClientRect().width < F.width * 0.8);
  for (const g of strokes) {
    let L = 0; try { L = g.getTotalLength(); } catch { continue; }
    const m = g.getScreenCTM(); if (!m || L < 8) continue; const hits = new Map();
    for (let d = 0; d <= L; d += 3) {
      const q = g.getPointAtLength(d); const x = m.a * q.x + m.c * q.y + m.e, y = m.b * q.x + m.d * q.y + m.f;
      for (const o of labels) if (x > o.r.left + 2 && x < o.r.right - 2 && y > o.r.top + 2 && y < o.r.bottom - 2 && visible(g, x, y)) hits.set(o.s, (hits.get(o.s) || 0) + 1);
    }
    for (const [lab, n] of hits) if (n >= 2) W.push(`text-on-line: "${lab}"`);
    // edge-through-node: both ends of the stroke lie outside a node shape but its middle runs inside it
    const pts = []; for (let d = 0; d <= L; d += 3) { const q = g.getPointAtLength(d); pts.push([m.a * q.x + m.c * q.y + m.e, m.b * q.x + m.d * q.y + m.f]); }
    for (const sh of shapes) { if (sh === g || sh.contains(g)) continue; const R = sh.getBoundingClientRect();
      const inside = ([x, y]) => x > R.left + 3 && x < R.right - 3 && y > R.top + 3 && y < R.bottom - 3 && document.elementsFromPoint(x, y).includes(sh);
      if (inside(pts[0]) || inside(pts[pts.length - 1])) continue;
      let run = 0, best = 0; for (const q of pts) { run = inside(q) ? run + 1 : 0; best = Math.max(best, run); }
      if (best >= 3) W.push(`edge-through-node: a line crosses "${(sh.parentElement?.textContent || sh.id || sh.tagName).trim().slice(0, 16)}"`); }
  }
  document.querySelectorAll('.katex-error').forEach(e => W.push('katex-error: ' + e.title));
  if (/\{\{[^}]+\}\}/.test(fig.innerText)) W.push('unfilled {{placeholder}}');
  return W;
});
const has = f => args.includes(f); const stem = out.replace(/\.png$/, '');
await p.addStyleTag({ content: '[data-s]{transition:none!important}' });
if (has('--full')) await p.screenshot({ path: out, fullPage: true });
else { const el = await p.$('#fig') || await p.$('body'); await el.screenshot({ path: out, omitBackground: false }); }
if (has('--figures')) { const figs = await p.$$('figure'); for (let i = 0; i < figs.length; i++) await figs[i].screenshot({ path: `${stem}-fig${i + 1}.png` }); }
if (has('--steps')) {
  const fs = await import('node:fs'); const { execFileSync } = await import('node:child_process');
  const steppers = await p.$$('.ve-steps');
  for (let si = 0; si < steppers.length; si++) {
    const N = await p.evaluate(f => window.veStepsOf(f), steppers[si]); const tag = steppers.length > 1 ? `-s${si + 1}` : ''; const frames = [];
    for (let k = 1; k <= N; k++) { await p.evaluate(([f, k]) => window.veGo(f, k), [steppers[si], k]); await p.waitForTimeout(80);
      const fp = `${stem}${tag}-step${k}.png`; await steppers[si].screenshot({ path: fp }); frames.push(fp); }
    await p.evaluate(f => window.veGo(f, window.veStepsOf(f)), steppers[si]);
    try { // strip: vertical stack (ffmpeg vstack), gif: 1.4s per frame
      execFileSync('ffmpeg', ['-y', '-loglevel', 'error', ...frames.flatMap(f => ['-i', f]), '-filter_complex', `${frames.map((_, i) => `[${i}]`).join('')}vstack=inputs=${frames.length},scale=iw/2:-1`, `${stem}${tag}-strip.png`]);
      if (has('--gif')) { const list = `${stem}${tag}-frames.txt`; fs.writeFileSync(list, frames.map(f => `file '${f}'\nduration 1.4`).join('\n') + `\nfile '${frames.at(-1)}'\n`);
        execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list, '-vf', 'scale=900:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse', `${stem}${tag}.gif`]); fs.unlinkSync(list); }
    } catch (e) { errs.push('ffmpeg: ' + e.message.split('\n')[0]); }
  }
}
await b.close();
const all = [...errs.map(e => 'js-error: ' + e), ...report];
console.log(JSON.stringify({ out, ms: Date.now() - t0, warnings: all }));
process.exit(all.length ? 2 : 0);
