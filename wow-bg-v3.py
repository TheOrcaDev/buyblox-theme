import re

filepath = r'C:\Users\User\buyblox-theme\sections\homepage.liquid'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# FULL-PAGE LIVING BACKGROUND + CLEANUP
# Approach: Fixed gradient blobs behind everything,
# frosted glass sections, clean premium feel.
# Remove all gimmicky effects. Less effects, more impact.
# ============================================================

# ====================
# A. REMOVE GIMMICKS
# ====================

# 1. Remove shooting stars CSS
content = content.replace(
    """/* ===== SHOOTING STARS ===== */
[data-shooting-star]{position:fixed;width:80px;height:2px;background:linear-gradient(90deg,var(--star-color,#3B82F6),transparent);border-radius:2px;pointer-events:none;z-index:9998;opacity:0;animation:shooting-star-move var(--star-dur,.8s) ease-out forwards;filter:drop-shadow(0 0 6px var(--star-color,#3B82F6))}
[data-shooting-star]::before{content:'';position:absolute;right:0;top:-1px;width:4px;height:4px;background:var(--star-color,#3B82F6);border-radius:50%;box-shadow:0 0 8px var(--star-color,#3B82F6),0 0 16px var(--star-color,#3B82F6)}
@keyframes shooting-star-move{0%{transform:rotate(var(--star-angle,-25deg)) translateX(0);opacity:0}10%{opacity:1}100%{transform:rotate(var(--star-angle,-25deg)) translateX(min(60vw,600px));opacity:0}}""",
    "")

# 2. Remove click ripple CSS
content = content.replace(
    """/* ===== CLICK RIPPLE ===== */
[data-click-ripple]{position:fixed;width:0;height:0;border-radius:50%;pointer-events:none;z-index:9997;transform:translate(-50%,-50%);border:2px solid rgba(37,99,235,.4);animation:click-ripple-expand .7s ease-out forwards}
@keyframes click-ripple-expand{0%{width:0;height:0;opacity:.8}100%{width:200px;height:200px;opacity:0}}""",
    "")

# 3. Remove rainbow hero border CSS
content = content.replace(
    """/* ===== ANIMATED HERO GLOW BORDER ===== */
._1e547::after{content:'';position:absolute;bottom:0;left:5%;right:5%;height:2px;background:linear-gradient(90deg,transparent,#3B82F6,#8B5CF6,#06B6D4,#10B981,#F59E0B,#EC4899,#3B82F6,transparent);background-size:200% 100%;animation:rainbow-border 4s linear infinite;z-index:8;filter:blur(1px);opacity:.6}
@keyframes rainbow-border{0%{background-position:0% 0%}100%{background-position:200% 0%}}
""",
    "")

# 4. Remove breathing overlay (._1e547::before)
content = content.replace(
    """/* ===== WOW BACKGROUND ENHANCEMENTS ===== */
._1e547::before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,transparent 0%,rgba(124,58,237,.04) 25%,rgba(6,182,212,.06) 50%,rgba(37,99,235,.04) 75%,transparent 100%);z-index:0;pointer-events:none;opacity:0;animation:bg-breathe 8s ease-in-out infinite}
@keyframes bg-breathe{0%,100%{opacity:0}50%{opacity:1}}""",
    "")

# 5. Remove perspective grid + old transition
content = content.replace(
    "._8bf10{transition:filter .3s ease}\n/* ===== PREMIUM GRADIENT MESH ===== */",
    "/* ===== GRADIENT MESH ===== */")

content = content.replace(
    "._8bf10::after{content:'';position:absolute;inset:-20%;width:140%;height:140%;background-image:linear-gradient(rgba(37,99,235,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(37,99,235,.05) 1px,transparent 1px);background-size:50px 50px;z-index:2;animation:grid-drift 15s linear infinite;transform:perspective(500px) rotateX(30deg);transform-origin:50% 0%;mask-image:radial-gradient(ellipse 80% 60% at 50% 40%,black 30%,transparent 70%)}@keyframes grid-drift{0%{background-position:0 0}100%{background-position:50px 50px}}",
    "")

