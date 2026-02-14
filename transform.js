/**
 * BuyBlox Theme Transform Script
 *
 * Consolidated Node.js replacement for all legacy Python transform scripts.
 * Run with: node transform.js
 *
 * This script applies all CSS/HTML/JS cleanup and visual upgrades to
 * sections/homepage.liquid in a single pass:
 *   - Bug fixes (double %%, dead keyframes)
 *   - Seasonal leftover removal (petals, flowers, santa hats, confetti, butterfly, snow)
 *   - Dead code removal (hidden wave dividers, display:none elements, shimmer dedup)
 *   - Background upgrade (animated gradient, noise grain, dot grid, glass morphism)
 *   - Interactive JS optimization (from ~64 injected DOM elements to ~6 orbs)
 *
 * Handles CRLF/LF line endings automatically.
 */

const fs = require('fs');
const path = require('path');

const filepath = path.join(__dirname, 'sections', 'homepage.liquid');
let c = fs.readFileSync(filepath, 'utf-8');
const origLen = c.length;

// Normalize to LF for processing, convert back at end
const hadCRLF = c.includes('\r\n');
if (hadCRLF) c = c.replace(/\r\n/g, '\n').replace(/\r/g, '\n');

let misses = 0;
function rep(old, replacement) {
  if (!c.includes(old)) {
    misses++;
    console.log('  MISS: ' + old.slice(0, 80).replace(/\n/g, '\\n') + '...');
    return false;
  }
  c = c.replace(old, replacement);
  return true;
}

function repAll(old, replacement) {
  if (!c.includes(old)) {
    misses++;
    console.log('  MISS-ALL: ' + old.slice(0, 80).replace(/\n/g, '\\n') + '...');
    return false;
  }
  while (c.includes(old)) c = c.replace(old, replacement);
  return true;
}

// ================================================
// TASK 1: BUG FIXES
// ================================================
console.log('=== TASK 1: BUG FIXES ===');

// Fix double percent sign in Escape Tsunami discount display
rep('}}%%</span>', '}}%</span>');

// Remove dead body-glow keyframes (defined but never referenced)
rep(
  "@keyframes body-glow{0%{background-position:0% 50%}25%{background-position:50% 0%}50%{background-position:100% 50%}75%{background-position:50% 100%}100%{background-position:0% 50%}}\n",
  ""
);

// ================================================
// TASK 2: REMOVE SEASONAL LEFTOVERS
// ================================================
console.log('=== TASK 2: REMOVE SEASONAL LEFTOVERS ===');

// --- Petal fall CSS ---
c = c.replace(/\._476a0\{[^}]+\}\n/g, '');
c = c.replace(/\._476a0:nth-child\(\d+\)\{[^}]+\}\n/g, '');
c = c.replace(/@keyframes bbf-petalfall\{[^}]+\}/g, '');
rep('._61b61{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:1;overflow:hidden}\n', '');

c = c.replace(/\._584bb\{[^}]+\}\n/g, '');
c = c.replace(/\._584bb:nth-child\(\d+\)\{[^}]+\}\n/g, '');
c = c.replace(/@keyframes bbh-petalfall\{[^}]+\}/g, '');
rep('._99e32{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:1;overflow:hidden}\n', '');

