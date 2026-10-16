import json,numpy as np,vl_convert as vlc
rng=np.random.default_rng(0);inc=rng.integers(0,3,300);cof=inc*1.2+rng.normal(0,.6,300);life=72+inc*4+rng.normal(0,1.5,300)
n=['低收入','中收入','高收入'];d=[{'咖啡':float(c),'寿命':float(l),'收入':n[i]} for c,l,i in zip(cof,life,inc)]
spec={"$schema":"https://vega.github.io/schema/vega-lite/v5.json","title":"分组回归线（Vega-Lite）","width":700,"height":400,"data":{"values":d},"config":{"font":"Noto Sans CJK SC"},
"layer":[{"mark":{"type":"point","filled":True},"encoding":{"x":{"field":"咖啡","type":"quantitative"},"y":{"field":"寿命","type":"quantitative","scale":{"zero":False}},"color":{"field":"收入"}}},
{"transform":[{"regression":"寿命","on":"咖啡","groupby":["收入"]}],"mark":"line","encoding":{"x":{"field":"咖啡","type":"quantitative"},"y":{"field":"寿命","type":"quantitative"},"color":{"field":"收入"}}},
{"transform":[{"regression":"寿命","on":"咖啡"}],"mark":{"type":"line","color":"red","strokeDash":[6,4]},"encoding":{"x":{"field":"咖啡","type":"quantitative"},"y":{"field":"寿命","type":"quantitative"}}}]}
json.dump(spec,open('p3_vega.vl.json','w'),ensure_ascii=False);open('p3_vega.png','wb').write(vlc.vegalite_to_png(json.dumps(spec),scale=2))
