with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for the style block that starts with or contains "PREMIUM BENTO FOOTER STYLES" or "Unified Premium Footer"
# Since style blocks are defined with <style> ... </style>, let's find all <style> tags and check if they contain footer styling.

import re
style_tags = re.findall(r"<style.*?>.*?</style>", content, re.DOTALL | re.IGNORECASE)

clean_footer_styles = ""
for tag in style_tags:
    if "PREMIUM BENTO FOOTER STYLES" in tag or "unified-footer-wrapper" in tag:
        # Strip the <style> and </style> tags themselves so we just get raw CSS
        raw_css = re.sub(r"</?style[^>]*>", "", tag, flags=re.IGNORECASE).strip()
        clean_footer_styles += raw_css + "\n\n"

print("Length of extracted raw CSS:", len(clean_footer_styles))

with open("scratch/clean_footer_css.css", "w", encoding="utf-8") as out:
    out.write(clean_footer_styles)

print("Saved to scratch/clean_footer_css.css")