c = c.replace(/\/\* Petals \*\/\n\._a512d \{\n[\s\S]*?@keyframes bbtr-petalfall \{\n[\s\S]*?\}\n\n/g, '');
c = c.replace(/\/\* Petals \*\/\n\._e145e \{\n[\s\S]*?@keyframes bbfaq-petalfall \{\n[\s\S]*?\}\n\n/g, '');

// Petal HTML containers
c = c.replace(/<div class="_61b61">\n[\s\S]*?<\/div>\n/g, function(m) {
  return m.includes('_476a0') ? '' : m;
});
rep('<div class="_99e32">\n\n</div>\n', '');
repAll('  <!-- Petals -->\n\n', '');

// --- Modal flower decorations ---
rep(
  "._a5ea2::before{content:'❀';position:absolute;top:8px;left:20px;font-size:20px;color:#D1D5DB;animation:bloom-spin 10s linear infinite}\n._a5ea2::after{content:'✿';position:absolute;top:12px;right:60px;font-size:18px;color:#FFA726;animation:bloom-spin 8s linear infinite reverse}",
  "._a5ea2::before{display:none}\n._a5ea2::after{display:none}"
);

// Flower stems
rep(
  "._f937c{position:absolute;top:0;width:2px;background:linear-gradient(180deg,#D1D5DB 0%,#E5E7EB 100%);z-index:1}\n._f937c::after{content:'✿';position:absolute;bottom:-16px;left:50%;transform:translateX(-50%);font-size:16px;color:#FFA726;text-shadow:0 0 8px rgba(255,167,38,.5);animation:bloom-spin 6s linear infinite}\n._f937c:nth-child(1){left:8%;height:30px}._f937c:nth-child(1)::after{animation-delay:0s}\n._f937c:nth-child(2){right:8%;height:35px}._f937c:nth-child(2)::after{content:'❀';font-size:14px;animation-delay:3s}",
  "._f937c{display:none}"
);

// --- Santa hat CSS ---
c = c.replace(/\/\* Santa hat on avatars \*\/\n\._1c601 \{[\s\S]*?\}\n\n/g, '');
c = c.replace(/\n  \._1c601 \{\n[\s\S]*?\}\n/g, '\n');

// --- FAQ confetti ---
c = c.replace(/\/\* Spring Confetti on FAQ Open \*\/\n\._818a4 \{[\s\S]*?\}\n\n@keyframes faq-confetti-fall \{[\s\S]*?\}\n\n/g, '');
c = c.replace(/function createFAQConfetti\(\) \{[\s\S]*?\n\}\n\n/g, '');
rep('    // Create confetti effect\n    createFAQConfetti();\n\n', '');

// --- Butterfly effect ---
c = c.replace(/\._8e588\{[^}]+\}\n/g, '');
c = c.replace(/@keyframes butterfly-float\{[^}]+\}\n/g, '');
c = c.replace(/\._04b48\{[^}]+\}\n/g, '');
c = c.replace(/@keyframes butterfly-trail-fall\{[^}]+\}\n/g, '');
c = c.replace(/function createButterflyEffect\(\)\{[^}]+\{[^}]+\}[^}]+\}\n/, '');
rep('if(m&&w){createButterflyEffect();w.innerHTML=', 'if(m&&w){w.innerHTML=');

// --- Modal petal snowfall ---
c = c.replace(/\._56054\{[^}]+\}\n/g, '');
c = c.replace(/@keyframes modal-petal-drift\{[^}]+\}\n/g, '');
c = c.replace(/\._90ff8\{[^}]+\}\n/g, '');
c = c.replace(/function createHeavySnow\(\)\{[^\n]+\}\n/, '');
rep("if(hs)hs.style.display='none';createHeavySnow();", "");
rep("if(hs)hs.style.display='';if(sf)sf.innerHTML=''", "");
rep('  <div class="_90ff8" id="modalSnowfall"></div>\n', '');
rep('  <div class="_2f0f5" id="heroSnowfall"></div>\n', '');
rep(",sf=document.getElementById('modalSnowfall'),hs=document.getElementById('heroSnowfall')", '');

// Spring container
rep('._a1df0{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:3;overflow:hidden}\n', '');

// Candy cane stripe → glass shine
rep(
  `._c6e6d::before {\n  content: '';\n  position: absolute;\n  top: 0;\n  left: 0;\n  right: 0;\n  bottom: 0;\n  background: repeating-linear-gradient(\n    135deg,\n    transparent,\n    transparent 8px,\n    rgba(255,255,255,0.15) 8px,\n    rgba(255,255,255,0.15) 16px\n  );\n  pointer-events: none;\n}`,
  `._c6e6d::before{content:'';position:absolute;top:0;left:-150%;width:200%;height:100%;background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,.25) 45%,rgba(255,255,255,.35) 50%,rgba(255,255,255,.25) 55%,transparent 60%);pointer-events:none;transition:left .6s cubic-bezier(.16,1,.3,1)}._c6e6d:hover::before{left:150%}`
);