# 6. Remove modal emoji confetti function + call
content = content.replace(
    "function cf(){const e=['🌸','✨','🌷','🦋','🌿','🌼'];for(let i=0;i<12;i++){setTimeout(()=>{const d=document.createElement('div');d.className='_a2198';d.textContent=e[Math.floor(Math.random()*e.length)];d.style.left=(20+Math.random()*60)+'%';d.style.setProperty('--drift',(Math.random()*100-50)+'px');document.body.appendChild(d);setTimeout(()=>d.remove(),4500)},i*100)}}",
    "function cf(){}")  # Empty function so calls don't error

# 7. Remove modal confetti CSS
content = content.replace(
    "._a2198{position:fixed;pointer-events:none;z-index:100001;font-size:20px;animation:modal-confetti-fall 4s ease-out forwards}\n@keyframes modal-confetti-fall{0%{transform:translateY(-20px) rotate(0deg);opacity:0}10%{opacity:1}100%{transform:translateY(100vh) translateX(var(--drift,0)) rotate(360deg);opacity:0}}",
    "")


# ===================================
# B. FULL-PAGE FIXED BACKGROUND
# ===================================

# 8. Change blob CSS — less blur (60px for more visible shapes), more vivid
content = content.replace(
    "._70520{position:absolute;border-radius:50%;filter:blur(120px);animation:mesh-float ease-in-out infinite;will-change:transform}",
    "._70520{position:absolute;border-radius:50%;filter:blur(80px);animation:mesh-float ease-in-out infinite;will-change:transform}")

# Make blobs use vw units so they scale with viewport
content = content.replace(
    "._70520:nth-child(1){width:1000px;height:1000px;top:-25%;left:-15%;background:rgba(37,99,235,.3);opacity:.8;animation-duration:18s}",
    "._70520:nth-child(1){width:55vw;height:55vw;min-width:500px;min-height:500px;top:-10%;left:-15%;background:rgba(37,99,235,.22);opacity:.8;animation-duration:20s}")
content = content.replace(
    "._70520:nth-child(2){width:900px;height:900px;top:10%;right:-20%;background:rgba(124,58,237,.25);opacity:.7;animation-duration:25s;animation-delay:-7s}",
    "._70520:nth-child(2){width:45vw;height:45vw;min-width:400px;min-height:400px;top:15%;right:-10%;background:rgba(124,58,237,.2);opacity:.7;animation-duration:28s;animation-delay:-7s}")
content = content.replace(
    "._70520:nth-child(3){width:1100px;height:1100px;bottom:-25%;left:5%;background:rgba(6,182,212,.2);opacity:.6;animation-duration:30s;animation-delay:-14s}",
    "._70520:nth-child(3){width:50vw;height:50vw;min-width:450px;min-height:450px;top:40%;left:-5%;background:rgba(6,182,212,.18);opacity:.7;animation-duration:32s;animation-delay:-14s}")
content = content.replace(
    "._70520:nth-child(4){width:800px;height:800px;top:40%;left:40%;background:rgba(236,72,153,.18);opacity:.5;animation-duration:22s;animation-delay:-4s}",
    "._70520:nth-child(4){width:40vw;height:40vw;min-width:350px;min-height:350px;top:60%;right:5%;background:rgba(236,72,153,.15);opacity:.6;animation-duration:24s;animation-delay:-4s}")
content = content.replace(
    "._70520:nth-child(5){width:700px;height:700px;top:60%;right:10%;background:rgba(245,158,11,.15);opacity:.5;animation-duration:26s;animation-delay:-10s}",
    "._70520:nth-child(5){width:35vw;height:35vw;min-width:300px;min-height:300px;top:80%;left:20%;background:rgba(245,158,11,.12);opacity:.5;animation-duration:26s;animation-delay:-10s}")

