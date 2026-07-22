import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find each section of mc-grid
matches = re.findall(r'<div class="mc-grid">.*?</div>\s*(?:<!--|<a)', content, re.DOTALL)
for i, m in enumerate(matches):
    print(f"--- Grid {i+1} ---")
    print(m)
