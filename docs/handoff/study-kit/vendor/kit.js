// study-kit: drawDAG(spec) -> SVG with KaTeX labels. spec = {nodes:[{id,label,x?,y?,dashed?,color?}], edges:[{from,to,label?,dashed?,color?,labelPos?}], layout:'manual'|'elk'|'dagre', r, width?, height?}
window.__READY = false;
const K = s => (window.katex ? katex.renderToString(s, { throwOnError: false }) : s);
function tex(str){ // "收入 $\\tau$" -> mixed html
  return str.split(/(\$[^$]+\$)/).map(p => p.startsWith('$') ? K(p.slice(1, -1)) : p).join(''); }
async function layoutELK(spec, r){
  const elk = new ELK();
  const g = await elk.layout({ id:'root', layoutOptions:{'elk.algorithm':'layered','elk.direction':spec.direction||'RIGHT','elk.spacing.nodeNode':'40','elk.layered.spacing.nodeNodeBetweenLayers':'90','elk.edgeRouting':'SPLINES'},
    children: spec.nodes.map(n => ({ id:n.id, width:2*r, height:2*r })), edges: spec.edges.map((e,i) => ({ id:'e'+i, sources:[e.from], targets:[e.to] })) });
  g.children.forEach(c => { const n = spec.nodes.find(n => n.id === c.id); n.x = c.x + r + 20; n.y = c.y + r + 20; });
  spec.width ??= g.width + 2*r; spec.height ??= g.height + 40;
}
function layoutDagre(spec, r){
  const g = new dagre.graphlib.Graph(); g.setGraph({ rankdir: spec.direction==='DOWN'?'TB':'LR', nodesep:40, ranksep:90 }); g.setDefaultEdgeLabel(()=>({}));
  spec.nodes.forEach(n => g.setNode(n.id, { width:2*r, height:2*r })); spec.edges.forEach(e => g.setEdge(e.from, e.to)); dagre.layout(g);
  spec.nodes.forEach(n => { const p = g.node(n.id); n.x = p.x + 20; n.y = p.y + 20; });
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
    const a = by[e.from], b = by[e.to], dx = b.x-a.x, dy = b.y-a.y, L = Math.hypot(dx,dy), ux = dx/L, uy = dy/L;
    const x1 = a.x+ux*r, y1 = a.y+uy*r, x2 = b.x-ux*(r+2), y2 = b.y-uy*(r+2);
    s += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${e.color||'var(--ink)'}" stroke-width="1.8" ${e.dashed?'stroke-dasharray="7 5"':''} marker-end="url(#ah)"/>`;
    if (e.label){ const off = e.labelOffset || 18, side = e.side==='left'?-1:1; // normal offset
      const mx = (x1+x2)/2 - uy*off*side, my = (y1+y2)/2 + ux*off*side; s += fo(mx, my, tex(e.label)); }
  }
  for (const n of spec.nodes){
    s += `<circle cx="${n.x}" cy="${n.y}" r="${r}" fill="${n.fill||'#fff'}" stroke="${n.color||'var(--ink)'}" stroke-width="1.8" ${n.dashed?'stroke-dasharray="6 5"':''}/>`;
    s += fo(n.x, n.y, tex(n.label), 'label node', 2*r);
  }
  host.innerHTML = s + '</svg>';
}