# 9. Change ._8bf10 positioning — will be moved to fixed by JS
# Keep CSS as position:absolute (fallback), JS will override to fixed
# Just remove overflow:hidden so blobs can show beyond hero
content = content.replace(
    "._8bf10{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:1;overflow:hidden}",
    "._8bf10{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:1}")


# ===================================
# C. FROSTED GLASS SECTIONS
# ===================================

# 10. Hero — most transparent to show blobs prominently
content = content.replace(
    "._1e547{position:relative;width:100vw;left:50%;margin-left:-50vw;padding:0;background:linear-gradient(180deg,#FFFFFF 0%,#FAFCFF 30%,#F5F9FF 50%,#FAFCFF 70%,#FFFFFF 100%);overflow:hidden;min-height:80vh}",
    "._1e547{position:relative;width:100vw;left:50%;margin-left:-50vw;padding:0;background:rgba(255,255,255,0.55);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);overflow:hidden;min-height:80vh}")

# 11. Featured Products — slightly more opaque for readability
content = content.replace(
    "background:linear-gradient(180deg,#FFFFFF 0%,#FDFDFD 5%,#FDFDFD 15%,#FAFAFA 30%,#FAFAFA 50%,#E5E7EB 70%,#FAFAFA 85%,#FAFAFA 100%);overflow:hidden;margin-top:-1px",
    "background:rgba(255,255,255,0.75);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);overflow:hidden;margin-top:-1px")

# 12. How It Works
content = content.replace(
    "background:linear-gradient(180deg,#FAFAFA 0%,#FAFAFA 20%,#FDFDFD 50%,#FDFDFD 80%,#FFFFFF 100%);overflow:hidden",
    "background:rgba(255,255,255,0.7);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);overflow:hidden",
    1)  # Only first occurrence

# 13. Trust & Reviews
content = content.replace(
    "background: linear-gradient(180deg, #FFFFFF 0%, #FAFCFF 15%, #F5F9FF 40%, #F5F9FF 60%, #F5F9FF 80%, #FAFCFF 100%);\n  overflow: hidden;",
    "background: rgba(255,255,255,0.65);\n  backdrop-filter: blur(30px);\n  -webkit-backdrop-filter: blur(30px);\n  overflow: hidden;",
    1)

# 14. FAQ
content = content.replace(
    "background: linear-gradient(180deg, #FAFCFF 0%, #F5F9FF 30%, #F5F9FF 60%, #F5F9FF 85%, #FAFCFF 100%);\n  overflow: hidden;",
    "background: rgba(255,255,255,0.65);\n  backdrop-filter: blur(30px);\n  -webkit-backdrop-filter: blur(30px);\n  overflow: hidden;",
    1)


# ===================================
# D. REWRITE INTERACTIVE JS
# ===================================

