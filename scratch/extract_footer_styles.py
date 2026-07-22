import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for all style tags
styles = re.findall(r"<style.*?>.*?</style>", content, re.DOTALL | re.IGNORECASE)
footer_styles = []

for s in styles:
    if "footer" in s.lower() or "pf-footer" in s.lower() or "unified-footer" in s.lower():
        footer_styles.append(s)

print(f"Found {len(footer_styles)} style blocks matching footer.")

with open("scratch/footer_styles.txt", "w", encoding="utf-8") as out:
    for idx, fs in enumerate(footer_styles):
        out.write(f"/* STYLE BLOCK {idx+1} */\n")
        out.write(fs)
        out.write("\n\n")

print("Written to scratch/footer_styles.txt")
