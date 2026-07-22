with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

found_nav = False
nav_lines = []
for idx, line in enumerate(lines):
    if "<nav" in line:
        found_nav = True
    if found_nav:
        nav_lines.append((idx + 1, line))
        if "</nav>" in line:
            break

for num, line in nav_lines:
    print(f"{num}: {line}", end="")

found_mob = False
mob_lines = []
for idx, line in enumerate(lines):
    if 'class="mobile-menu"' in line or 'class=\'mobile-menu\'' in line:
        found_mob = True
    if found_mob:
        mob_lines.append((idx + 1, line))
        if "</div>" in line and len(mob_lines) > 20: # simple end heuristic or count nesting
            pass
# Let's also print 50 lines after mobile-menu starts to see its end
for idx, line in enumerate(lines):
    if 'class="mobile-menu"' in line:
        for i in range(idx, idx + 80):
            print(f"MOB {i+1}: {lines[i]}", end="")
        break
