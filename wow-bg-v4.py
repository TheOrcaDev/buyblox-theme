import re

filepath = r'C:\Users\User\buyblox-theme\sections\homepage.liquid'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# V4: FULL-PAGE LIVING BACKGROUND — NO LAG EDITION
#
# Problem with V3: backdrop-filter:blur() on every section =
# GPU murder. And blobs were invisible behind opaque sections.
#
# New approach:
# - Hero: keeps its full blob mesh (already works great)
# - Every OTHER section: gets animated gradient color overlays
#   via ::before pseudo-elements (pure CSS, zero JS, no blur)
# - Body: subtle flowing gradient as base
# - Remove ALL backdrop-filter
# - Fewer, cleaner JS effects
# ============================================================

# ====================
# A. REVERT SECTION BACKGROUNDS (remove backdrop-filter, restore solid bg)
# ====================

# Hero — back to gradient, no backdrop-filter
content = content.replace(
    "._1e547{position:relative;width:100vw;left:50%;margin-left:-50vw;padding:0;background:rgba(255,255,255,0.55);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);overflow:hidden;min-height:80vh}",
    "._1e547{position:relative;width:100vw;left:50%;margin-left:-50vw;padding:0;background:linear-gradient(180deg,#FFFFFF 0%,#FAFCFF 30%,#F5F9FF 50%,#FAFCFF 70%,#FFFFFF 100%);overflow:hidden;min-height:80vh}")

# Products — back to solid
content = content.replace(
    "background:rgba(255,255,255,0.75);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);overflow:hidden;margin-top:-1px",
    "background:#FFFFFF;overflow:hidden;margin-top:-1px")

# How It Works — back to solid
content = content.replace(
    "background:rgba(255,255,255,0.7);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);overflow:hidden",
    "background:#FFFFFF;overflow:hidden",
    1)

# Trust — back to solid (multi-line format)
content = content.replace(
    "background: rgba(255,255,255,0.65);\n  backdrop-filter: blur(30px);\n  -webkit-backdrop-filter: blur(30px);\n  overflow: hidden;",
    "background: #FFFFFF;\n  overflow: hidden;",
    1)

# FAQ — back to solid (multi-line format, second occurrence)
content = content.replace(
    "background: rgba(255,255,255,0.65);\n  backdrop-filter: blur(30px);\n  -webkit-backdrop-filter: blur(30px);\n  overflow: hidden;",
    "background: #FFFFFF;\n  overflow: hidden;",
    1)

# ====================
# B. REMOVE BODY ANIMATED GRADIENT (unnecessary layer)
# ====================
content = content.replace(
    """/* ===== FULL-PAGE LIVING BACKGROUND ===== */
body{background:linear-gradient(135deg,#f8faff 0%,#f0f4ff 25%,#faf5ff 50%,#f0fffe 75%,#fffbf0 100%);background-size:400% 400%;animation:bg-flow 20s ease infinite}
@keyframes bg-flow{0%{background-position:0% 50%}25%{background-position:100% 0%}50%{background-position:100% 100%}75%{background-position:0% 100%}100%{background-position:0% 50%}}
""",
    "")

# ====================
# C. RESTORE MESH INSIDE HERO (add overflow:hidden back)
# ====================
content = content.replace(
    "._8bf10{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:1}",
    "._8bf10{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:1;overflow:hidden}")

# Revert blobs from vw to fixed sizes (vw was for full-page, now they're hero-only again)
content = content.replace(
    "._70520:nth-child(1){width:55vw;height:55vw;min-width:500px;min-height:500px;top:-10%;left:-15%;background:rgba(37,99,235,.22);opacity:.8;animation-duration:20s}",
    "._70520:nth-child(1){width:900px;height:900px;top:-20%;left:-15%;background:rgba(37,99,235,.25);opacity:.8;animation-duration:20s}")
