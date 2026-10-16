// Usage: node render.mjs in.html [out.png] [--scale 2] [--full] [--figures] [--steps] [--gif]
// --full: whole page; --figures: also each <figure> -> out-figN.png; --steps: each .ve-steps -> out-stepK.png + out-strip.png (+ --gif out.gif via ffmpeg)
// Renders #fig (or body) with headless Chrome, waits for window.__READY, then self-checks:
// text-box overlaps, elements overflowing #fig, KaTeX errors, unresolved {{placeholders}}.
import { chromium } from 'playwright-core';
import path from 'node:path';
const args = process.argv.slice(2);
const inp = path.resolve(args[0]); const out = args[1] && !args[1].startsWith('--') ? args[1] : inp.replace(/\.html?$/, '.png');
const scale = Number(args[args.indexOf('--scale') + 1]) || 2;
const exe = process.env.CHROME || '/usr/bin/google-chrome';
const t0 = Date.now();
const b = await chromium.launch({ executablePath: exe, args: ['--allow-file-access-from-files'] });
const p = await b.newPage({ deviceScaleFactor: scale, viewport: { width: 1200, height: 800 } });
const errs = []; p.on('pageerror', e => errs.push(e.message));
await p.goto('file://' + inp);
await p.waitForFunction(() => window.__READY !== false, null, { timeout: 15000 }).catch(() => errs.push('timeout waiting __READY'));
await p.evaluate(() => document.fonts.ready);
const report = await p.evaluate(() => {
  const fig = document.querySelector('#fig') || document.body; const F = fig.getBoundingClientRect();
  const W = [];
  const boxes = [...fig.querySelectorAll('text, .label, .katex, h1,h2,h3,p,li,span.t')].filter(e => !e.closest('.katex-html') || e.classList.contains('katex'))
    .map(e => ({ e, r: e.getBoundingClientRect(), s: (e.textContent || '').trim().slice(0, 20) })).filter(o => o.r.width > 0 && o.s && !o.e.closest('.off') && getComputedStyle(o.e).visibility !== 'hidden');
  for (let i = 0; i < boxes.length; i++) {
    const a = boxes[i].r;
    if (a.left < F.left - 1 || a.right > F.right + 1 || a.top < F.top - 1 || a.bottom > F.bottom + 1) W.push(`overflow: "${boxes[i].s}"`);
    for (let j = i + 1; j < boxes.length; j++) {
      if (boxes[i].e.contains(boxes[j].e) || boxes[j].e.contains(boxes[i].e)) continue;
      const c = boxes[j].r; const ox = Math.min(a.right, c.right) - Math.max(a.left, c.left), oy = Math.min(a.bottom, c.bottom) - Math.max(a.top, c.top);
      if (ox > 2 && oy > 2) W.push(`overlap: "${boxes[i].s}" × "${boxes[j].s}"`);
    }
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
