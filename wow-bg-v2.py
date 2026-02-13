import re

filepath = r'C:\Users\User\buyblox-theme\sections\homepage.liquid'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# MEGA WOW BACKGROUND V2 — For 12yo Roblox kids
# ============================================================

# 1. UPGRADE CURSOR GLOW — Bigger, rainbow-shifting, with sparkle trail
# ---------------------------------------------------------------
content = content.replace(
    "[data-cursor-glow]{position:fixed;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.12) 0%,rgba(59,130,246,.06) 30%,transparent 70%);pointer-events:none;z-index:0;transform:translate(-50%,-50%);opacity:0;transition:opacity .4s ease;will-change:left,top}",
    "[data-cursor-glow]{position:fixed;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.18) 0%,rgba(124,58,237,.1) 25%,rgba(6,182,212,.06) 50%,transparent 70%);pointer-events:none;z-index:0;transform:translate(-50%,-50%);opacity:0;transition:opacity .5s ease;will-change:left,top;mix-blend-mode:screen}"
)

# 2. UPGRADE JS PARTICLES — More, bigger, varied shapes, mouse-reactive
# ---------------------------------------------------------------
old_interactive_js = """// ===== INTERACTIVE BACKGROUND =====
(function(){
  var isTouch='ontouchstart' in window||navigator.maxTouchPoints>0;
  if(!isTouch){
    var glow=document.createElement('div');
    glow.setAttribute('data-cursor-glow','');
    document.body.appendChild(glow);
    var mx=0,my=0,gx=0,gy=0,active=false,idle;
    document.addEventListener('mousemove',function(e){
      mx=e.clientX;my=e.clientY;
      if(!active){active=true;glow.classList.add('active')}
      clearTimeout(idle);
      idle=setTimeout(function(){active=false;glow.classList.remove('active')},3000);
    },{passive:true});
    (function animate(){gx+=(mx-gx)*.08;gy+=(my-gy)*.08;glow.style.left=gx+'px';glow.style.top=gy+'px';requestAnimationFrame(animate)})();
  }
  var mesh=document.querySelector('._8bf10');
  if(mesh){
    var ticking=false;
    window.addEventListener('scroll',function(){
      if(!ticking){requestAnimationFrame(function(){mesh.style.transform='translateY('+window.scrollY*.12+'px)';ticking=false});ticking=true}
    },{passive:true});
  }
  var pCount=isTouch?8:15;
  var colors=['rgba(37,99,235,.25)','rgba(59,130,246,.2)','rgba(6,182,212,.22)','rgba(124,58,237,.18)','rgba(16,185,129,.2)'];
  for(var i=0;i<pCount;i++){
    var p=document.createElement('div');
    p.setAttribute('data-particle','');
    var size=(2+Math.random()*5);
    p.style.cssText='left:'+Math.random()*100+'%;top:'+Math.random()*100+'%;width:'+size+'px;height:'+size+'px;background:'+colors[i%colors.length]+';animation-duration:'+(12+Math.random()*25)+'s;animation-delay:'+(-Math.random()*30)+'s;--p-drift:'+(Math.random()*80-40)+'px;--p-dist:'+(-(30+Math.random()*40))+'vh;--p-opacity:'+(0.3+Math.random()*0.4);
    document.body.appendChild(p);
  }
})();"""