# Replace the entire V2 interactive block with cleaner V3
old_js = """// ===== INTERACTIVE BACKGROUND V2 =====
(function(){
  var isTouch='ontouchstart' in window||navigator.maxTouchPoints>0;
  var mx=innerWidth/2,my=innerHeight/2,gx=mx,gy=my;

  // --- Cursor glow with rainbow hue shift ---
  if(!isTouch){
    var glow=document.createElement('div');
    glow.setAttribute('data-cursor-glow','');
    document.body.appendChild(glow);
    var active=false,idle,hue=220;
    document.addEventListener('mousemove',function(e){
      mx=e.clientX;my=e.clientY;
      if(!active){active=true;glow.classList.add('active')}
      clearTimeout(idle);
      idle=setTimeout(function(){active=false;glow.classList.remove('active')},3000);
    },{passive:true});
    (function animate(){
      gx+=(mx-gx)*.08;gy+=(my-gy)*.08;
      hue=(hue+0.15)%360;
      glow.style.left=gx+'px';glow.style.top=gy+'px';
      glow.style.background='radial-gradient(circle,hsla('+Math.round(hue)+',80%,60%,.15) 0%,hsla('+Math.round(hue+60)+',70%,50%,.08) 30%,transparent 70%)';
      requestAnimationFrame(animate);
    })();

    // --- Mouse sparkle trail ---
    var sparklePool=[];
    for(var si=0;si<20;si++){
      var sp=document.createElement('div');
      sp.style.cssText='position:fixed;width:4px;height:4px;border-radius:50%;pointer-events:none;z-index:9999;opacity:0;transition:none;will-change:transform,opacity';
      document.body.appendChild(sp);
      sparklePool.push({el:sp,life:0});
    }
    var sparkleIdx=0,lastSX=0,lastSY=0;
    document.addEventListener('mousemove',function(e){
      var dx=e.clientX-lastSX,dy=e.clientY-lastSY;
      if(dx*dx+dy*dy<400)return;
      lastSX=e.clientX;lastSY=e.clientY;
      var s=sparklePool[sparkleIdx%20];
      sparkleIdx++;
      var sc=['#3B82F6','#8B5CF6','#06B6D4','#10B981','#F59E0B','#EC4899'];
      s.el.style.left=e.clientX+'px';s.el.style.top=e.clientY+'px';
      s.el.style.background=sc[Math.floor(Math.random()*sc.length)];
      s.el.style.opacity='1';s.el.style.transform='translate(-50%,-50%) scale(1)';
      s.el.style.width=(3+Math.random()*4)+'px';s.el.style.height=s.el.style.width;
      s.el.style.transition='opacity .6s ease,transform .6s ease';
      setTimeout(function(){s.el.style.opacity='0';s.el.style.transform='translate(-50%,-50%) scale(0) translateY(-20px)'},16);
    },{passive:true});
  }

  // --- Parallax mesh on scroll ---
  var mesh=document.querySelector('._8bf10');
  if(mesh){
    var ticking=false;
    window.addEventListener('scroll',function(){
      if(!ticking){requestAnimationFrame(function(){mesh.style.transform='translateY('+window.scrollY*.12+'px)';ticking=false});ticking=true}
    },{passive:true});
  }

  // --- Shooting stars (periodic) ---
  function createShootingStar(){
    var star=document.createElement('div');
    star.setAttribute('data-shooting-star','');
    var startX=Math.random()*80+10;
    var dur=0.6+Math.random()*0.8;
    var angle=-15-Math.random()*30;
    var colors=['#3B82F6','#8B5CF6','#06B6D4','#EC4899','#F59E0B'];
    var color=colors[Math.floor(Math.random()*colors.length)];
    star.style.cssText='left:'+startX+'%;top:'+(Math.random()*40)+'%;--star-color:'+color+';--star-angle:'+angle+'deg;animation-duration:'+dur+'s';
    document.body.appendChild(star);
    setTimeout(function(){star.remove()},dur*1000+100);
  }
  setInterval(createShootingStar,2500+Math.random()*2000);
  setTimeout(createShootingStar,1000);

  // --- Floating particles (upgraded) ---
  var pCount=isTouch?10:25;
  var colors=['rgba(37,99,235,.3)','rgba(59,130,246,.25)','rgba(6,182,212,.28)','rgba(124,58,237,.22)','rgba(16,185,129,.25)','rgba(236,72,153,.2)','rgba(245,158,11,.22)'];
  for(var i=0;i<pCount;i++){
    var p=document.createElement('div');
    p.setAttribute('data-particle','');
    var size=(3+Math.random()*6);
    p.style.cssText='left:'+Math.random()*100+'%;top:'+Math.random()*100+'%;width:'+size+'px;height:'+size+'px;background:'+colors[i%colors.length]+';animation-duration:'+(10+Math.random()*20)+'s;animation-delay:'+(-Math.random()*25)+'s;--p-drift:'+(Math.random()*100-50)+'px;--p-dist:'+(-(30+Math.random()*50))+'vh;--p-opacity:'+(0.4+Math.random()*0.4);
    if(i%4===0) p.style.boxShadow='0 0 '+(4+Math.random()*8)+'px '+colors[i%colors.length];
    document.body.appendChild(p);
  }

  // --- Interactive tilt on mouse (blobs react to cursor) ---
  if(!isTouch){
    var blobs=document.querySelectorAll('._70520');
    document.addEventListener('mousemove',function(e){
      var cx=e.clientX/innerWidth-.5;
      var cy=e.clientY/innerHeight-.5;
      blobs.forEach(function(b,i){
        var intensity=10+i*5;
        b.style.transform='translate('+cx*intensity+'px,'+cy*intensity+'px)';
      });
    },{passive:true});
  }

  // --- Click ripple effect ---
  document.addEventListener('click',function(e){
    var ripple=document.createElement('div');
    ripple.setAttribute('data-click-ripple','');
    ripple.style.left=e.clientX+'px';ripple.style.top=e.clientY+'px';
    document.body.appendChild(ripple);
    setTimeout(function(){ripple.remove()},800);
  });
})();"""

