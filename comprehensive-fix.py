import re

filepath = r'C:\Users\User\buyblox-theme\sections\homepage.liquid'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# COMPREHENSIVE FIX — Background, Colors, Gaps, Everything
# ============================================================
#
# APPROACH: Animated body gradient (vivid colors) + semi-transparent
# section backgrounds (NO backdrop-filter). The body gradient is
# visible through ALL sections, creating one continuous living bg.
# No blur operations = no lag.
#
# Also fixing: gaps, mobile spacing, bottom fade, wave fills,
# and any remaining visual issues.
# ============================================================


# ====================
# 1. BODY GRADIENT — Use vivid 300-level colors
# ====================
content = content.replace(
    "body{background:linear-gradient(135deg,#DBEAFE 0%,#EDE9FE 16%,#CFFAFE 33%,#D1FAE5 50%,#FEF3C7 66%,#FCE7F3 83%,#DBEAFE 100%);background-size:500% 500%;animation:body-glow 20s ease infinite}",
    "body{background:linear-gradient(135deg,#93C5FD 0%,#C4B5FD 17%,#67E8F9 33%,#6EE7B7 50%,#FCD34D 67%,#F9A8D4 83%,#93C5FD 100%);background-size:600% 600%;animation:body-glow 25s ease infinite}")


# ====================
# 2. SECTION BACKGROUNDS — Semi-transparent white (NO blur!)
# ====================

# Hero — most transparent (blobs add their own visual depth)
content = content.replace(
    "._1e547{position:relative;width:100vw;left:50%;margin-left:-50vw;padding:0;background:linear-gradient(180deg,#FFFFFF 0%,#FAFCFF 30%,#F5F9FF 50%,#FAFCFF 70%,#FFFFFF 100%);overflow:hidden;min-height:80vh}",
    "._1e547{position:relative;width:100vw;left:50%;margin-left:-50vw;padding:0;background:rgba(255,255,255,0.65);overflow:hidden;min-height:80vh}")

# Products
content = content.replace(
    "background:#FFFFFF;overflow:hidden;margin-top:-1px",
    "background:rgba(255,255,255,0.8);overflow:hidden;margin-top:-1px")

# How It Works (minified, single-line)
content = content.replace(
    "._fc821{--text:#111;--bg:#FFF;--highlight:#FF6D00;--orange:#FF6D00;--light-gray:#F5F5F5;box-sizing:border-box;position:relative;width:100vw;left:50%;margin-left:-50vw;padding:0;background:#FFFFFF;overflow:hidden}",
    "._fc821{--text:#111;--bg:#FFF;--highlight:#FF6D00;--orange:#FF6D00;--light-gray:#F5F5F5;box-sizing:border-box;position:relative;width:100vw;left:50%;margin-left:-50vw;padding:0;background:rgba(255,255,255,0.78);overflow:hidden}")

# Trust (multi-line format)
content = content.replace(
    "  background: #FFFFFF;\n  overflow: hidden;\n}",
    "  background: rgba(255,255,255,0.8);\n  overflow: hidden;\n}",
    1)  # First occurrence = Trust

# FAQ (multi-line format)
content = content.replace(
    "  background: #FFFFFF;\n  overflow: hidden;\n}",
    "  background: rgba(255,255,255,0.8);\n  overflow: hidden;\n}",
    1)  # Second occurrence = FAQ


# ====================
# 3. HERO BOTTOM FADE — Fade to semi-transparent, not solid white
# ====================
content = content.replace(
    "._0ac44{position:absolute;bottom:0;left:0;width:100%;height:200px;background:linear-gradient(180deg,transparent 0%,#FFFFFF 100%);pointer-events:none;z-index:7}",
    "._0ac44{position:absolute;bottom:0;left:0;width:100%;height:150px;background:linear-gradient(180deg,transparent 0%,rgba(255,255,255,0.8) 100%);pointer-events:none;z-index:7}")


# ====================
# 4. WAVE DIVIDER FILLS — Match semi-transparent sections
# ====================
# Trust bottom wave: #FDFDFD → transparent fill (let body gradient show)
content = content.replace(
    'fill="#FDFDFD"',
    'fill="rgba(255,255,255,0.8)"')

# Products top wave SVG — find it in HTML
# The _025ac is a decorative wave at the top of products section
# _9fecd is the how-it-works bottom wave


# ====================
# 5. FIX FEATURED PRODUCTS MOBILE TOP PADDING
#    Currently 70-100px on mobile which creates a HUGE gap
# ====================
content = content.replace(
    "._364cd{padding:clamp(70px,12vw,100px) clamp(16px,4vw,24px) clamp(20px,4vw,40px)}",
    "._364cd{padding:clamp(30px,5vw,40px) clamp(16px,4vw,24px) clamp(20px,4vw,40px)}")


# ====================
# 6. FIX FAQ MOBILE BOTTOM PADDING — 50-80px is too much
# ====================
content = content.replace(
    "padding: clamp(30px, 5vw, 50px) clamp(20px, 4vw, 24px) clamp(50px, 10vw, 80px)",
    "padding: clamp(20px, 3vw, 30px) clamp(20px, 4vw, 24px) clamp(24px, 4vw, 40px)")


# ====================
# 7. PRODUCT CARDS — Make slightly transparent so body bg peeks through
# ====================
# Card background #FFF → very slight transparency for depth
content = content.replace(
    "._113e9{padding:16px;position:relative;z-index:2;background:#FFF;border-radius:0 0 15px 15px}",
    "._113e9{padding:16px;position:relative;z-index:2;background:rgba(255,255,255,0.95);border-radius:0 0 15px 15px}")