// ================================================
// TASK 3: REMOVE DEAD CSS/HTML
// ================================================
console.log('=== TASK 3: REMOVE DEAD CSS/HTML ===');

// Hidden wave dividers
c = c.replace(/\/\* Bottom meadow transition \*\/\n\._69f80 \{\n[\s\S]*?\._69f80 svg \{\n[\s\S]*?\}\n/g, '');
c = c.replace(/\/\* Bottom meadow wave \*\/\n\._e5551 \{\n[\s\S]*?\._e5551 svg \{\n[\s\S]*?\}\n/g, '');
c = c.replace(/\._025ac\{[^}]+\}\n/g, '');
c = c.replace(/\._025ac svg\{[^}]+\}\n/g, '');
c = c.replace(/\._9fecd\{[^}]+\}\n/g, '');
c = c.replace(/\._9fecd svg\{[^}]+\}\n/g, '');
c = c.replace(/\n  <!-- Bottom Meadow Wave -->\n  <div class="_69f80">\n[\s\S]*?<\/div>\n/g, '\n');
c = c.replace(/\n  <!-- Bottom Meadow Wave -->\n  <div class="_e5551">\n[\s\S]*?<\/div>\n/g, '\n');

// display:none elements (CSS + HTML)
rep('._4ccfb {\n  display: none;\n}\n\n', '');
rep('._235cb{display:none}\n', '');
rep('._9eaaf {\n  display: none;\n}\n\n', '');
rep('._ab880 {\n  display: none;\n}\n\n', '');
rep('    <div class="_235cb"></div>\n', '');

// Deduplicate @keyframes shimmer
let shimmerCount = 0;
c = c.replace(/@keyframes shimmer\{0%,100%\{background-position:0% 0%\}50%\{background-position:100% 0%\}\}\n/g, function(m) {
  shimmerCount++;
  return shimmerCount === 1 ? m : '';
});
console.log('  Shimmer deduped: kept 1, removed ' + (shimmerCount - 1));

// ================================================
// TASK 4: BACKGROUND UPGRADE
// ================================================
console.log('=== TASK 4: BACKGROUND UPGRADE ===');

// Animated gradient + noise texture + dot grid on body
rep(
  '/* ===== FULL-PAGE LIVING GRADIENT (on body, behind everything) ===== */\nbody{background:#F0F4FF}',
  `/* ===== FULL-PAGE LIVING GRADIENT ===== */
body{background:linear-gradient(135deg,#DBEAFE 0%,#EDE9FE 20%,#CFFAFE 40%,#DBEAFE 60%,#F3E8FF 80%,#DBEAFE 100%);background-size:400% 400%;animation:bg-flow 30s ease infinite;position:relative}
@keyframes bg-flow{0%{background-position:0% 50%}25%{background-position:50% 0%}50%{background-position:100% 50%}75%{background-position:50% 100%}100%{background-position:0% 50%}}
/* ===== NOISE/GRAIN TEXTURE ===== */
body::after{content:'';position:fixed;inset:0;pointer-events:none;z-index:99998;opacity:0.03;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");mix-blend-mode:overlay}
/* ===== DOT GRID TEXTURE ===== */
body::before{content:'';position:fixed;inset:0;pointer-events:none;z-index:0;background-image:radial-gradient(circle,rgba(99,102,241,.04) 1px,transparent 1px);background-size:28px 28px}`
);

