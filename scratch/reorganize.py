#!/usr/bin/env python3
"""
reorganize.py — Reorganizes Braand School Website project structure.
Run from project root: python scratch/reorganize.py
"""

import os
import shutil
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def ensure_dir(path):
    os.makedirs(os.path.join(ROOT, path), exist_ok=True)

def move_file(src, dst):
    src_path = os.path.join(ROOT, src)
    dst_path = os.path.join(ROOT, dst)
    if not os.path.exists(src_path):
        print(f"  [SKIP] not found: {src}")
        return False
    ensure_dir(os.path.dirname(dst))
    shutil.move(src_path, dst_path)
    print(f"  [MOVE] {src}  →  {dst}")
    return True

def remove_dir(path):
    full = os.path.join(ROOT, path)
    if os.path.exists(full):
        shutil.rmtree(full)
        print(f"  [RMDIR] {path}/")

def remove_file(path):
    full = os.path.join(ROOT, path)
    if os.path.exists(full):
        os.remove(full)
        print(f"  [DEL]   {path}")

def replace_in_file(filepath, replacements):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    except Exception as e:
        print(f"  [ERR] Could not read {os.path.relpath(filepath, ROOT)}: {e}")
        return 0
    count = 0
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            count += 1
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [PATCH] {os.path.relpath(filepath, ROOT)}  ({count} substitution(s))")
    return count

def replace_in_all_files(replacements):
    exts = {'.html', '.css', '.js', '.json', '.py'}
    skip_dirs = {'.git', '__MACOSX', '.vercel'}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        # Skip scratch dir itself (so we don't patch this script)
        rel = os.path.relpath(dirpath, ROOT)
        if rel.startswith('scratch'):
            continue
        for fname in filenames:
            if os.path.splitext(fname)[1] in exts:
                replace_in_file(os.path.join(dirpath, fname), replacements)

# ══════════════════════════════════════════════════════════════
print("\n" + "="*62)
print("  BRAAND SCHOOL — PROJECT REORGANIZATION")
print("="*62)

# ─── PHASE 1: Create new directories ──────────────────────────
print("\n[1/7] Creating new image subdirectories...")
for d in ["images/logo", "images/hero", "images/bento",
          "images/gallery", "images/floaters", "images/backgrounds"]:
    ensure_dir(d)
    print(f"  [DIR]   {d}/")

# ─── PHASE 2: Move images ──────────────────────────────────────
print("\n[2/7] Moving images to organised folders...")

# Logo + badges
move_file("images/logo.png",  "images/logo/logo.png")
move_file("images/nsdc.png",  "images/logo/nsdc.png")

# Hero section images
move_file("images/hero_brand.png",               "images/hero/hero_brand.png")
move_file("images/hero_business.png",            "images/hero/hero_business.png")
move_file("images/hero_creator_inverted.png",    "images/hero/hero_creator_inverted.png")
move_file("images/hero_creator_inverted.webp",   "images/hero/hero_creator_inverted.webp")

# Bento / section shape images
for prefix in ["bento", "business", "creator"]:
    for i in range(1, 5):
        move_file(f"images/{prefix}_shape_{i}.png", f"images/bento/{prefix}_shape_{i}.png")

# Testimonial avatar headshots (root of images/)
for i in range(1, 5):
    move_file(f"images/avatar-{i}.png", f"images/testimonials/avatar-{i}.png")

# Decorative floaters
for i in range(1, 4):
    move_file(f"images/floater_{i}.png", f"images/floaters/floater_{i}.png")
move_file("images/floater_4.jpg", "images/floaters/floater_4.jpg")
move_file("images/floater_5.jpg", "images/floaters/floater_5.jpg")

# Section backgrounds / patterns
move_file("images/mission_pattern.png",                  "images/backgrounds/mission_pattern.png")
move_file("images/pngegg.png",                           "images/backgrounds/pngegg.png")
move_file("images/istockphoto-942287864-612x612.png",    "images/backgrounds/istockphoto-942287864-612x612.png")