content = content.replace(
    "._70520:nth-child(2){width:45vw;height:45vw;min-width:400px;min-height:400px;top:15%;right:-10%;background:rgba(124,58,237,.2);opacity:.7;animation-duration:28s;animation-delay:-7s}",
    "._70520:nth-child(2){width:800px;height:800px;top:10%;right:-15%;background:rgba(124,58,237,.2);opacity:.7;animation-duration:28s;animation-delay:-7s}")
content = content.replace(
    "._70520:nth-child(3){width:50vw;height:50vw;min-width:450px;min-height:450px;top:40%;left:-5%;background:rgba(6,182,212,.18);opacity:.7;animation-duration:32s;animation-delay:-14s}",
    "._70520:nth-child(3){width:1000px;height:1000px;bottom:-25%;left:5%;background:rgba(6,182,212,.18);opacity:.65;animation-duration:32s;animation-delay:-14s}")
content = content.replace(
    "._70520:nth-child(4){width:40vw;height:40vw;min-width:350px;min-height:350px;top:60%;right:5%;background:rgba(236,72,153,.15);opacity:.6;animation-duration:24s;animation-delay:-4s}",
    "._70520:nth-child(4){width:700px;height:700px;top:45%;left:40%;background:rgba(236,72,153,.15);opacity:.5;animation-duration:24s;animation-delay:-4s}")
content = content.replace(
    "._70520:nth-child(5){width:35vw;height:35vw;min-width:300px;min-height:300px;top:80%;left:20%;background:rgba(245,158,11,.12);opacity:.5;animation-duration:26s;animation-delay:-10s}",
    "._70520:nth-child(5){width:600px;height:600px;top:60%;right:10%;background:rgba(245,158,11,.1);opacity:.4;animation-duration:26s;animation-delay:-10s}")


# ====================
# D. ADD ANIMATED COLOR OVERLAYS TO EVERY SECTION
#    Pure CSS — radial-gradient + animated position = living color
#    Zero performance cost (just GPU compositing, no blur)
# ====================

section_overlays = """/* ===== SECTION COLOR OVERLAYS (living background per section) ===== */
._99e1a::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;opacity:.6;
background:radial-gradient(ellipse 60% 50% at 10% 40%,rgba(37,99,235,.08),transparent 70%),radial-gradient(ellipse 50% 60% at 90% 60%,rgba(124,58,237,.06),transparent 70%),radial-gradient(ellipse 40% 40% at 50% 20%,rgba(6,182,212,.05),transparent 60%);
background-size:200% 200%;animation:glow-a 18s ease-in-out infinite alternate}
._fc821::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;opacity:.6;
background:radial-gradient(ellipse 55% 45% at 85% 30%,rgba(6,182,212,.08),transparent 70%),radial-gradient(ellipse 50% 50% at 15% 70%,rgba(16,185,129,.06),transparent 70%),radial-gradient(ellipse 45% 55% at 50% 50%,rgba(37,99,235,.04),transparent 60%);
background-size:200% 200%;animation:glow-b 20s ease-in-out infinite alternate}
._24fcc::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;opacity:.6;
background:radial-gradient(ellipse 50% 50% at 20% 50%,rgba(124,58,237,.07),transparent 70%),radial-gradient(ellipse 55% 45% at 80% 40%,rgba(236,72,153,.06),transparent 70%),radial-gradient(ellipse 40% 40% at 50% 80%,rgba(37,99,235,.05),transparent 60%);
background-size:200% 200%;animation:glow-c 16s ease-in-out infinite alternate}
._acc57::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;opacity:.6;
background:radial-gradient(ellipse 55% 50% at 75% 30%,rgba(37,99,235,.07),transparent 70%),radial-gradient(ellipse 45% 55% at 25% 70%,rgba(245,158,11,.05),transparent 70%),radial-gradient(ellipse 50% 40% at 50% 50%,rgba(124,58,237,.04),transparent 60%);
background-size:200% 200%;animation:glow-a 22s ease-in-out infinite alternate}
@keyframes glow-a{0%{background-position:0% 0%}100%{background-position:100% 100%}}
@keyframes glow-b{0%{background-position:100% 0%}100%{background-position:0% 100%}}
@keyframes glow-c{0%{background-position:50% 0%}100%{background-position:50% 100%}}
"""

