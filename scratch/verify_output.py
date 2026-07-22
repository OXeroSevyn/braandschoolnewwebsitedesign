import os
from bs4 import BeautifulSoup

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"
file_path = os.path.join(base_dir, "graphic-design-course.html")

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

sect = soup.find('section', id='testimonials')
if sect:
    print("Found section id='testimonials'")
    print("Classes:", sect.get('class'))
    header = sect.find(class_='fg-header')
    if header:
        print("Header Title:", header.find(class_='fg-title').get_text(strip=True))
    grid = sect.find(class_='fg-grid')
    if grid:
        cards = grid.find_all(class_='fg-card')
        print(f"Found {len(cards)} testimonial cards")
        if cards:
            print("First Card text:", cards[0].find(class_='tm-quote').get_text(strip=True))
            img = cards[0].find('img')
            print("First Card Avatar src:", img.get('src') if img else "None")
else:
    print("Could not find testimonials section!")
