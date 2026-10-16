import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams['font.family']=['Noto Sans CJK SC','Noto Sans Mono CJK SC','sans-serif']
rng=np.random.default_rng(1); n=150
fig,ax=plt.subplots(1,2,figsize=(12,5),dpi=130)
cols={'低收入':'#e8590c','高收入':'#1971c2'}
X=[];Y=[]
for g,(cm,lm) in {'低收入':(1,74),'高收入':(3,82)}.items():
    c=np.clip(rng.normal(cm,0.7,n),0,None); l=lm+rng.normal(0,2,n)
    X.append(c);Y.append(l)
    ax[1].scatter(c,l,s=14,alpha=.6,color=cols[g],label=g)
    b=np.polyfit(c,l,1); xs=np.linspace(c.min(),c.max(),2); ax[1].plot(xs,np.polyval(b,xs),color=cols[g],lw=2.5)
x=np.concatenate(X);y=np.concatenate(Y)
ax[0].scatter(x,y,s=14,alpha=.5,color='gray'); b=np.polyfit(x,y,1); xs=np.linspace(x.min(),x.max(),2)
ax[0].plot(xs,np.polyval(b,xs),'k',lw=2.5)
ax[0].set_title(f"① 不分组：咖啡越多越长寿？（斜率 {b[0]:.1f} 岁/杯）",fontsize=13)
ax[1].set_title("② 按收入分层：组内几乎无关（斜率≈0）",fontsize=13); ax[1].legend()
for a in ax: a.set_xlabel("每天咖啡杯数"); a.set_ylabel("寿命（岁）"); a.grid(alpha=.3)
fig.suptitle("模拟数据：混杂因素「收入」制造了虚假相关",fontsize=15); fig.tight_layout(); fig.savefig("2_scatter.png")
