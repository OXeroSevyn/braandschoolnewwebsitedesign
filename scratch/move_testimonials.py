with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find start of testimonials
testi_start = -1
for idx, line in enumerate(lines):
    if "STUDENT TESTIMONIALS SECTION" in line:
        testi_start = idx
        break

if testi_start == -1:
    print("Could not find start of testimonials section!")
    exit(1)

# Find end of testimonials (the closing style tag before .faq-section style)
testi_end = -1
for idx in range(testi_start, len(lines)):
    if ".faq-section" in lines[idx]:
        for j in range(idx - 1, testi_start, -1):
            if "</style>" in lines[j]:
                testi_end = j
                break
        break

if testi_end == -1:
    print("Could not find end of testimonials section style!")
    exit(1)

print(f"Moving lines {testi_start+1} to {testi_end+1}...")

# Slice the list
testi_lines = lines[testi_start:testi_end+1]
remaining_lines = lines[:testi_start] + lines[testi_end+1:]

# Find the end of authorized section:
# We look for the closing </section> of the authorized section.
auth_start = -1
for idx, line in enumerate(remaining_lines):
    if "class=\"authorized-section\"" in line or "class='authorized-section'" in line:
        auth_start = idx
        break

if auth_start == -1:
    print("Could not find authorized-section start!")
    exit(1)

auth_end = -1
for idx in range(auth_start, len(remaining_lines)):
    if "</section>" in remaining_lines[idx]:
        auth_end = idx
        break

if auth_end == -1:
    print("Could not find authorized-section end!")
    exit(1)

print(f"Authorized section ends at line {auth_end+1} in remaining lines.")

# Insert after auth_end
final_lines = remaining_lines[:auth_end+1] + ["\n"] + testi_lines + remaining_lines[auth_end+1:]

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(final_lines)

print("Successfully moved testimonials section right after authorized section!")
