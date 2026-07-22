with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "hamburger" in line.lower() or "mobile-menu" in line.lower() or "join-popup" in line.lower():
        if "script" in line or idx > 10000: # towards the end
            print(f"{idx+1}: {line.strip()}")
            # print 10 lines before and after
            start = max(0, idx - 15)
            end = min(len(lines), idx + 20)
            for j in range(start, end):
                print(f"  {j+1}: {lines[j].strip()}")
            print("-" * 40)