// Reduce hero blob opacity
rep(
  '._70520:nth-child(1){width:1100px;height:1100px;top:-20%;left:-15%;background:rgba(37,99,235,.5);opacity:.95;animation-duration:20s}',
  '._70520:nth-child(1){width:1100px;height:1100px;top:-20%;left:-15%;background:rgba(37,99,235,.25);opacity:.7;animation-duration:20s}'
);
rep(
  '._70520:nth-child(2){width:1000px;height:1000px;top:10%;right:-15%;background:rgba(124,58,237,.45);opacity:.9;animation-duration:28s;animation-delay:-7s}',
  '._70520:nth-child(2){width:1000px;height:1000px;top:10%;right:-15%;background:rgba(124,58,237,.2);opacity:.65;animation-duration:28s;animation-delay:-7s}'
);
rep(
  '._70520:nth-child(3){width:1200px;height:1200px;bottom:-25%;left:5%;background:rgba(6,182,212,.4);opacity:.85;animation-duration:32s;animation-delay:-14s}',
  '._70520:nth-child(3){width:1200px;height:1200px;bottom:-25%;left:5%;background:rgba(6,182,212,.18);opacity:.6;animation-duration:32s;animation-delay:-14s}'
);
rep(
  '._70520:nth-child(4){width:700px;height:700px;top:45%;left:40%;background:rgba(236,72,153,.38);opacity:.8;animation-duration:24s;animation-delay:-4s}',
  '._70520:nth-child(4){width:700px;height:700px;top:45%;left:40%;background:rgba(236,72,153,.15);opacity:.5;animation-duration:24s;animation-delay:-4s}'
);
rep(
  '._70520:nth-child(5){width:600px;height:600px;top:60%;right:10%;background:rgba(245,158,11,.32);opacity:.7;animation-duration:26s;animation-delay:-10s}',
  '._70520:nth-child(5){width:600px;height:600px;top:60%;right:10%;background:rgba(245,158,11,.12);opacity:.45;animation-duration:26s;animation-delay:-10s}'
);

// Semi-transparent hero section
rep(
  '._1e547{position:relative;width:100vw;left:50%;margin-left:-50vw;padding:0;background:linear-gradient(180deg,#DBEAFE 0%,#D4DAFF 50%,#DDD0F5 100%);overflow:hidden}',
  '._1e547{position:relative;width:100vw;left:50%;margin-left:-50vw;padding:0;background:linear-gradient(180deg,rgba(219,234,254,.85) 0%,rgba(212,218,255,.8) 50%,rgba(221,208,245,.85) 100%);overflow:hidden}'
);

// Semi-transparent other sections
rep(
  "background:linear-gradient(180deg,#D4DAFF 0%,#DADAFF 40%,#DDD0F5 100%);overflow:hidden;margin-top:-1px",
  "background:linear-gradient(180deg,rgba(212,218,255,.82) 0%,rgba(218,218,255,.78) 40%,rgba(221,208,245,.82) 100%);overflow:hidden;margin-top:-1px"
);
rep(
  "background:linear-gradient(180deg,#DDD0F5 0%,#D6DCFF 40%,#D4DAFF 100%);overflow:hidden}",
  "background:linear-gradient(180deg,rgba(221,208,245,.82) 0%,rgba(214,220,255,.78) 40%,rgba(212,218,255,.82) 100%);overflow:hidden}"
);
rep(
  "background: linear-gradient(180deg, #D4DAFF 0%, #D8D4FF 40%, #DBEAFE 100%);\n  overflow: hidden;",
  "background: linear-gradient(180deg, rgba(212,218,255,.82) 0%, rgba(216,212,255,.78) 40%, rgba(219,234,254,.82) 100%);\n  overflow: hidden;"
);
rep(
  "background: linear-gradient(180deg, #DBEAFE 0%, #D4DAFF 40%, #DDD0F5 100%);\n  overflow: hidden;",
  "background: linear-gradient(180deg, rgba(219,234,254,.82) 0%, rgba(212,218,255,.78) 40%, rgba(221,208,245,.82) 100%);\n  overflow: hidden;"
);

