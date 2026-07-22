import os

# Paths to the target files
files = [
    r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\video-editing-course.html",
    r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\graphic-design-course.html",
    r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\digital-marketing-course.html",
    r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\courses\digital-marketing-course-siliguri.html"
]

# Source file containing the correct Team Section HTML and CSS
source_file = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\index.html"

with open(source_file, "r", encoding="utf-8") as f:
    index_content = f.read()

# Extract Team Section HTML
team_html_start = '  <!-- ── OUR TEAM SECTION ── -->'
team_html_end = '  <!-- ── APPLY / BATCH INFO SECTION ── -->'
start_idx = index_content.find(team_html_start)
end_idx = index_content.find(team_html_end)

if start_idx == -1 or end_idx == -1:
    print("Error: Could not find team section in index.html")
    exit(1)

team_html_full = index_content[start_idx:end_idx]

# Extract team section style block inside the team section in index.html
# It starts with `<style>` and ends with `</style>` right before APPLY
style_start_idx = team_html_full.find("<style>")
style_end_idx = team_html_full.find("</style>")

if style_start_idx == -1 or style_end_idx == -1:
    print("Error: Could not find style in team html block")
    exit(1)

team_style_content = team_html_full[style_start_idx:style_end_idx + 8]
# Remove the style block from team_html so we can keep HTML and CSS separate if needed, 
# or keep it as is. Actually index.html has the style tag embedded directly after the section.
# Let's inspect how index.html structure is.
# In index.html, we have:
# <section class="team-section" id="our-team"> ... </section>
# <style> ... </style>
# And then the next section.
# So we can copy the whole block (HTML + Style) directly!
# Let's check how the course pages are structured.
# The course pages have:
# 1. CSS styles in the head/top style block (.builtby-section { ... })
# 2. HTML section in the body (<section class="builtby-section reveal"> ... </section>)
# It's cleaner to:
# 1. Replace the `.builtby-section` style rules in the CSS block with the team section style rules.
# 2. Replace the `<section class="builtby-section ..."> ... </section>` HTML block in the body with the team section HTML block.

# Let's extract clean CSS rules (without style tag)
clean_css = team_html_full[style_start_idx + 7 : style_end_idx].strip()
# Let's extract clean HTML section (without style tag)
clean_html = (team_html_full[:style_start_idx] + team_html_full[style_end_idx + 8:]).strip()

print(f"Extracted clean HTML length: {len(clean_html)}")
print(f"Extracted clean CSS length: {len(clean_css)}")

# Define targets for replacement in the course pages
builtby_css_start = '/* Built By Section */'
builtby_css_end = '/* ─── OUR ALUMNI NETWORK'

builtby_html_start = '<!-- BUILT BY SECTION -->'
builtby_html_end = '<!-- ── OUR ALUMNI NETWORK SECTION ── -->'

for file_path in files:
    if not os.path.exists(file_path):
        print(f"Warning: File not found: {file_path}")
        continue
        
    print(f"Processing: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the CSS block to replace
    css_start_idx = content.find(builtby_css_start)
    if css_start_idx == -1:
        # Try another common comment if any
        print(f"  Warning: could not find CSS start in {file_path}")
        continue

    # We need to find the end of the builtby CSS block, which is right before OUR ALUMNI NETWORK styling
    css_end_idx = content.find(builtby_css_end)
    if css_end_idx == -1:
        print(f"  Warning: could not find CSS end in {file_path}")
        continue

    # Find the HTML block to replace
    html_start_idx = content.find(builtby_html_start)
    if html_start_idx == -1:
        print(f"  Warning: could not find HTML start in {file_path}")
        continue

    html_end_idx = content.find(builtby_html_end)
    if html_end_idx == -1:
        print(f"  Warning: could not find HTML end in {file_path}")
        continue

    # Perform the replacements
    # 1. Replace the CSS block
    new_css = f"/* ── OUR TEAM — COMPACT TWO-COLUMN ── */\n      {clean_css}\n\n      "
    content_updated_css = content[:css_start_idx] + new_css + content[css_end_idx:]

    # Recalculate HTML positions because content length changed
    html_start_idx = content_updated_css.find(builtby_html_start)
    html_end_idx = content_updated_css.find(builtby_html_end)

    # 2. Replace the HTML block
    new_html = f"{clean_html}\n\n  "
    final_content = content_updated_css[:html_start_idx] + new_html + content_updated_css[html_end_idx:]

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"  Successfully updated {file_path}")
