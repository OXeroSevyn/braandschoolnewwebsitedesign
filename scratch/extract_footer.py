import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for <footer ... > ... </footer>
match = re.search(r"<footer.*?>.*?</footer>", content, re.DOTALL | re.IGNORECASE)
if match:
    print("FOUND FOOTER:")
    with open("scratch/footer_output.txt", "w", encoding="utf-8") as out:
        out.write(match.group(0))
    print("Footer content written to scratch/footer_output.txt")
else:
    print("NO FOOTER TAG FOUND")
    # Search for something containing footer class
    match2 = re.search(r'<div\s+class="[^"]*footer[^"]*"[^>]*>.*?</div>', content, re.DOTALL | re.IGNORECASE)
    if match2:
        print("FOUND FOOTER DIV:")
        with open("scratch/footer_output.txt", "w", encoding="utf-8") as out:
            out.write(match2.group(0))
    else:
        print("NO FOOTER DIV FOUND")