# Insert before hero section comment
content = content.replace(
    "/* ========== SECTION: HERO ========== */",
    section_overlays + "/* ========== SECTION: HERO ========== */")


# ====================
# E. REWRITE JS — Remove mesh-move, clean up
# ====================

old_js = """// ===== FULL-PAGE LIVING BACKGROUND =====
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

new_js = """// ===== INTERACTIVE BACKGROUND =====
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
      if(!ticking){requestAnimationFrame(function(){mesh.style.transform='translateY('+window.scrollY*.1+'px)';ticking=false});ticking=true}
    },{passive:true});
  }

  // --- Floating orbs across page ---
  var oCount=isTouch?5:10;
  var orbColors=['rgba(37,99,235,.15)','rgba(124,58,237,.12)','rgba(6,182,212,.14)','rgba(236,72,153,.1)','rgba(245,158,11,.11)'];
  for(var i=0;i<oCount;i++){
    var orb=document.createElement('div');
    orb.setAttribute('data-particle','');
    var size=(4+Math.random()*6);
    orb.style.cssText='left:'+Math.random()*100+'%;top:'+Math.random()*100+'%;width:'+size+'px;height:'+size+'px;background:'+orbColors[i%orbColors.length]+';box-shadow:0 0 '+(size*1.5)+'px '+orbColors[i%orbColors.length]+';animation-duration:'+(15+Math.random()*25)+'s;animation-delay:'+(-Math.random()*30)+'s;--p-drift:'+(Math.random()*60-30)+'px;--p-dist:'+(-(20+Math.random()*30))+'vh;--p-opacity:'+(0.4+Math.random()*0.3);
    document.body.appendChild(orb);
  }
})();"""

content = content.replace(old_js, new_js)


# ====================
# F. CLEAN UP CURSOR GLOW CSS
# ====================
content = content.replace(
    "[data-cursor-glow]{position:fixed;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.12) 0%,rgba(124,58,237,.06) 35%,transparent 70%);pointer-events:none;z-index:9999;transform:translate(-50%,-50%);opacity:0;transition:opacity .5s ease;will-change:left,top}",
    "[data-cursor-glow]{position:fixed;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.1) 0%,rgba(124,58,237,.05) 35%,transparent 70%);pointer-events:none;z-index:9999;transform:translate(-50%,-50%);opacity:0;transition:opacity .4s ease;will-change:left,top}")


# ============================================================
# WRITE OUTPUT
# ============================================================
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! {len(content)} chars / {len(content.splitlines())} lines\n")

checks = {
    'No backdrop-filter': 'backdrop-filter' not in content,
    'No bg-flow': 'bg-flow' not in content,
    'No mesh body move': 'body.insertBefore' not in content,
    'No blob mouse-follow': 'blobAnimate' not in content,
    'Hero solid bg': '#FAFCFF 30%,#F5F9FF 50%' in content,
    'Products solid bg': "background:#FFFFFF;overflow:hidden;margin-top:-1px" in content,
    'Mesh overflow hidden': 'z-index:1;overflow:hidden' in content,
    'Products overlay': '._99e1a::before{content' in content,
    'HowItWorks overlay': '._fc821::before{content' in content,
    'Trust overlay': '._24fcc::before{content' in content,
    'FAQ overlay': '._acc57::before{content' in content,
    'Glow animations': 'glow-a' in content and 'glow-b' in content and 'glow-c' in content,
    'Cursor glow 400px': 'width:400px;height:400px' in content,
    'Floating orbs': 'oCount=isTouch?5:10' in content,
    'Scroll parallax': "mesh.style.transform='translateY('" in content,
    'Hero blobs 900px': 'width:900px;height:900px' in content,
    'Modal confetti disabled': 'function cf(){}' in content,
}
print("Verification:")
for name, val in checks.items():
    print(f"  {'OK' if val else 'XX'}: {name}")
