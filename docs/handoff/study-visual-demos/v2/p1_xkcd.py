import numpy as np,matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
fm.fontManager.addfont('/home/box/.local/share/fonts/from-mac/mini/LXGWWenKai-Light.ttf')
rng=np.random.default_rng(0);inc=rng.integers(0,3,300);cof=inc*1.2+rng.normal(0,.6,300);life=72+inc*4+rng.normal(0,1.5,300)
with plt.xkcd():
  plt.rcParams['font.family']=['LXGW WenKai']
  f,a=plt.subplots(1,2,figsize=(11,4.6))
  a[0].scatter(cof,life,c='gray',s=12);b=np.polyfit(cof,life,1);xx=np.linspace(cof.min(),cof.max());a[0].plot(xx,np.polyval(b,xx),'r');a[0].set_title('不分组：多喝一杯多活 %.1f 年？'%b[0]);a[0].set_xlabel('每日咖啡杯数');a[0].set_ylabel('寿命')
  for g,c,n in zip(range(3),['#e67e22','#3498db','#27ae60'],['低收入','中收入','高收入']):
    m=inc==g;a[1].scatter(cof[m],life[m],c=c,s=12,label=n);bb=np.polyfit(cof[m],life[m],1);x2=np.linspace(cof[m].min(),cof[m].max());a[1].plot(x2,np.polyval(bb,x2),c=c)
  a[1].set_title('按收入分组：组内几乎平');a[1].legend();a[1].set_xlabel('每日咖啡杯数')
  plt.tight_layout();plt.savefig('p1_xkcd.png',dpi=130)
