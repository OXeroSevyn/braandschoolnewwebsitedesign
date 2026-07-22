import os
import sys
from bs4 import BeautifulSoup

# Set console encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

files = [
    "graphic-design-course.html",
    "video-editing-course.html",
    "digital-marketing-course.html",
    "courses/digital-marketing-course-siliguri.html"
]

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"

for file_path in files:
    full_path = os.path.join(base_dir, file_path)
    if not os.path.exists(full_path):
        continue
    
    print(f"\n==================== {file_path} ====================")
    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Let's find the testimonials section or cards
    # Coverflow cards are inside .testi-coverflow-stage or .testi-grid
    cards = soup.select(".testi-card, .testi-coverflow-card")
    for idx, card in enumerate(cards):
        # Extract quote
        quote_p = card.select_one(".testi-p")
        quote = quote_p.get_text(strip=True) if quote_p else ""
        
        # Extract avatar
        img = card.select_one(".testi-avatar")
        src = img.get('src') if img else ""
        onerror = img.get('onerror') if img else ""
        
        # Extract name & role
        name_div = card.select_one(".testi-name")
        name = name_div.get_text(strip=True) if name_div else ""
        
        role_div = card.select_one(".testi-role")
        role = role_div.get_text(strip=True) if role_div else ""
        
        # Extract badge details if any
        badge = card.select_one(".testi-badge")
        badge_text = ""
        if badge:
            badge_text = badge.get_text(separator=" | ", strip=True)
            
        print(f"Card {idx+1}:")
        print(f"  Name: {name}")
        print(f"  Role: {role}")
        print(f"  Src: {src} (onerror: {onerror})")
        print(f"  Quote: {quote}")
        if badge_text:
            print(f"  Badge: {badge_text}")
        print()