# Student gallery / showcase images
for fname, new_fname in [
    ("brand_collab_rahul.png",   "brand_collab_rahul.png"),
    ("brand_identity_priya.png", "brand_identity_priya.png"),
    ("logo_system_anika.png",    "logo_system_anika.png"),
    ("packaging_ishaan.png",     "packaging_ishaan.png"),
    ("short_film_sneha.png",     "short_film_sneha.png"),
    ("social_campaign_arjun.png","social_campaign_arjun.png"),
    ("all certificate.png",      "all-certificate.png"),
    ("course-1.png",             "course-1.png"),
]:
    move_file(f"images/{fname}", f"images/gallery/{new_fname}")

# Root-level loose .webp files (with spaces in names)
move_file("Creator course.webp",  "images/explore-courses/creator-course.webp")
move_file("Dm Course .webp",       "images/explore-courses/dm-course.webp")
move_file("graphic design.webp",  "images/explore-courses/graphic-design.webp")

# Remove duplicate root-level course thumbnails (same files live in explore-courses/)
remove_file("images/course_design.jpg")
remove_file("images/course_marketing.jpg")
remove_file("images/course_video.jpg")

# Remove 'main course contents' dir (avatars already moved to testimonials/)
for i in range(1, 5):
    remove_file(f"images/main course contents/avatar-{i}.png")
remove_dir("images/main course contents")

# Remove mobile-bento dir (exact duplicates of explore-courses/)
remove_dir("images/mobile-bento")

# Remove empty BS BG dir
remove_dir("images/BS BG")

# Remove junk macOS artifact dir at root (gitignored but may still exist on disk)
remove_dir("__MACOSX")

# ─── PHASE 3: Move course HTML pages → courses/ ────────────────
print("\n[3/7] Moving course HTML pages to courses/...")
COURSE_PAGES = [
    "graphic-design-course.html",
    "digital-marketing-course.html",
    "video-editing-course.html",
    "ai-for-everyone.html",
    "ar-vr-course.html",
    "the-digital-art-course.html",
    "the-ui-ux-design-course.html",
]
for page in COURSE_PAGES:
    move_file(page, f"courses/{page}")

# ─── PHASE 4: Path substitutions in all HTML/CSS/JS files ─────
print("\n[4/7] Updating all image path references...")