// Glass morphism on cards
rep(
  '._698ac{position:relative;background:var(--bg);border:3px solid #E2E8F0;',
  '._698ac{position:relative;background:rgba(255,255,255,.8);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:2px solid rgba(255,255,255,.5);'
);
rep(
  '._113e9{padding:16px;position:relative;z-index:2;background:#FFF;border-radius:0 0 15px 15px}',
  '._113e9{padding:16px;position:relative;z-index:2;background:rgba(255,255,255,.85);border-radius:0 0 15px 15px}'
);
rep(
  '._1ef0d{position:relative;background:#FFF;border:4px solid #E5E7EB;',
  '._1ef0d{position:relative;background:rgba(255,255,255,.8);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:2px solid rgba(255,255,255,.5);'
);
rep(
  '._605d9{background:#FFF;border:3px solid #E5E7EB;',
  '._605d9{background:rgba(255,255,255,.8);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:2px solid rgba(255,255,255,.5);'
);
rep(
  "._1264f {\n  background: #FFFFFF;\n  border: 3px solid #E5E7EB;",
  "._1264f {\n  background: rgba(255,255,255,.8);\n  backdrop-filter: blur(8px);\n  -webkit-backdrop-filter: blur(8px);\n  border: 2px solid rgba(255,255,255,.5);"
);
rep(
  "._a8c26 {\n  background: linear-gradient(135deg, #FFFFFF 0%, #FDFDFD 100%);\n  border: 3px solid #E5E7EB;",
  "._a8c26 {\n  background: rgba(255,255,255,.8);\n  backdrop-filter: blur(8px);\n  -webkit-backdrop-filter: blur(8px);\n  border: 2px solid rgba(255,255,255,.5);"
);
rep(
  "._e70fc {\n  flex: 0 0 auto;\n  width: 300px;\n  min-width: 300px;\n  background: linear-gradient(135deg, #FFFFFF 0%, #FDFDFD 100%);\n  border: 3px solid #E5E7EB;",
  "._e70fc {\n  flex: 0 0 auto;\n  width: 300px;\n  min-width: 300px;\n  background: rgba(255,255,255,.8);\n  backdrop-filter: blur(8px);\n  -webkit-backdrop-filter: blur(8px);\n  border: 2px solid rgba(255,255,255,.5);"
);
rep(
  '._a5a29{position:relative;display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,0.9);backdrop-filter:blur(10px);border:2px solid #E5E7EB;',
  '._a5a29{position:relative;display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,0.75);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.5);'
);
rep(
  '._a17fd{position:relative;overflow:hidden;margin:40px 20px 0;padding:20px 0 30px;background:rgba(255,255,255,0.9);backdrop-filter:blur(8px);border-radius:20px;border:1px solid #E5E7EB;',
  '._a17fd{position:relative;overflow:hidden;margin:40px 20px 0;padding:20px 0 30px;background:rgba(255,255,255,0.7);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-radius:20px;border:1px solid rgba(255,255,255,.5);'
);
rep(
  "._2a00b {\n  background: linear-gradient(135deg, #E5E7EB 0%, #E5E7EB 100%);\n  border: 3px solid #D1D5DB;",
  "._2a00b {\n  background: rgba(229,231,235,0.7);\n  backdrop-filter: blur(8px);\n  -webkit-backdrop-filter: blur(8px);\n  border: 2px solid rgba(255,255,255,.4);"
);
rep(
  "._ca7c4 {\n  background: linear-gradient(135deg, #E5E7EB 0%, #E5E7EB 100%);\n  border: 3px solid #D1D5DB;",
  "._ca7c4 {\n  background: rgba(229,231,235,0.7);\n  backdrop-filter: blur(8px);\n  -webkit-backdrop-filter: blur(8px);\n  border: 2px solid rgba(255,255,255,.4);"
);
rep(
  '._73a03{position:relative;background:rgba(255,255,255,0.97);',
  '._73a03{position:relative;background:rgba(255,255,255,0.85);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);'
);

