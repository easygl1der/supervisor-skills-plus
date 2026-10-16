import {chromium} from '/workspace/study-kit/node_modules/playwright-core/index.mjs';
const b=await chromium.launch({channel:process.env.CH||undefined,executablePath:process.env.CHROME});const p=await b.newPage({viewport:{width:1100,height:900},deviceScaleFactor:2});
const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.argv[2]);await p.waitForFunction('window.__READY');
await p.screenshot({path:process.argv[3],fullPage:true});console.log('errors',errs);await b.close();