RENAMES = [
    # ── main course contents (most specific — process first) ──
    ("images/main course contents/avatar-1.png", "images/testimonials/avatar-1.png"),
    ("images/main course contents/avatar-2.png", "images/testimonials/avatar-2.png"),
    ("images/main course contents/avatar-3.png", "images/testimonials/avatar-3.png"),
    ("images/main course contents/avatar-4.png", "images/testimonials/avatar-4.png"),
    ("images/main%20course%20contents/avatar-1.png", "images/testimonials/avatar-1.png"),
    ("images/main%20course%20contents/avatar-2.png", "images/testimonials/avatar-2.png"),
    ("images/main%20course%20contents/avatar-3.png", "images/testimonials/avatar-3.png"),
    ("images/main%20course%20contents/avatar-4.png", "images/testimonials/avatar-4.png"),

    # ── mobile-bento → explore-courses ──
    ("images/mobile-bento/course_ai_everyone.png",  "images/explore-courses/course_ai_everyone.png"),
    ("images/mobile-bento/course_ar_vr.png",         "images/explore-courses/course_ar_vr.png"),
    ("images/mobile-bento/course_design.jpg",         "images/explore-courses/course_design.jpg"),
    ("images/mobile-bento/course_digital_art.png",   "images/explore-courses/course_digital_art.png"),
    ("images/mobile-bento/course_marketing.jpg",      "images/explore-courses/course_marketing.jpg"),
    ("images/mobile-bento/course_ui_ux.png",          "images/explore-courses/course_ui_ux.png"),
    ("images/mobile-bento/course_video.jpg",          "images/explore-courses/course_video.jpg"),

    # ── Logo ──
    ("images/logo.png",  "images/logo/logo.png"),
    ("images/nsdc.png",  "images/logo/nsdc.png"),

    # ── Hero ──
    ("images/hero_creator_inverted.webp", "images/hero/hero_creator_inverted.webp"),
    ("images/hero_creator_inverted.png",  "images/hero/hero_creator_inverted.png"),
    ("images/hero_brand.png",             "images/hero/hero_brand.png"),
    ("images/hero_business.png",          "images/hero/hero_business.png"),

    # ── Bento shapes ──
    ("images/bento_shape_1.png",    "images/bento/bento_shape_1.png"),
    ("images/bento_shape_2.png",    "images/bento/bento_shape_2.png"),
    ("images/bento_shape_3.png",    "images/bento/bento_shape_3.png"),
    ("images/bento_shape_4.png",    "images/bento/bento_shape_4.png"),
    ("images/business_shape_1.png", "images/bento/business_shape_1.png"),
    ("images/business_shape_2.png", "images/bento/business_shape_2.png"),
    ("images/business_shape_3.png", "images/bento/business_shape_3.png"),
    ("images/business_shape_4.png", "images/bento/business_shape_4.png"),
    ("images/creator_shape_1.png",  "images/bento/creator_shape_1.png"),
    ("images/creator_shape_2.png",  "images/bento/creator_shape_2.png"),
    ("images/creator_shape_3.png",  "images/bento/creator_shape_3.png"),
    ("images/creator_shape_4.png",  "images/bento/creator_shape_4.png"),

    # ── Avatars ──
    ("images/avatar-1.png", "images/testimonials/avatar-1.png"),
    ("images/avatar-2.png", "images/testimonials/avatar-2.png"),
    ("images/avatar-3.png", "images/testimonials/avatar-3.png"),
    ("images/avatar-4.png", "images/testimonials/avatar-4.png"),

    # ── Floaters ──
    ("images/floater_1.png", "images/floaters/floater_1.png"),
    ("images/floater_2.png", "images/floaters/floater_2.png"),
    ("images/floater_3.png", "images/floaters/floater_3.png"),
    ("images/floater_4.jpg", "images/floaters/floater_4.jpg"),
    ("images/floater_5.jpg", "images/floaters/floater_5.jpg"),

    # ── Backgrounds ──
    ("images/mission_pattern.png",                 "images/backgrounds/mission_pattern.png"),
    ("images/pngegg.png",                          "images/backgrounds/pngegg.png"),
    ("images/istockphoto-942287864-612x612.png",   "images/backgrounds/istockphoto-942287864-612x612.png"),

    # ── Gallery / student work ──
    ("images/brand_collab_rahul.png",   "images/gallery/brand_collab_rahul.png"),
    ("images/brand_identity_priya.png", "images/gallery/brand_identity_priya.png"),
    ("images/logo_system_anika.png",    "images/gallery/logo_system_anika.png"),
    ("images/packaging_ishaan.png",     "images/gallery/packaging_ishaan.png"),
    ("images/short_film_sneha.png",     "images/gallery/short_film_sneha.png"),
    ("images/social_campaign_arjun.png","images/gallery/social_campaign_arjun.png"),
    ("images/all certificate.png",      "images/gallery/all-certificate.png"),
    ("images/all%20certificate.png",    "images/gallery/all-certificate.png"),
    ("images/course-1.png",             "images/gallery/course-1.png"),

    # ── Root-level loose .webp files ──
    ('"Creator course.webp"',  '"images/explore-courses/creator-course.webp"'),
    ("'Creator course.webp'",  "'images/explore-courses/creator-course.webp'"),
    ('"Dm Course .webp"',      '"images/explore-courses/dm-course.webp"'),
    ("'Dm Course .webp'",      "'images/explore-courses/dm-course.webp'"),
    ('"graphic design.webp"',  '"images/explore-courses/graphic-design.webp"'),
    ("'graphic design.webp'",  "'images/explore-courses/graphic-design.webp'"),

    # ── Duplicate root image/ thumbnails (now only in explore-courses/) ──
    # (just in case any file still referenced the root copies)
    ('"images/course_design.jpg"',   '"images/explore-courses/course_design.jpg"'),
    ("'images/course_design.jpg'",   "'images/explore-courses/course_design.jpg'"),
    ('"images/course_marketing.jpg"',"\"images/explore-courses/course_marketing.jpg\""),
    ("'images/course_marketing.jpg'","'images/explore-courses/course_marketing.jpg'"),
    ('"images/course_video.jpg"',    '"images/explore-courses/course_video.jpg"'),
    ("'images/course_video.jpg'",    "'images/explore-courses/course_video.jpg'"),
]

