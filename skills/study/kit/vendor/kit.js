// study-kit: drawDAG(spec) -> SVG with KaTeX labels.
// spec = {nodes:[{id,label,x?,y?,r?,dashed?,color?,fill?}], edges:[{from,to,label?,dashed?,color?,side?,labelOffset?,noArrow?}],
//         layout:'manual'|'elk'|'dagre', r, width?, height?, direction?,
//         spacing?:{node,layer}   gaps for elk/dagre (default 40 / 90),
//         fitLabels?:true         grow each circle so its label fits (otherwise r or node.r),
//         labelsAsNodes?:true     elk/dagre: each edge label becomes a text node the layout makes room for;
//                                 the edge into it has no arrow, so A -verb-> B still reads as one edge}
window.__READY = false;
const K = s => (window.katex ? katex.renderToString(s, { throwOnError: false }) : s);
function tex(str){ // "收入 $\\tau$" -> mixed html
  return str.split(/(\$[^$]+\$)/).map(p => p.startsWith('$') ? K(p.slice(1, -1)) : p).join(''); }
// measure label html with the page's own fonts (same box as the foreignObject below)
function measure(host, html, cls){
  const d = document.createElement('div'); d.className = cls;
  d.style.cssText = 'position:absolute;visibility:hidden;white-space:nowrap;font-size:15px;left:-9999px';
  d.innerHTML = html; host.appendChild(d); const w = d.getBoundingClientRect().width; d.remove(); return w; }
// half sizes of a node box: circles are 2r square, text nodes are their measured label
const box = n => n.text ? [n.w/2, n.h/2] : [n.r, n.r];
async function layoutELK(nodes, edges, spec){
  const sp = spec.spacing || {}, elk = new ELK();
  const g = await elk.layout({ id:'root', layoutOptions:{'elk.algorithm':'layered','elk.direction':spec.direction||'RIGHT','elk.spacing.nodeNode':String(sp.node??40),'elk.layered.spacing.nodeNodeBetweenLayers':String(sp.layer??90),'elk.spacing.edgeNode':'16','elk.edgeRouting':'SPLINES'},
    children: nodes.map(n => { const [hw, hh] = box(n); return { id:n.id, width:2*hw, height:2*hh }; }), edges: edges.map((e,i) => ({ id:'e'+i, sources:[e.from], targets:[e.to] })) });
  g.children.forEach(c => { const n = nodes.find(n => n.id === c.id); n.x = c.x + c.width/2 + 20; n.y = c.y + c.height/2 + 20; });
  // keep ELK's routed bend points (and its spread-out end points) so edges go around nodes and do not all meet in one spot
  g.edges.forEach((ge, i) => { const sec = ge.sections && ge.sections[0]; if (sec) edges[i].pts = [sec.startPoint, ...(sec.bendPoints || []), sec.endPoint].map(q => [q.x + 20, q.y + 20]); });
  spec.width ??= g.width + 40; spec.height ??= g.height + 40;
}
function layoutDagre(nodes, edges, spec){
  const sp = spec.spacing || {}, g = new dagre.graphlib.Graph({ multigraph:true });
  g.setGraph({ rankdir: spec.direction==='DOWN'?'TB':'LR', nodesep:sp.node??40, ranksep:sp.layer??90 }); g.setDefaultEdgeLabel(()=>({}));
  nodes.forEach(n => { const [hw, hh] = box(n); g.setNode(n.id, { width:2*hw, height:2*hh }); });
  edges.forEach((e, i) => g.setEdge(e.from, e.to, {}, 'e'+i)); dagre.layout(g);
  nodes.forEach(n => { const p = g.node(n.id); n.x = p.x + 20; n.y = p.y + 20; });
  edges.forEach((e, i) => { const ge = g.edge(e.from, e.to, 'e'+i); if (ge && ge.points) e.pts = ge.points.map(q => [q.x + 20, q.y + 20]); });
  spec.width ??= g.graph().width + 40; spec.height ??= g.graph().height + 40;
}
// point on the border of node n in direction (dx,dy), pushed out by pad
function border(n, dx, dy, pad){
  const L = Math.hypot(dx, dy) || 1, ux = dx/L, uy = dy/L;
  if (!n.text) return [n.x + ux*(n.r+pad), n.y + uy*(n.r+pad)];
  const [hw, hh] = box(n), t = Math.min(ux ? hw/Math.abs(ux) : Infinity, uy ? hh/Math.abs(uy) : Infinity);
  return [n.x + ux*(t+pad), n.y + uy*(t+pad)]; }