# Step cards
content = content.replace(
    "._1ef0d{position:relative;background:#FFF;border:4px solid #FAFAFA;",
    "._1ef0d{position:relative;background:rgba(255,255,255,0.92);border:4px solid rgba(255,255,255,0.7);")

# Tutorial cards
content = content.replace(
    "._605d9{background:#FFF;border:3px solid #FAFAFA;",
    "._605d9{background:rgba(255,255,255,0.92);border:3px solid rgba(255,255,255,0.7);")

# Trust feature cards
content = content.replace(
    "._1264f {\n  background: linear-gradient(135deg, #FFFFFF 0%, #FDFDFD 100%);\n  border: 3px solid #E5E7EB;",
    "._1264f {\n  background: rgba(255,255,255,0.9);\n  border: 3px solid rgba(229,231,235,0.8);")


# ====================
# 8. CREATOR CAROUSEL — Match transparency
# ====================
content = content.replace(
    "._fda51{flex:0 0 auto;display:flex;flex-direction:column;align-items:center;gap:10px;padding:16px 14px;background:linear-gradient(135deg,#FFF 0%,#FDFDFD 100%);border:3px solid #E5E7EB;",
    "._fda51{flex:0 0 auto;display:flex;flex-direction:column;align-items:center;gap:10px;padding:16px 14px;background:rgba(255,255,255,0.9);border:3px solid rgba(229,231,235,0.8);")


# ====================
# 9. HERO MESH BLOBS — Reduce blur for more visible shapes
# ====================
content = content.replace(
    "._70520{position:absolute;border-radius:50%;filter:blur(80px);animation:mesh-float ease-in-out infinite;will-change:transform}",
    "._70520{position:absolute;border-radius:50%;filter:blur(60px);animation:mesh-float ease-in-out infinite;will-change:transform}")


# ====================
# 10. MOBILE MESH VISIBILITY — Currently opacity 0.2 on mobile, too faint
# ====================
content = content.replace(
    "._8bf10{opacity:0.2}",
    "._8bf10{opacity:0.5}")


# ====================
# 11. FAQ SECTION — Remove excessive inner margins
# ====================
# FAQ accordion items margin — check if there's excessive spacing
# Also fix the trust section mobile margin
content = content.replace(
    "margin: 0 0 40px;",
    "margin: 0 0 20px;")


# ====================
# 12. INTERNAL CONTENT WRAPPER SPACING — Ensure consistency
# ====================
# Trust content wrapper padding on desktop is very tight (10-20px top)
# This is fine — the trust section doesn't need huge top padding
# since the wave from the section above provides visual transition

# How It Works top padding is very tight (5-10px) — bump it slightly
content = content.replace(
    "._68c40{max-width:1280px;margin:0 auto;padding:clamp(5px,1vw,10px) clamp(20px,4vw,40px) clamp(12px,2vw,20px);position:relative;z-index:2}",
    "._68c40{max-width:1280px;margin:0 auto;padding:clamp(16px,2vw,24px) clamp(20px,4vw,40px) clamp(12px,2vw,20px);position:relative;z-index:2}")


# ====================
# 13. GREEN BORDER REMNANT — Fix spring theme leftover
# ====================
# There's a green border on mobile trust grid that shouldn't be there
content = content.replace(
    "border: 2px solid rgba(200, 230, 201, 0.5);",
    "border: 2px solid rgba(229, 231, 235, 0.5);")


# ====================
# 14. MODAL BACKGROUND — Slightly transparent for consistency
# ====================
content = content.replace(
    "._73a03{position:relative;background:linear-gradient(180deg,#FFFFFF 0%,#FDFDFD 100%);",
    "._73a03{position:relative;background:rgba(255,255,255,0.97);")


# ============================================================
# WRITE OUTPUT
# ============================================================
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! {len(content)} chars / {len(content.splitlines())} lines\n")

checks = {
    'Body gradient vivid': '#93C5FD 0%' in content,
    'Body gradient animated': 'body-glow 25s' in content,
    'Hero semi-transparent': 'rgba(255,255,255,0.65);overflow:hidden;min-height:80vh' in content,
    'Products semi-transparent': 'rgba(255,255,255,0.8);overflow:hidden;margin-top:-1px' in content,
    'HowItWorks semi-transparent': 'rgba(255,255,255,0.78);overflow:hidden' in content,
    'Trust semi-transparent': 'rgba(255,255,255,0.8);\n  overflow: hidden;\n}' in content,
    'No backdrop-filter on sections': 'backdrop-filter:blur(30px)' not in content and 'backdrop-filter:blur(40px)' not in content,
    'Bottom fade 150px': 'height:150px' in content,
    'Bottom fade rgba': 'rgba(255,255,255,0.8) 100%)' in content,
    'Wave fill rgba': 'fill="rgba(255,255,255,0.8)"' in content,
    'Products mobile padding fixed': 'clamp(30px,5vw,40px) clamp(16px' in content,
    'FAQ mobile padding fixed': 'clamp(24px, 4vw, 40px)' in content,
    'Cards semi-transparent': 'rgba(255,255,255,0.92)' in content,
    'Blobs less blur': 'blur(60px)' in content,
    'Mobile mesh 0.5': 'opacity:0.5' in content,
    'Green border fixed': 'rgba(229, 231, 235, 0.5)' in content,
    'HowItWorks top padding': 'clamp(16px,2vw,24px) clamp(20px,4vw,40px)' in content,
}
print("Verification:")
for name, val in checks.items():
    print(f"  {'OK' if val else 'XX'}: {name}")
