import re

filepath = r'C:\Users\User\buyblox-theme\sections\homepage.liquid'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# 1. FIX ALL SPACING — Tighten everything, remove dead space
# ============================================================

# --- Wave dividers: reduce height from 80px to 40px ---
content = content.replace(
    "._69f80 {\n  position: absolute;\n  bottom: 0;\n  left: 0;\n  width: 100%;\n  height: 80px;",
    "._69f80 {\n  position: absolute;\n  bottom: 0;\n  left: 0;\n  width: 100%;\n  height: 40px;")
content = content.replace(
    "._e5551 {\n  position: absolute;\n  bottom: 0;\n  left: 0;\n  width: 100%;\n  height: 80px;",
    "._e5551 {\n  position: absolute;\n  bottom: 0;\n  left: 0;\n  width: 100%;\n  height: 40px;")

# --- Internal margins: reduce all section-level margins ---
# Trust section margin-bottom (40-60px → 20-30px)
content = content.replace("margin-bottom: clamp(40px, 6vw, 60px);",
                          "margin-bottom: clamp(16px, 3vw, 28px);")
# Trust/FAQ header margins (28-40px → 16-24px)
content = content.replace("margin-bottom: clamp(28px, 4vw, 40px);",
                          "margin-bottom: clamp(14px, 2vw, 24px);")
# Featured products header (32-48px → 16-28px)
content = content.replace("margin-bottom:clamp(32px,5vw,48px)}",
                          "margin-bottom:clamp(14px,2.5vw,24px)}")
# FAQ header (32-48px → 16-28px, spaced version)
content = content.replace("margin-bottom: clamp(32px, 5vw, 48px);",
                          "margin-bottom: clamp(14px, 2.5vw, 24px);")
# Tabs margin (40px → 20px)
content = content.replace("._c8907{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-bottom:40px}",
                          "._c8907{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-bottom:20px}")
# Help center box margin (60px → 24px)
content = content.replace("margin: 0 0 60px;\n}", "margin: 0 0 24px;\n}")
# Hero CTA wrapper margin (40px → 24px)
content = content.replace("._79a7b{position:relative;display:inline-block;margin-bottom:40px}",
                          "._79a7b{position:relative;display:inline-block;margin-bottom:24px}")

# --- Mobile spacing fixes ---
# Hero mobile bottom padding (80-120px is WAY too much → 30-50px)
content = content.replace(
    "._d389b{padding:clamp(12px,2.5vw,24px) 16px clamp(80px,12vw,120px)}",
    "._d389b{padding:clamp(12px,2.5vw,24px) 16px clamp(24px,4vw,40px)}")
# Mobile trust badge margin (60px → 20px)
content = content.replace(
    "._a5a29{font-size:13px;padding:18px 20px;margin-bottom:60px;",
    "._a5a29{font-size:13px;padding:18px 20px;margin-bottom:20px;")
# Mobile CTA wrapper margin (60px → 24px)
content = content.replace(
    "._79a7b{margin:0 0 60px;",
    "._79a7b{margin:0 0 24px;")

# ============================================================
# 2. WOW BACKGROUND — Bigger blobs, scroll color shift, animated grid
# ============================================================

# --- Make gradient blobs bigger and brighter ---
# Blob 1: blue - bigger and more visible
content = content.replace(
    "._70520:nth-child(1){width:800px;height:800px;top:-20%;left:-15%;background:rgba(37,99,235,.2);opacity:.7;animation-duration:20s}",
    "._70520:nth-child(1){width:1000px;height:1000px;top:-25%;left:-15%;background:rgba(37,99,235,.3);opacity:.8;animation-duration:18s}")
# Blob 2: purple - bigger
content = content.replace(
    "._70520:nth-child(2){width:700px;height:700px;top:15%;right:-20%;background:rgba(124,58,237,.15);opacity:.6;animation-duration:28s;animation-delay:-7s}",
    "._70520:nth-child(2){width:900px;height:900px;top:10%;right:-20%;background:rgba(124,58,237,.25);opacity:.7;animation-duration:25s;animation-delay:-7s}")
# Blob 3: cyan - bigger
content = content.replace(
    "._70520:nth-child(3){width:900px;height:900px;bottom:-30%;left:10%;background:rgba(6,182,212,.12);opacity:.5;animation-duration:32s;animation-delay:-14s}",
    "._70520:nth-child(3){width:1100px;height:1100px;bottom:-25%;left:5%;background:rgba(6,182,212,.2);opacity:.6;animation-duration:30s;animation-delay:-14s}")
# Blob 4: pink - bigger
content = content.replace(
    "._70520:nth-child(4){width:600px;height:600px;top:45%;left:45%;background:rgba(236,72,153,.1);opacity:.4;animation-duration:24s;animation-delay:-4s}",
    "._70520:nth-child(4){width:800px;height:800px;top:40%;left:40%;background:rgba(236,72,153,.18);opacity:.5;animation-duration:22s;animation-delay:-4s}")

# --- Replace static dot grid with animated perspective grid ---
content = content.replace(
    "._8bf10::after{content:'';position:absolute;inset:0;background-image:radial-gradient(circle at 1px 1px,rgba(37,99,235,.04) 1px,transparent 0);background-size:32px 32px;z-index:2}",
    "._8bf10::after{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(37,99,235,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(37,99,235,.06) 1px,transparent 1px);background-size:60px 60px;z-index:2;animation:grid-drift 20s linear infinite}@keyframes grid-drift{0%{background-position:0 0}100%{background-position:60px 60px}}")