async function drawDAG(spec, host){
  const r = spec.r || 26, auto = spec.layout === 'elk' || spec.layout === 'dagre';
  const nodes = spec.nodes.slice(), edges = [];
  for (const n of nodes){ // per-node radius; optionally grown to fit the label
    n.r = n.r || r;
    if (spec.fitLabels) n.r = Math.max(n.r, Math.ceil(measure(host, tex(n.label), 'label node') / 2) + 10); }
  spec.edges.forEach((e, i) => {
    if (!(auto && spec.labelsAsNodes && e.label)) return edges.push(e);
    const L = { id:'_lab'+i, text:true, label:e.label, color:e.color, h:28 };
    L.w = Math.ceil(measure(host, tex(e.label), 'label')) + 12; nodes.push(L);
    edges.push({ ...e, to:L.id, label:null, noArrow:true }, { ...e, from:L.id, label:null }); });
  if (spec.layout === 'elk') await layoutELK(nodes, edges, spec); else if (spec.layout === 'dagre') layoutDagre(nodes, edges, spec);
  const W = spec.width || 800, H = spec.height || 400, NS = 'http://www.w3.org/2000/svg';
  const by = Object.fromEntries(nodes.map(n => [n.id, n]));
  let s = `<svg xmlns="${NS}" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L3,5z" fill="context-stroke"/></marker></defs>`;
  const fo = (x, y, html, cls='label', w=160, style='') => `<foreignObject x="${x-w/2}" y="${y-16}" width="${w}" height="32"><div xmlns="http://www.w3.org/1999/xhtml" class="${cls}" style="display:flex;justify-content:center;align-items:center;height:32px;font-size:15px;${style}">${html}</div></foreignObject>`;
  for (const e of edges){
    const a = by[e.from], b = by[e.to];
    // route: layout points (elk/dagre) or a straight line. Ends go on the node border in the direction of the
    // layout's own end point (so several edges into one node stay apart), else toward the next route point.
    const P = (e.pts && e.pts.length >= 2 ? e.pts.map(q => [...q]) : [[a.x, a.y], [b.x, b.y]]);
    const away = (n, q, nb) => {
      const dx = q[0]-n.x, dy = q[1]-n.y;
      if (Math.hypot(dx, dy) <= 2) return [nb[0]-n.x, nb[1]-n.y];
      if (n.text) return [dx, dy];
      // circle: the layout spreads ports along one side of the 2r box (about +-45 deg); stretch that to +-70 deg
      const k = 1.22; // 70 deg in radians
      if (Math.abs(dx) >= Math.abs(dy)) { const a = Math.max(-1, Math.min(1, dy / n.r)) * k; return [Math.sign(dx) * Math.cos(a), Math.sin(a)]; }
      const a = Math.max(-1, Math.min(1, dx / n.r)) * k; return [Math.sin(a), Math.sign(dy) * Math.cos(a)]; };
    const d0 = away(a, P[0], P[1]), d1 = away(b, P[P.length-1], P[P.length-2]);
    P[0] = border(a, d0[0], d0[1], 0); P[P.length-1] = border(b, d1[0], d1[1], 2);
    // smooth route through the layout points (quadratic segments via midpoints), straight when only two points
    const f = q => q[0].toFixed(1) + ',' + q[1].toFixed(1), mid = (u, v) => [(u[0]+v[0])/2, (u[1]+v[1])/2];
    let d = 'M' + f(P[0]);
    if (P.length === 2) d += ' L' + f(P[1]);
    else { d += ' L' + f(mid(P[0], P[1])); for (let i = 1; i < P.length - 1; i++) d += ' Q' + f(P[i]) + ' ' + f(i === P.length - 2 ? P[i+1] : mid(P[i], P[i+1])); }
    s += `<path d="${d}" fill="none" stroke="${e.color||'var(--ink)'}" stroke-width="1.8" stroke-linejoin="round" ${e.dashed?'stroke-dasharray="7 5"':''} ${e.noArrow?'':'marker-end="url(#ah)"'}/>`;
    if (e.label){ // label at the middle of the route, offset along the normal of that segment
      const seg = P.slice(1).map((q, i) => Math.hypot(q[0]-P[i][0], q[1]-P[i][1])); let half = seg.reduce((x, y) => x + y, 0) / 2, i = 0;
      while (i < seg.length - 1 && half > seg[i]) { half -= seg[i]; i++; }
      const ux = (P[i+1][0]-P[i][0]) / (seg[i] || 1), uy = (P[i+1][1]-P[i][1]) / (seg[i] || 1);
      const cx = P[i][0] + ux*half, cy = P[i][1] + uy*half, off = e.labelOffset || 18, side = e.side==='left'?-1:1;
      s += fo(cx - uy*off*side, cy + ux*off*side, tex(e.label)); }
  }
  for (const n of nodes){
    if (n.text) { s += fo(n.x, n.y, tex(n.label), 'label edge-label', n.w, 'white-space:nowrap;' + (n.color ? `color:${n.color}` : '')); continue; }
    s += `<circle cx="${n.x}" cy="${n.y}" r="${n.r}" fill="${n.fill||'#fff'}" stroke="${n.color||'var(--ink)'}" stroke-width="1.8" ${n.dashed?'stroke-dasharray="6 5"':''}/>`;
    s += fo(n.x, n.y, tex(n.label), 'label node', 2*n.r);
  }
  host.innerHTML = s + '</svg>';
}