new_js = """// ===== FULL-PAGE LIVING BACKGROUND =====
(function(){
  var isTouch='ontouchstart' in window||navigator.maxTouchPoints>0;

  // --- Move gradient mesh to body as fixed full-page background ---
  var mesh=document.querySelector('._8bf10');
  if(mesh){
    document.body.insertBefore(mesh,document.body.firstChild);
    mesh.style.cssText='position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;overflow:visible';
  }

  // --- Smooth cursor glow (desktop only) ---
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
      gx+=(mx-gx)*.06;gy+=(my-gy)*.06;
      glow.style.left=gx+'px';glow.style.top=gy+'px';
      requestAnimationFrame(animate);
    })();
  }

  // --- Blobs follow mouse subtly (desktop) ---
  if(!isTouch&&mesh){
    var blobs=mesh.querySelectorAll('._70520');
    var bx=0,by=0,tmx=0,tmy=0;
    document.addEventListener('mousemove',function(e){
      tmx=(e.clientX/innerWidth-.5);
      tmy=(e.clientY/innerHeight-.5);
    },{passive:true});
    (function blobAnimate(){
      bx+=(tmx-bx)*.02;by+=(tmy-by)*.02;
      blobs.forEach(function(b,i){
        var d=8+i*6;
        b.style.marginLeft=bx*d+'px';
        b.style.marginTop=by*d+'px';
      });
      requestAnimationFrame(blobAnimate);
    })();
  }

  // --- Scroll parallax on blobs ---
  if(mesh){
    var ticking=false;
    window.addEventListener('scroll',function(){
      if(!ticking){requestAnimationFrame(function(){
        var sy=window.scrollY*.04;
        mesh.style.transform='translateY(-'+sy+'px)';
        ticking=false;
      });ticking=true}
    },{passive:true});
  }

  // --- Floating orbs (fewer, bigger, more visible) ---
  var oCount=isTouch?5:10;
  var orbColors=['rgba(37,99,235,.18)','rgba(124,58,237,.15)','rgba(6,182,212,.16)','rgba(236,72,153,.12)','rgba(245,158,11,.14)'];
  for(var i=0;i<oCount;i++){
    var orb=document.createElement('div');
    orb.setAttribute('data-particle','');
    var size=(5+Math.random()*8);
    orb.style.cssText='left:'+Math.random()*100+'%;top:'+Math.random()*100+'%;width:'+size+'px;height:'+size+'px;background:'+orbColors[i%orbColors.length]+';box-shadow:0 0 '+(size*2)+'px '+orbColors[i%orbColors.length]+';animation-duration:'+(15+Math.random()*25)+'s;animation-delay:'+(-Math.random()*30)+'s;--p-drift:'+(Math.random()*60-30)+'px;--p-dist:'+(-(20+Math.random()*30))+'vh;--p-opacity:'+(0.5+Math.random()*0.3);
    document.body.appendChild(orb);
  }
})();"""

content = content.replace(old_js, new_js)