// Remove V4 CSS overlays
c = c.replace(/\/\* ===== SECTION COLOR OVERLAYS[\s\S]*?@keyframes glow-c\{[^\}]+\{[^\}]+\}\}\n/g, '');

// Semi-transparent hero bottom fade
rep(
  '._0ac44{position:absolute;bottom:0;left:0;width:100%;height:80px;background:linear-gradient(180deg,transparent 0%,#D4DAFF 100%);pointer-events:none;z-index:7}',
  '._0ac44{position:absolute;bottom:0;left:0;width:100%;height:80px;background:linear-gradient(180deg,transparent 0%,rgba(212,218,255,.8) 100%);pointer-events:none;z-index:7}'
);

// ================================================
// TASK 5: SLIM DOWN INTERACTIVE JS
// ================================================
console.log('=== TASK 5: SLIM DOWN INTERACTIVE JS ===');

const oldJSStart = '// ===== INTERACTIVE BACKGROUND =====\n(function(){\n  var isTouch=\'ontouchstart\' in window||navigator.maxTouchPoints>0;\n\n  // --- Cursor glow (desktop only) ---';
const oldJSStartIdx = c.indexOf(oldJSStart);
if (oldJSStartIdx === -1) {
  console.log('  MISS: Could not find interactive JS block start');
} else {
  const endMarker = "  },{passive:true});\n})();\n\n// ===== SCROLL REVEAL =====";
  const endIdx = c.indexOf(endMarker, oldJSStartIdx);
  if (endIdx === -1) {
    console.log('  MISS: Could not find interactive JS block end');
  } else {
    const oldBlock = c.substring(oldJSStartIdx, endIdx + "  },{passive:true});\n})();".length);

    const newJS = `// ===== INTERACTIVE BACKGROUND =====
(function(){
  var isTouch='ontouchstart' in window||navigator.maxTouchPoints>0;

  // --- Cursor glow (desktop only) ---
  if(!isTouch){
    var glow=document.createElement('div');
    glow.setAttribute('data-cursor-glow','');
    document.body.appendChild(glow);
    var mx=innerWidth/2,my=innerHeight/2,gx=mx,gy=my,active=false,idle;
    document.addEventListener('mousemove',function(e){
      mx=e.clientX;my=e.clientY;
      if(!active){active=true;glow.classList.add('active')}
      clearTimeout(idle);
      idle=setTimeout(function(){active=false;glow.classList.remove('active')},3000);
    },{passive:true});
    (function animate(){
      gx+=(mx-gx)*.07;gy+=(my-gy)*.07;
      glow.style.left=gx+'px';glow.style.top=gy+'px';
      requestAnimationFrame(animate);
    })();
  }

  // --- Scroll parallax on hero mesh ---
  var mesh=document.querySelector('._8bf10');
  if(mesh){
    var ticking=false;
    window.addEventListener('scroll',function(){
      if(!ticking){requestAnimationFrame(function(){mesh.style.transform='translateY('+window.scrollY*.08+'px)';ticking=false});ticking=true}
    },{passive:true});
  }

  // --- Floating orbs (reduced count, glowing) ---
  var oCount=isTouch?3:6;
  var orbColors=['rgba(37,99,235,.15)','rgba(124,58,237,.12)','rgba(6,182,212,.14)','rgba(236,72,153,.1)','rgba(245,158,11,.11)','rgba(16,185,129,.12)'];
  for(var i=0;i<oCount;i++){
    var orb=document.createElement('div');
    orb.setAttribute('data-particle','');
    var size=(4+Math.random()*5);
    orb.style.cssText='left:'+Math.random()*100+'%;top:'+Math.random()*100+'%;width:'+size+'px;height:'+size+'px;background:'+orbColors[i%orbColors.length]+';box-shadow:0 0 '+(size*2)+'px '+orbColors[i%orbColors.length]+';animation-duration:'+(18+Math.random()*22)+'s;animation-delay:'+(-Math.random()*30)+'s;--p-drift:'+(Math.random()*50-25)+'px;--p-dist:'+(-(20+Math.random()*25))+'vh;--p-opacity:'+(0.3+Math.random()*0.3);
    document.body.appendChild(orb);
  }
})();`;

    c = c.replace(oldBlock, newJS);
    console.log('  OK: Replaced interactive JS block (' + oldBlock.length + ' -> ' + newJS.length + ' chars)');
  }
}

