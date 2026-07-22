with open("assets/js/main.js", "r", encoding="utf-8") as f:
    js_content = f.read()

if "hamburger" in js_content or "mobile-menu" in js_content:
    print("Found hamburger/mobile-menu handling inside assets/js/main.js")
else:
    print("Not found inside assets/js/main.js")
