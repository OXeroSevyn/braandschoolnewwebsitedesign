import os
import re
import json
from datetime import datetime

blogs_dir = "/Users/isharoka/Downloads/MAin website/blogs"
blog_html_path = "/Users/isharoka/Downloads/MAin website/blog.html"
metadata_file = "/Users/isharoka/Downloads/MAin website/scratch/blog_metadata.json"

with open(metadata_file, "r", encoding="utf-8") as f:
    blogs = json.load(f)

# Parse categories from each blog folder
for b in blogs:
    slug = b["slug"]
    index_path = os.path.join(blogs_dir, slug, "index.html")
    category = "general"
    if os.path.exists(index_path):
        try:
            with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            # Find categories
            cat_match = re.search(r'class="post-categories">.*?<a[^>]*>(.*?)</a>', content, re.DOTALL | re.IGNORECASE)
            if cat_match:
                category = cat_match.group(1).strip().lower()
        except Exception:
            pass
    b["category"] = category

# Parse dates for sorting
months = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
}

def parse_date(date_str):
    try:
        # Expected: "Month DD, YYYY"
        # e.g., "June 25, 2024"
        parts = date_str.replace(",", "").split()
        if len(parts) == 3:
            m = months[parts[0].lower()]
            d = int(parts[1])
            y = int(parts[2])
            return datetime(y, m, d)
        elif len(parts) == 2:
            m = months[parts[0].lower()]
            y = int(parts[1])
            return datetime(y, m, 1)
        elif len(parts) == 1:
            return datetime(int(parts[0]), 1, 1)
    except Exception:
        pass
    return datetime(2020, 1, 1)

blogs.sort(key=lambda b: parse_date(b["date"]), reverse=True)

# Generate HTML string
html_items = []
for index, b in enumerate(blogs):
    slug = b["slug"]
    title = b["title"]
    date = b["date"]
    desc = b["description"]
    img = b["image"] if b["image"] else "https://braandschool.com/wp-content/uploads/2023/10/cropped-bs-logo.png"
    cat = b["category"]
    
    item_html = f"""
                <div class="onovo-blog-item archive-item" data-category="{cat}">
                  <div id="post-{index}" class="post-{index} post type-post status-publish format-standard has-post-thumbnail hentry">
                    <div class="image" data-onovo-overlay="" data-onovo-scroll="">
                      <a href="/blogs/{slug}/">
                        <img src="{img}" alt="{title}" />
                      </a>
                    </div>
                    <div class="desc">
                      <div class="info">
                        <div class="date">
                          {date}
                        </div>
                      </div>
                      <h3 class="title">
                        <a href="/blogs/{slug}/">{title}</a>
                      </h3>
                      <div class="onovo-text">
                        <p>
                          {desc}
                          <br />
                          <a href="/blogs/{slug}/" class="onovo-btn onovo-hover-btn">
                            <span>Read more</span>
                          </a>
                        </p>
                      </div>
                    </div>
                  </div>
                </div>"""
    html_items.append(item_html)

generated_html = "\n".join(html_items)

# Write generated html code to a file so we can read/use it
with open("/Users/isharoka/Downloads/MAin website/scratch/generated_blogs.html", "w", encoding="utf-8") as f:
    f.write(generated_html)

print("Generated HTML for 42 blogs!")
