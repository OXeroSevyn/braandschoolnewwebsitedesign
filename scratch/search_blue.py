import re

def search_in_file(filename, out_f):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    # search for keywords like 'blue', 'rgb(0', 'rgba(0', '#0000ff', '#00f' or similar blue hues
    matches = re.finditer(r"([^{}]*(?:blue|#0000ff|rgba?\(\s*0\s*,\s*\d+\s*,\s*255|rgba?\(\s*0\s*,\s*0\s*,\s*255)[^{}]*\{.*?\})", content, re.IGNORECASE | re.DOTALL)
    out_f.write(f"=== Matches in {filename} ===\n")
    count = 0
    for m in matches:
        out_f.write(m.group(0)[:500] + "\n")
        out_f.write("-" * 30 + "\n")
        count += 1
    if count == 0:
        out_f.write("No matches found.\n")

with open("scratch/blue_output.txt", "w", encoding="utf-8") as out:
    search_in_file("index.html", out)
    search_in_file("assets/css/main.css", out)

print("Done, written to scratch/blue_output.txt")
