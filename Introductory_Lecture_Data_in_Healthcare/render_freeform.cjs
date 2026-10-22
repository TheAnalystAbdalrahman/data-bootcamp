const fs=require('fs'),path=require('path');
const {chromium}=require('C:/Users/abdal/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
const b=await chromium.launch({headless:true,executablePath:'C:/Users/abdal/AppData/Local/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-win64/chrome-headless-shell.exe'});
const p=await b.newPage({viewport:{width:2100,height:1313}});
const dir=path.join(__dirname,'Freeform_Previews');
const svg=fs.readFileSync(path.join(dir,'Map.svg'),'utf8');
await p.setContent('<style>body{margin:0}svg{width:2100px;height:1313px}</style>'+svg);
await p.screenshot({path:path.join(dir,'Overview.png')});
await p.setViewportSize({width:1600,height:1100});
await p.setContent('<style>body{margin:0}svg{width:1600px;height:1100px}</style>'+svg.replace('viewBox="0 0 8400 5250"','viewBox="1600 1650 2800 1950"'));
await p.screenshot({path:path.join(dir,'Four_Types.png')});
const overflow=await p.locator('text').evaluateAll(es=>es.filter(e=>e.getBBox().width>1900).map(e=>e.textContent));
console.log(JSON.stringify({rendered:2,veryWideText:overflow}));await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