new_interactive_js = """// ===== INTERACTIVE BACKGROUND V2 =====
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

content = content.replace(old_interactive_js, new_interactive_js)

# 3. ADD NEW CSS for shooting stars, click ripple, upgraded particles
# ---------------------------------------------------------------
new_css = """/* ===== SHOOTING STARS ===== */
[data-shooting-star]{position:fixed;width:80px;height:2px;background:linear-gradient(90deg,var(--star-color,#3B82F6),transparent);border-radius:2px;pointer-events:none;z-index:9998;opacity:0;animation:shooting-star-move var(--star-dur,.8s) ease-out forwards;filter:drop-shadow(0 0 6px var(--star-color,#3B82F6))}
[data-shooting-star]::before{content:'';position:absolute;right:0;top:-1px;width:4px;height:4px;background:var(--star-color,#3B82F6);border-radius:50%;box-shadow:0 0 8px var(--star-color,#3B82F6),0 0 16px var(--star-color,#3B82F6)}
@keyframes shooting-star-move{0%{transform:rotate(var(--star-angle,-25deg)) translateX(0);opacity:0}10%{opacity:1}100%{transform:rotate(var(--star-angle,-25deg)) translateX(min(60vw,600px));opacity:0}}
/* ===== CLICK RIPPLE ===== */
[data-click-ripple]{position:fixed;width:0;height:0;border-radius:50%;pointer-events:none;z-index:9997;transform:translate(-50%,-50%);border:2px solid rgba(37,99,235,.4);animation:click-ripple-expand .7s ease-out forwards}
@keyframes click-ripple-expand{0%{width:0;height:0;opacity:.8}100%{width:200px;height:200px;opacity:0}}
"""

content = content.replace(
    "[data-cursor-glow].active{opacity:1}",
    "[data-cursor-glow].active{opacity:1}\n" + new_css
)

# 4. UPGRADE GRADIENT MESH — Add 5th blob + rainbow pulse animation
# ---------------------------------------------------------------
# Add a 5th blob (gold/amber) for more color variety
content = content.replace(
    "._70520:nth-child(4){width:800px;height:800px;top:40%;left:40%;background:rgba(236,72,153,.18);opacity:.5;animation-duration:22s;animation-delay:-4s}",
    "._70520:nth-child(4){width:800px;height:800px;top:40%;left:40%;background:rgba(236,72,153,.18);opacity:.5;animation-duration:22s;animation-delay:-4s}\n._70520:nth-child(5){width:700px;height:700px;top:60%;right:10%;background:rgba(245,158,11,.15);opacity:.5;animation-duration:26s;animation-delay:-10s}"
)

# Add 5th blob div in HTML
content = content.replace(
    """  <div class="_8bf10">
    <div class="_70520"></div>
    <div class="_70520"></div>
    <div class="_70520"></div>
    <div class="_70520"></div>
  </div>""",
    """  <div class="_8bf10">
    <div class="_70520"></div>
    <div class="_70520"></div>
    <div class="_70520"></div>
    <div class="_70520"></div>
    <div class="_70520"></div>
  </div>"""
)

# 5. ADD ANIMATED GRADIENT BORDER around the whole hero
# ---------------------------------------------------------------
hero_border_css = """/* ===== ANIMATED HERO GLOW BORDER ===== */
._1e547::after{content:'';position:absolute;bottom:0;left:5%;right:5%;height:2px;background:linear-gradient(90deg,transparent,#3B82F6,#8B5CF6,#06B6D4,#10B981,#F59E0B,#EC4899,#3B82F6,transparent);background-size:200% 100%;animation:rainbow-border 4s linear infinite;z-index:8;filter:blur(1px);opacity:.6}
@keyframes rainbow-border{0%{background-position:0% 0%}100%{background-position:200% 0%}}
"""
content = content.replace(
    "/* ===== BOTTOM FADE ===== */",
    hero_border_css + "/* ===== BOTTOM FADE ===== */"
)

# 6. MAKE GRID MORE VISIBLE + add perspective warp
# ---------------------------------------------------------------
content = content.replace(
    "._8bf10::after{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(37,99,235,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(37,99,235,.06) 1px,transparent 1px);background-size:60px 60px;z-index:2;animation:grid-drift 20s linear infinite}@keyframes grid-drift{0%{background-position:0 0}100%{background-position:60px 60px}}",
    "._8bf10::after{content:'';position:absolute;inset:-20%;width:140%;height:140%;background-image:linear-gradient(rgba(37,99,235,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(37,99,235,.05) 1px,transparent 1px);background-size:50px 50px;z-index:2;animation:grid-drift 15s linear infinite;transform:perspective(500px) rotateX(30deg);transform-origin:50% 0%;mask-image:radial-gradient(ellipse 80% 60% at 50% 40%,black 30%,transparent 70%)}@keyframes grid-drift{0%{background-position:0 0}100%{background-position:50px 50px}}"
)

# 7. UPGRADE SCROLL COLOR SHIFT — more dramatic with aurora effect
# ---------------------------------------------------------------
content = content.replace(
    """// ===== SCROLL COLOR SHIFT =====
(function(){
  var hero=document.querySelector('._1e547');
  if(!hero)return;
  var ticking2=false;
  window.addEventListener('scroll',function(){
    if(!ticking2){requestAnimationFrame(function(){
      var p=Math.min(window.scrollY/3000,1);
      var h=Math.round(220+p*60);
      var s=Math.round(70+p*15);
      hero.style.background='linear-gradient(180deg,#FFFFFF 0%,hsl('+h+','+s+'%,97%) 30%,hsl('+h+','+s+'%,96%) 50%,hsl('+h+','+s+'%,97%) 70%,#FFFFFF 100%)';
      ticking2=false;
    });ticking2=true}
  },{passive:true});
})();""",
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
})();"""
)

# ============================================================
# WRITE OUTPUT
# ============================================================
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! {len(content)} chars / {len(content.splitlines())} lines\n")

checks = {
    'Rainbow cursor glow': 'mix-blend-mode:screen' in content,
    'Mouse sparkle trail': 'sparklePool' in content,
    'Shooting stars CSS': 'shooting-star-move' in content,
    'Shooting stars JS': 'createShootingStar' in content,
    'Click ripple CSS': 'click-ripple-expand' in content,
    'Click ripple JS': 'data-click-ripple' in content,
    '5th gradient blob CSS': 'nth-child(5)' in content,
    '5th gradient blob HTML': content.count('<div class="_70520"></div>') == 5,
    'Blob mouse reactivity': 'blobs.forEach' in content,
    'Rainbow hero border': 'rainbow-border' in content,
    'Perspective grid': 'perspective(500px)' in content,
    'Upgraded scroll shift': 'SCROLL COLOR SHIFT V2' in content,
    'More particles (25)': 'pCount=isTouch?10:25' in content,
    'Glowing particles': 'boxShadow' in content,
    'No old interactive block': 'pCount=isTouch?8:15' not in content,
}
print("Verification:")
for name, val in checks.items():
    print(f"  {'OK' if val else 'XX'}: {name}")
