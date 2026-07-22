import re

with open("scratch/footer_styles.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Let's extract all CSS rules containing any footer class
# Specifically: .unified-footer-wrapper, .premium-footer-bento, .bento-box, .footer-brand-bento, .pf-mission, .pf-desc, .pf-socials, .pf-social-btn, .footer-links-bento, .pf-nav-col, .pf-nav-header, .pf-link, .footer-contact-bento, .pf-contact-item, .pf-contact-icon, .pf-contact-text, .pf-contact-label, .pf-footer-bottom, .pf-fb-left, .pf-fb-right, .footer-apply-btn, .btn-badge
# Let's find all CSS rules inside <style> tags in footer_styles.txt that correspond to these classes.

rules = []
# Match class names or selectors in CSS
css_blocks = re.findall(r"([^{}]+\{[^{}]*\})", content, re.DOTALL)
for block in css_blocks:
    block_clean = block.strip()
    if any(keyword in block_clean.lower() for keyword in ["footer", "pf-", "bento-box"]):
        # exclude selectors that belong to other sections like matrix-grid or bento-grid in manifesto
        if not any(excl in block_clean.lower() for excl in ["manifesto", "bento-row", "bento-grid", "pedagogy", "curriculum", "method", "mindset", "enquiry"]):
            rules.append(block_clean)

# Also find @media queries that might have footer styling
media_blocks = re.findall(r"(@media[^{}]*\{[^{}]*footer[^{}]*\})", content, re.DOTALL | re.IGNORECASE)
for block in media_blocks:
    rules.append(block.strip())

print(f"Extracted {len(rules)} CSS blocks.")

with open("scratch/clean_footer_css.css", "w", encoding="utf-8") as out:
    out.write("\n\n".join(rules))

print("Saved to scratch/clean_footer_css.css")