replace_in_all_files(RENAMES)

# ─── PHASE 5: Update vercel.json destinations ─────────────────
print("\n[5/7] Updating vercel.json...")
vercel_path = os.path.join(ROOT, "vercel.json")
with open(vercel_path, 'r', encoding='utf-8') as f:
    vercel = json.load(f)

COURSE_DESTS = {
    "/graphic-design-course",
    "/video-editing-course",
    "/digital-marketing-course",
    "/ai-for-everyone",
    "/ar-vr-course",
    "/the-digital-art-course",
    "/the-ui-ux-design-course",
}

for rw in vercel.get("rewrites", []):
    dest = rw.get("destination", "")
    if dest in COURSE_DESTS:
        new_dest = "/courses" + dest
        print(f"  [UPDATE] {rw['source']}  →  {new_dest}")
        rw["destination"] = new_dest

with open(vercel_path, 'w', encoding='utf-8') as f:
    json.dump(vercel, f, indent=2)
    f.write('\n')

# ─── PHASE 6: Update dev_server.py ────────────────────────────
print("\n[6/7] Updating dev_server.py course routes...")
ds_path = os.path.join(ROOT, "dev_server.py")
with open(ds_path, 'r', encoding='utf-8') as f:
    ds = f.read()

OLD = 'self.path = f"/{course_name}.html"'
NEW = 'self.path = f"/courses/{course_name}.html"'
if OLD in ds:
    ds = ds.replace(OLD, NEW)
    print(f"  [UPDATE] course file path  →  /courses/{{course_name}}.html")
else:
    print("  [WARN]  Pattern not found in dev_server.py — check manually")

with open(ds_path, 'w', encoding='utf-8') as f:
    f.write(ds)

# ─── PHASE 7: Write images/README.md guide ────────────────────
print("\n[7/7] Writing images/README.md guide...")
readme = """\
# 📸 Images — Quick Reference Guide

Organised by purpose. To swap any image, just replace the file and keep the same filename.

| Folder | What's inside |
|---|---|
| `logo/` | Site logo (`logo.png`), NSDC badge (`nsdc.png`) |
| `hero/` | Homepage hero images (brand, business, creator versions) |
| `explore-courses/` | Course card thumbnails shown on homepage + course listing |
| `bento/` | Bento-grid shape images for each section (brand / business / creator) |
| `gallery/` | Student work showcase, certificate image, course-1 |
| `testimonials/` | Testimonial avatar headshots (`avatar-1.png` → `avatar-4.png`) |
| `mentors/` | Mentor profile photos |
| `floaters/` | Decorative floating graphics used in the manifesto section |
| `backgrounds/` | Background patterns and textures |
| `featured/` | Press / media logos (Times of India, YourStory, etc.) |
| `tools/` | Tool icons (Figma, Adobe CC, etc.) |
| `philosophy-icons/` | SVG icons for the Philosophy / Pedagogy section |
| `builtby/` | "Built by students" section showcase images |
| `courses/` | Per-course images, one subfolder per course |

## How to Replace an Image
1. Find the right subfolder above
2. Drop in your new file
3. **Keep the exact same filename** — the site picks it up automatically
4. If you must use a different filename, search for the old name in the relevant `.html` file and update it there

## ⚠️ Before deleting any image
Search for its filename across the `.html` files to confirm it's no longer referenced.
"""
with open(os.path.join(ROOT, "images", "README.md"), 'w', encoding='utf-8') as f:
    f.write(readme)
print("  [WRITE] images/README.md")

# ══════════════════════════════════════════════════════════════
print("\n" + "="*62)
print("  ✅  REORGANIZATION COMPLETE!")
print("="*62)
print()
print("  Next:")
print("  1. Restart dev server:  python dev_server.py 8080")
print("  2. Test all pages in the browser")
print("  3. git add -A && git commit -m 'Reorganise project folder structure'")
print()
