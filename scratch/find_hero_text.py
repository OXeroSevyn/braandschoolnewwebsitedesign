with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's search for "creative thinkers" and find the lines
lines = html.splitlines()
for idx, line in enumerate(lines):
    if "creative thinkers" in line or "Sharpen your vision" in line:
        print(f"Line {idx+1}: {line.strip()}")
        # print surrounding lines
        for offset in range(-10, 10):
            print(f"  {idx+1+offset}: {lines[idx+offset].strip()}")