# --- Add extra CSS for scroll color shift + noise ---
wow_css = """/* ===== WOW BACKGROUND ENHANCEMENTS ===== */
._1e547::before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,transparent 0%,rgba(124,58,237,.04) 25%,rgba(6,182,212,.06) 50%,rgba(37,99,235,.04) 75%,transparent 100%);z-index:0;pointer-events:none;opacity:0;animation:bg-breathe 8s ease-in-out infinite}
@keyframes bg-breathe{0%,100%{opacity:0}50%{opacity:1}}
._8bf10{transition:filter .3s ease}
"""
content = content.replace("/* ===== PREMIUM GRADIENT MESH ===== */",
                          wow_css + "/* ===== PREMIUM GRADIENT MESH ===== */")

# --- Add scroll-reactive color shift JS ---
scroll_color_js = """
// ===== SCROLL COLOR SHIFT =====
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
})();
"""
content = content.replace("// ===== INTERACTIVE BACKGROUND =====",
                          scroll_color_js + "\n// ===== INTERACTIVE BACKGROUND =====")

# ============================================================
# 3. REPLACE CANDY CANE STRIPES → Glass shine sweep
# ============================================================

# Hero CTA button (._ab1bb::before)
content = content.replace(
    "._ab1bb::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:repeating-linear-gradient(45deg,transparent,transparent 10px,rgba(255,255,255,.1) 10px,rgba(255,255,255,.1) 20px);border-radius:16px;pointer-events:none}",
    "._ab1bb::before{content:'';position:absolute;top:0;left:-100%;width:200%;height:100%;background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,.25) 45%,rgba(255,255,255,.35) 50%,rgba(255,255,255,.25) 55%,transparent 60%);border-radius:16px;pointer-events:none;transition:left .7s cubic-bezier(.16,1,.3,1)}._ab1bb:hover::before{left:100%}")

# Add to Cart button (._b211c::before)
content = content.replace(
    "._b211c::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:repeating-linear-gradient(45deg,transparent,transparent 8px,rgba(255,255,255,.1) 8px,rgba(255,255,255,.1) 16px);border-radius:12px;pointer-events:none}",
    "._b211c::before{content:'';position:absolute;top:0;left:-100%;width:200%;height:100%;background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,.2) 45%,rgba(255,255,255,.3) 50%,rgba(255,255,255,.2) 55%,transparent 60%);border-radius:12px;pointer-events:none;transition:left .5s cubic-bezier(.16,1,.3,1)}._b211c:hover::before{left:100%}")

# View All button (._60954::before)
content = content.replace(
    "._60954::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:repeating-linear-gradient(45deg,transparent,transparent 10px,rgba(255,255,255,.1) 10px,rgba(255,255,255,.1) 20px);border-radius:16px;pointer-events:none}",
    "._60954::before{content:'';position:absolute;top:0;left:-100%;width:200%;height:100%;background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,.25) 45%,rgba(255,255,255,.35) 50%,rgba(255,255,255,.25) 55%,transparent 60%);border-radius:16px;pointer-events:none;transition:left .7s cubic-bezier(.16,1,.3,1)}._60954:hover::before{left:100%}")

# View Tutorial button (._d310a::before)
content = content.replace(
    "._d310a::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:repeating-linear-gradient(45deg,transparent,transparent 8px,rgba(255,255,255,.15) 8px,rgba(255,255,255,.15) 16px);border-radius:12px;pointer-events:none}",
    "._d310a::before{content:'';position:absolute;top:0;left:-100%;width:200%;height:100%;background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,.2) 45%,rgba(255,255,255,.3) 50%,rgba(255,255,255,.2) 55%,transparent 60%);border-radius:12px;pointer-events:none;transition:left .5s cubic-bezier(.16,1,.3,1)}._d310a:hover::before{left:100%}")

# ============================================================
# WRITE OUTPUT
# ============================================================
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! {len(content)} chars / {len(content.splitlines())} lines\n")

checks = {
    'Wave height 40px': 'height: 40px;' in content and 'height: 80px;' not in content,
    'Trust margin reduced': 'margin-bottom: clamp(16px, 3vw, 28px);' in content,
    'Tabs margin 20px': 'margin-bottom:20px}' in content,
    'Help center 24px': "margin: 0 0 24px;\n}" in content,
    'Mobile hero fixed': 'clamp(24px,4vw,40px)}' in content,
    'Bigger blob 1': 'width:1000px;height:1000px' in content,
    'Brighter blob opacity': 'opacity:.8;animation-duration:18s' in content,
    'Animated grid': 'grid-drift' in content,
    'BG breathe': 'bg-breathe' in content,
    'Scroll color shift': 'SCROLL COLOR SHIFT' in content,
    'Glass shine CTA': "._ab1bb::before{content:'';position:absolute;top:0;left:-100%" in content,
    'Glass shine cart': "._b211c::before{content:'';position:absolute;top:0;left:-100%" in content,
    'Glass shine view': "._60954::before{content:'';position:absolute;top:0;left:-100%" in content,
    'Glass shine tutorial': "._d310a::before{content:'';position:absolute;top:0;left:-100%" in content,
    'No candy cane': 'repeating-linear-gradient(45deg' not in content,
}
print("Verification:")
for name, val in checks.items():
    print(f"  {'OK' if val else 'XX'}: {name}")
