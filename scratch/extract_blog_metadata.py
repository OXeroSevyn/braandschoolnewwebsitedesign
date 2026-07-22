import os
import re
import json

blogs_dir = "/Users/isharoka/Downloads/MAin website/blogs"
output_file = "/Users/isharoka/Downloads/MAin website/scratch/blog_metadata.json"

metadata = []

for folder in os.listdir(blogs_dir):
    if folder.startswith("."):
        continue
    folder_path = os.path.join(blogs_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    index_path = os.path.join(folder_path, "index.html")
    if not os.path.exists(index_path):
        continue
        
    try:
        with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
            
        # 1. Extract Title
        title = ""
        title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()
            # Clean up title suffixes
            title = re.sub(r'\s*&#8211;\s*Braand.*$', '', title)
            title = re.sub(r'\s*–\s*Braand.*$', '', title)
            title = re.sub(r'\s*-\s*Braand.*$', '', title)
            title = re.sub(r'\s*&#8211;\s*Braand\s*School.*$', '', title)
            title = re.sub(r'\s*–\s*Braand\s*School.*$', '', title)
            title = re.sub(r'\s*-\s*Braand\s*School.*$', '', title)
            title = title.replace("&#8217;", "’").replace("&amp;", "&")

        # 2. Extract Date
        date_str = ""
        # Look for the date block
        # <div class="post-date">\s*<span>Published</span>\s*<span class="text-big">\s*(.*?)\s*</span>
        date_match = re.search(r'class="post-date"[^>]*>.*?<span class="text-big">\s*(.*?)\s*</span>', html, re.DOTALL | re.IGNORECASE)
        if date_match:
            date_str = date_match.group(1).strip()
            date_str = re.sub(r'\s+', ' ', date_str)
            
        if not date_str:
            # Fallback to general Month DD, YYYY regex
            date_match2 = re.search(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b', html)
            if date_match2:
                date_str = date_match2.group(0)
            else:
                # Look for upload folder date e.g. wp-content/uploads/2026/04/
                upload_match = re.search(r'uploads/(\d{4})/(\d{2})/', html)
                if upload_match:
                    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                    year = upload_match.group(1)
                    month_num = int(upload_match.group(2))
                    if 1 <= month_num <= 12:
                        date_str = f"{months[month_num]} {year}"
                    else:
                        date_str = "2026"
                else:
                    date_str = "2026"

        # 3. Extract Image
        img_url = ""
        # Noxfolio/custom themes have <div class="entry-media"> ... <img ... src="url" ... />
        media_match = re.search(r'class="entry-media"[^>]*>.*?<img[^>]+src=["\'](.*?)["\']', html, re.DOTALL | re.IGNORECASE)
        if media_match:
            img_url = media_match.group(1).strip()
        else:
            # Fallback 1: og:image
            og_match = re.search(r'<meta\s+property=["\']og:image["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
            if og_match:
                img_url = og_match.group(1).strip()
            else:
                # Fallback 2: first img tag
                first_img = re.search(r'<img[^>]+src=["\'](.*?)["\']', html, re.IGNORECASE)
                if first_img:
                    img_url = first_img.group(1).strip()
                    
        # Normalize relative image paths to root-relative path of our domain
        # e.g., "../wp-content/uploads/..." -> "/blogs/wp-content/uploads/..."
        if img_url.startswith("../"):
            img_url = "/" + img_url.replace("../", "blogs/", 1)
        elif img_url.startswith("http://braand.local/"):
            img_url = img_url.replace("http://braand.local/", "/blogs/", 1)
        elif img_url.startswith("https://braandschool.com/"):
            img_url = img_url.replace("https://braandschool.com/", "/", 1)
            # if it starts with /wp-content, it should probably be /blogs/wp-content since the folders were moved
            if img_url.startswith("/wp-content/"):
                img_url = "/blogs" + img_url

        # 4. Extract Description
        desc = ""
        # Noxfolio theme article content usually is in <div class="entry-content ...">
        # Let's search for first few <p> tags inside or outside
        p_matches = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL | re.IGNORECASE)
        for p_content in p_matches:
            # Strip HTML tags from paragraph content
            p_text = re.sub(r'<[^>]+>', '', p_content).strip()
            # Skip empty, short, or share/meta paragraphs
            if not p_text or len(p_text) < 40 or "cookie" in p_text.lower() or "javascript" in p_text.lower():
                continue
            desc = p_text
            break
            
        if not desc:
            # Try meta description
            desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
            if desc_match:
                desc = desc_match.group(1).strip()
                
        if len(desc) > 180:
            desc = desc[:177] + "..."
        desc = desc.replace("&#8217;", "’").replace("&amp;", "&").replace("&#8211;", "–").replace("&#8220;", "“").replace("&#8221;", "”")

        metadata.append({
            "slug": folder,
            "title": title,
            "date": date_str,
            "description": desc,
            "image": img_url,
        })
    except Exception as e:
        print(f"Error parsing {folder}: {e}")

# Save output
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

print(f"Extracted metadata for {len(metadata)} blogs to {output_file}")
