// study-kit: drawDAG(spec) -> SVG with KaTeX labels. spec = {nodes:[{id,label,x?,y?,dashed?,color?}], edges:[{from,to,label?,dashed?,color?,side?,labelOffset?}] (elk/dagre routes are kept), layout:'manual'|'elk'|'dagre', r, width?, height?}
window.__READY = false;
const K = s => (window.katex ? katex.renderToString(s, { throwOnError: false }) : s);
function tex(str){ // "收入 $\\tau$" -> mixed html
  return str.split(/(\$[^$]+\$)/).map(p => p.startsWith('$') ? K(p.slice(1, -1)) : p).join(''); }
async function layoutELK(spec, r){
  const elk = new ELK();
  const g = await elk.layout({ id:'root', layoutOptions:{'elk.algorithm':'layered','elk.direction':spec.direction||'RIGHT','elk.spacing.nodeNode':'40','elk.layered.spacing.nodeNodeBetweenLayers':'90','elk.edgeRouting':'SPLINES'},
    children: spec.nodes.map(n => ({ id:n.id, width:2*r, height:2*r })), edges: spec.edges.map((e,i) => ({ id:'e'+i, sources:[e.from], targets:[e.to] })) });
  g.children.forEach(c => { const n = spec.nodes.find(n => n.id === c.id); n.x = c.x + r + 20; n.y = c.y + r + 20; });
  // keep ELK's routed bend points so edges go around nodes instead of through them
  g.edges.forEach((ge, i) => { const sec = ge.sections && ge.sections[0]; if (sec) spec.edges[i].pts = [sec.startPoint, ...(sec.bendPoints || []), sec.endPoint].map(q => [q.x + 20, q.y + 20]); });
  spec.width ??= g.width + 2*r; spec.height ??= g.height + 40;
}
function layoutDagre(spec, r){
  const g = new dagre.graphlib.Graph(); g.setGraph({ rankdir: spec.direction==='DOWN'?'TB':'LR', nodesep:40, ranksep:90 }); g.setDefaultEdgeLabel(()=>({}));
  spec.nodes.forEach(n => g.setNode(n.id, { width:2*r, height:2*r })); spec.edges.forEach(e => g.setEdge(e.from, e.to)); dagre.layout(g);
  spec.nodes.forEach(n => { const p = g.node(n.id); n.x = p.x + 20; n.y = p.y + 20; });
  spec.edges.forEach(e => { const ge = g.edge(e.from, e.to); if (ge && ge.points) e.pts = ge.points.map(q => [q.x + 20, q.y + 20]); });
  spec.width ??= g.graph().width + 40; spec.height ??= g.graph().height + 40;
}
async function drawDAG(spec, host){
  const r = spec.r || 26;
  if (spec.layout === 'elk') await layoutELK(spec, r); else if (spec.layout === 'dagre') layoutDagre(spec, r);
  const W = spec.width || 800, H = spec.height || 400, NS = 'http://www.w3.org/2000/svg';
  const by = Object.fromEntries(spec.nodes.map(n => [n.id, n]));
  let s = `<svg xmlns="${NS}" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L3,5z" fill="context-stroke"/></marker></defs>`;
  const fo = (x, y, html, cls='label', w=160) => `<foreignObject x="${x-w/2}" y="${y-16}" width="${w}" height="32"><div xmlns="http://www.w3.org/1999/xhtml" class="${cls}" style="display:flex;justify-content:center;align-items:center;height:32px;font-size:15px">${html}</div></foreignObject>`;
  for (const e of spec.edges){
    const a = by[e.from], b = by[e.to];
    // route: layout points (elk/dagre) or a straight line; first and last segments clipped to the node circles
    const P = (e.pts && e.pts.length >= 2 ? e.pts.map(q => [...q]) : [[a.x, a.y], [b.x, b.y]]);
    P[0] = [a.x, a.y]; P[P.length-1] = [b.x, b.y];
    const clip = (c, toward, pad) => { const dx = toward[0]-c[0], dy = toward[1]-c[1], L = Math.hypot(dx, dy) || 1; return [c[0]+dx/L*(r+pad), c[1]+dy/L*(r+pad)]; };
    P[0] = clip(P[0], P[1], 0); P[P.length-1] = clip(P[P.length-1], P[P.length-2], 2);
    // smooth route through the layout points (quadratic segments via midpoints), straight when only two points
    const f = q => q[0].toFixed(1) + ',' + q[1].toFixed(1), mid = (u, v) => [(u[0]+v[0])/2, (u[1]+v[1])/2];
    let d = 'M' + f(P[0]);
    if (P.length === 2) d += ' L' + f(P[1]);
    else { d += ' L' + f(mid(P[0], P[1])); for (let i = 1; i < P.length - 1; i++) d += ' Q' + f(P[i]) + ' ' + f(i === P.length - 2 ? P[i+1] : mid(P[i], P[i+1])); }
    s += `<path d="${d}" fill="none" stroke="${e.color||'var(--ink)'}" stroke-width="1.8" stroke-linejoin="round" ${e.dashed?'stroke-dasharray="7 5"':''} marker-end="url(#ah)"/>`;
    if (e.label){ // label at the middle of the route, offset along the normal of that segment
      const seg = P.slice(1).map((q, i) => Math.hypot(q[0]-P[i][0], q[1]-P[i][1])); let half = seg.reduce((x, y) => x + y, 0) / 2, i = 0;
      while (i < seg.length - 1 && half > seg[i]) { half -= seg[i]; i++; }
      const ux = (P[i+1][0]-P[i][0]) / (seg[i] || 1), uy = (P[i+1][1]-P[i][1]) / (seg[i] || 1);
      const cx = P[i][0] + ux*half, cy = P[i][1] + uy*half, off = e.labelOffset || 18, side = e.side==='left'?-1:1;
      s += fo(cx - uy*off*side, cy + ux*off*side, tex(e.label)); }
  }
  for (const n of spec.nodes){
    s += `<circle cx="${n.x}" cy="${n.y}" r="${r}" fill="${n.fill||'#fff'}" stroke="${n.color||'var(--ink)'}" stroke-width="1.8" ${n.dashed?'stroke-dasharray="6 5"':''}/>`;
    s += fo(n.x, n.y, tex(n.label), 'label node', 2*r);
  }
  host.innerHTML = s + '</svg>';
}
