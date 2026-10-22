const fs=require('fs'), path=require('path');
const base='C:/Users/abdal/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/';
const {chromium}=require(base+'playwright');
const sharp=require(base+'sharp');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Users/abdal/AppData/Local/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-win64/chrome-headless-shell.exe'});
 const page=await browser.newPage({viewport:{width:1600,height:1000},deviceScaleFactor:1});
 const dir=path.join(__dirname,'Board_Previews');
 const scenes=JSON.parse(fs.readFileSync(path.join(dir,'scenes.json'),'utf8'));
 const problems=[];
 for(const s of scenes){
   await page.goto('file:///'+path.join(dir,`scene_${s.key}.html`).replaceAll('\\','/'));
   await page.screenshot({path:path.join(dir,`scene_${s.key}.png`)});
   const overflow=await page.locator('.txt').evaluateAll(es=>es.filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.textContent));
   if(overflow.length) problems.push({scene:s.key,overflow});
 }
 const composites=[];
 for(let i=0;i<scenes.length;i++) composites.push({input:await sharp(path.join(dir,`scene_${scenes[i].key}.png`)).resize(480,300).toBuffer(),left:(i%3)*500,top:Math.floor(i/3)*320});
 await sharp({create:{width:1500,height:1280,channels:3,background:'#E2E8F0'}}).composite(composites).png().toFile(path.join(dir,'Overview.png'));
 await browser.close();
 console.log(JSON.stringify({rendered:scenes.length,overflow:problems}));
})().catch(e=>{console.error(e.message);process.exit(1)});
