import numpy as np,plotly.graph_objects as go
rng=np.random.default_rng(0);inc=rng.integers(0,3,300);cof=inc*1.2+rng.normal(0,.6,300);life=72+inc*4+rng.normal(0,1.5,300)
fig=go.Figure();names=['低收入','中收入','高收入']
for g in range(3):
  m=inc==g;fig.add_scatter(x=cof[m],y=life[m],mode='markers',name=names[g])
fig.update_layout(title='咖啡与寿命：按收入着色（Plotly）',xaxis_title='每日咖啡杯数',yaxis_title='寿命',font_family='Noto Sans CJK SC',template='plotly_white',width=900,height=520)
fig.write_html('p2_plotly.html');fig.write_image('p2_plotly.png',scale=2)
