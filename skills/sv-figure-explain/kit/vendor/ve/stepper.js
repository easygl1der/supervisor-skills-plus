/* Stepper / scene player (idea from visual-explainer diagrams.md, MIT (c) 2025 Nico Bailon).
 Markup: <figure class="ve-steps" data-steps="N"> parts with data-s="k" (appears at step k) or data-s="0 3 5" (always drawn, lit on 3,5)
 Optional data-only="k": visible only at step k. Captions: window.CAPS=[...] or <ol class="ve-capsrc"><li>..</ol>.
 Opens on the FULL picture (step N). API: window.veGo(fig,k); window.veStepsOf(fig). Each step may call window.onStep(k,fig). */
(function(){
function init(fig){
  const N=+fig.dataset.steps; const src=fig.querySelector('.ve-capsrc'); const caps=src?[...src.children].map(li=>li.innerHTML):(window.CAPS||[]);
  if(src)src.remove();
  const bar=document.createElement('div');bar.className='ve-player';
  bar.innerHTML='<button data-go="-1" aria-label="上一步">◀</button><button data-play aria-label="播放">▶ 播放</button><input type="range" min="1" max="'+N+'" value="'+N+'" aria-label="步骤"><button data-go="1" aria-label="下一步">▶</button><span class="ve-pos"></span>';
  const cap=document.createElement('p');cap.className='ve-cap';cap.setAttribute('aria-live','polite');
  fig.appendChild(cap);fig.appendChild(bar);
  const range=bar.querySelector('input'),pos=bar.querySelector('.ve-pos');let cur=N,timer=null;
  function go(k){cur=Math.max(1,Math.min(N,k));range.value=cur;pos.textContent=cur+' / '+N;
    fig.querySelectorAll('[data-s]').forEach(el=>{const ss=el.dataset.s.trim().split(/\s+/).map(Number);const first=ss[0];
      el.classList.toggle('off',first>cur && !(first===0));el.classList.toggle('now',ss.includes(cur)&&cur!==N);});
    fig.querySelectorAll('[data-only]').forEach(el=>{el.classList.toggle('off',+el.dataset.only!==cur)});
    cap.innerHTML=caps[cur-1]||'';if(window.renderMathInElement)renderMathInElement(cap,{delimiters:[{left:'$',right:'$',display:false}]});
    if(window.onStep)window.onStep(cur,fig);}
  bar.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;
    if(b.dataset.go){stop();go(cur+ +b.dataset.go);} else if(b.hasAttribute('data-play')){if(timer)stop();else{if(cur>=N)go(1);b.textContent='❚❚ 暂停';timer=setInterval(()=>{if(cur>=N)stop();else go(cur+1)},1600);}}});
  function stop(){clearInterval(timer);timer=null;bar.querySelector('[data-play]').textContent='▶ 播放';}
  range.addEventListener('input',()=>{stop();go(+range.value)});
  fig.__go=go;fig.__N=N;go(+(new URLSearchParams(location.search).get('step'))||N);
}
window.veGo=(fig,k)=>fig.__go(k);window.veStepsOf=fig=>fig.__N;
window.veInit=()=>document.querySelectorAll('.ve-steps').forEach(init);
})();