// Clean up excessive blank lines
c = c.replace(/\n{4,}/g, '\n\n\n');

// Convert back to CRLF if original had it
if (hadCRLF) c = c.replace(/\n/g, '\r\n');

fs.writeFileSync(filepath, c, 'utf-8');

const newLen = c.length;
console.log(`\nDone! ${origLen} -> ${newLen} chars (${origLen > newLen ? origLen - newLen : newLen - origLen} ${origLen > newLen ? 'removed' : 'added'})`);
if (misses > 0) console.log(`WARNING: ${misses} pattern(s) did not match`);

// Re-read as LF for verification
let v = fs.readFileSync(filepath, 'utf-8').replace(/\r\n/g, '\n');

const checks = {
  'No double %%': !v.includes('}}%%'),
  'No body-glow': !v.includes('@keyframes body-glow'),
  'No bbf-petalfall': !v.includes('bbf-petalfall'),
  'No bbh-petalfall': !v.includes('bbh-petalfall'),
  'No bbtr-petalfall': !v.includes('bbtr-petalfall'),
  'No bbfaq-petalfall': !v.includes('bbfaq-petalfall'),
  'Flowers disabled': v.includes('._a5ea2::before{display:none}'),
  'Stems disabled': v.includes('._f937c{display:none}'),
  'No FAQ confetti class': !v.includes('._818a4 {'),
  'No createFAQConfetti': !v.includes('createFAQConfetti'),
  'No butterfly': !v.includes('createButterflyEffect'),
  'No createHeavySnow': !v.includes('createHeavySnow'),
  'No heroSnowfall': !v.includes('heroSnowfall'),
  'Glass shine on help btn': v.includes('._c6e6d:hover::before{left:150%}'),
  'Noise texture': v.includes('feTurbulence'),
  'Dot grid CSS': v.includes("body::before{content:''"),
  'Animated body gradient': v.includes('bg-flow'),
  'Blobs reduced': v.includes("rgba(37,99,235,.25);opacity:.7"),
  'Glass product cards': v.includes('._698ac{position:relative;background:rgba(255,255,255,.8)'),
  'Glass step cards': v.includes('._1ef0d{position:relative;background:rgba(255,255,255,.8)'),
  'Glass FAQ items': v.includes('._a8c26 {\n  background: rgba(255,255,255,.8);'),
  'Glass review cards': v.includes('._e70fc {\n  flex: 0 0 auto;\n  width: 300px;\n  min-width: 300px;\n  background: rgba(255,255,255,.8);'),
  'Semi-transparent sections': v.includes('rgba(212,218,255,.82)'),
  'JS slimmed (6 orbs)': v.includes('oCount=isTouch?3:6'),
  'No JS dot grids': !v.includes("radial-gradient(circle,rgba(99,102,241,.06)"),
  'No JS blobs': !v.includes('blobGrads'),
  'No JS sweep': !v.includes('bg-sweep'),
  'No JS glow-pulse': !v.includes('glow-pulse'),
  'No JS pShapes': !v.includes('pShapes'),
  'Confetti kept': v.includes('canvas-confetti'),
};

console.log('\nVerification:');
let failures = 0;
for (const [name, val] of Object.entries(checks)) {
  if (!val) failures++;
  console.log(`  ${val ? 'OK' : 'XX'}: ${name}`);
}
console.log(`\n${failures === 0 ? 'ALL CHECKS PASSED!' : failures + ' CHECKS FAILED'}`);