# 15. Simplify cursor glow CSS (no more rainbow, clean blue)
content = content.replace(
    "[data-cursor-glow]{position:fixed;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.18) 0%,rgba(124,58,237,.1) 25%,rgba(6,182,212,.06) 50%,transparent 70%);pointer-events:none;z-index:0;transform:translate(-50%,-50%);opacity:0;transition:opacity .5s ease;will-change:left,top;mix-blend-mode:screen}",
    "[data-cursor-glow]{position:fixed;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.12) 0%,rgba(124,58,237,.06) 35%,transparent 70%);pointer-events:none;z-index:9999;transform:translate(-50%,-50%);opacity:0;transition:opacity .5s ease;will-change:left,top}")

# 16. Replace scroll color shift with one that affects the fixed bg
content = content.replace(
    """// ===== SCROLL COLOR SHIFT V2 =====
(function(){
  var hero=document.querySelector('._1e547');
  if(!hero)return;
  var ticking2=false;
  window.addEventListener('scroll',function(){
    if(!ticking2){requestAnimationFrame(function(){
      var p=Math.min(window.scrollY/2000,1);
      var h1=Math.round(220+p*80);
      var h2=Math.round(240+p*100);
      var s=Math.round(70+p*20);
      hero.style.background='linear-gradient(180deg,#FFFFFF 0%,hsl('+h1+','+s+'%,97%) 25%,hsl('+h2+','+s+'%,96%) 50%,hsl('+h1+','+s+'%,97%) 75%,#FFFFFF 100%)';
      ticking2=false;
    });ticking2=true}
  },{passive:true});
})();""",
    "")  # Remove — scroll now handled in the main block via mesh parallax


# ===================================
# E. ADD FULL-PAGE BG CONTAINER CSS
# ===================================

# Add a subtle animated gradient that sits behind everything
fullpage_bg_css = """/* ===== FULL-PAGE LIVING BACKGROUND ===== */
body{background:linear-gradient(135deg,#f8faff 0%,#f0f4ff 25%,#faf5ff 50%,#f0fffe 75%,#fffbf0 100%);background-size:400% 400%;animation:bg-flow 20s ease infinite}
@keyframes bg-flow{0%{background-position:0% 50%}25%{background-position:100% 0%}50%{background-position:100% 100%}75%{background-position:0% 100%}100%{background-position:0% 50%}}
"""

content = content.replace(
    "/* ========== SECTION: HERO ========== */",
    fullpage_bg_css + "/* ========== SECTION: HERO ========== */")


# ============================================================
# WRITE OUTPUT
# ============================================================
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! {len(content)} chars / {len(content.splitlines())} lines\n")

checks = {
    'No shooting stars': 'shooting-star-move' not in content,
    'No click ripple': 'click-ripple-expand' not in content,
    'No rainbow border': 'rainbow-border' not in content,
    'No breathing overlay': 'bg-breathe' not in content,
    'No perspective grid': 'perspective(500px)' not in content,
    'No sparkle trail': 'sparklePool' not in content,
    'No old scroll shift': 'SCROLL COLOR SHIFT V2' not in content,
    'Modal confetti disabled': 'function cf(){}' in content,
    'Full-page bg CSS': 'bg-flow' in content,
    'Frosted hero': 'rgba(255,255,255,0.55)' in content,
    'Frosted products': 'rgba(255,255,255,0.75)' in content,
    'Frosted trust': 'rgba(255,255,255,0.65)' in content,
    'Mesh moved to body JS': 'document.body.insertBefore(mesh' in content,
    'Blob mouse follow': 'blobAnimate' in content,
    'Blobs vw units': '55vw' in content,
    'Less blur 80px': 'blur(80px)' in content,
    'Cursor glow clean': "z-index:9999;transform:translate(-50%,-50%)" in content,
    'Fewer particles': 'oCount=isTouch?5:10' in content,
    'Glowing orbs': "box-shadow:0 0 '+(size*2)" in content,
}
print("Verification:")
for name, val in checks.items():
    print(f"  {'OK' if val else 'XX'}: {name}")
