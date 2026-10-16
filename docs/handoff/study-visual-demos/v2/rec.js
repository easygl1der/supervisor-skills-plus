const {chromium}=require(process.env.PW);(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:960,height:540}});await p.goto('file://'+process.cwd()+'/a1_anim.html');
const t0=Date.now();let i=0;require('fs').mkdirSync('fr',{recursive:true});while(Date.now()-t0<4500){await p.screenshot({path:`fr/${String(i++).padStart(4,'0')}.png`});}
console.log(i,'frames');await b.close();})();
