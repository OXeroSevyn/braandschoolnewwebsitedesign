import os
import json
from bs4 import BeautifulSoup

files = [
    "graphic-design-course.html",
    "video-editing-course.html",
    "digital-marketing-course.html",
    "courses/digital-marketing-course-siliguri.html"
]

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"
data = {}

for file_path in files:
    full_path = os.path.join(base_dir, file_path)
    if not os.path.exists(full_path):
        continue
    
    data[file_path] = []
    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    cards = soup.select(".testi-card, .testi-coverflow-card")
    for idx, card in enumerate(cards):
        quote_p = card.select_one(".testi-p")
        quote = quote_p.get_text(strip=True) if quote_p else ""
        
        img = card.select_one(".testi-avatar")
        src = img.get('src') if img else ""
        onerror = img.get('onerror') if img else ""
        
        name_div = card.select_one(".testi-name")
        name = name_div.get_text(strip=True) if name_div else ""
        
        role_div = card.select_one(".testi-role")
        role = role_div.get_text(strip=True) if role_div else ""
        
        badge = card.select_one(".testi-badge")
        badge_html = str(badge) if badge else ""
        
        data[file_path].append({
            "name": name,
            "role": role,
            "src": src,
            "onerror": onerror,
            "quote": quote,
            "badge_html": badge_html
        })

with open(os.path.join(base_dir, "scratch", "extracted_testimonials.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("Done! Saved to scratch/extracted_testimonials.json")
