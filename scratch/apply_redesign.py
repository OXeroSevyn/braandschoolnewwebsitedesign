import os
import json
import re

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"
json_path = os.path.join(base_dir, "scratch", "extracted_testimonials.json")

with open(json_path, 'r', encoding='utf-8') as f:
    testimonials_data = json.load(f)

# Extract new CSS from index.html (lines 7685 to 8110)
index_path = os.path.join(base_dir, "index.html")
with open(index_path, 'r', encoding='utf-8') as f:
    index_lines = f.readlines()

new_css_lines = index_lines[7684:8110]
new_css = "".join(new_css_lines)

# Additional CSS to style the badge inside the new speech bubbles if any exist
badge_css = """
    /* --- Testimonial Badge support --- */
    .testi-badge {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: #ffffff;
      border: 1px solid rgba(0, 0, 0, 0.08);
      padding: 8px 16px;
      border-radius: 12px;
      margin-top: 16px;
      width: fit-content;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .testi-badge-label {
      font-size: 11px;
      text-transform: uppercase;
      font-family: var(--font-mono);
      line-height: 1.2;
      color: #6b7280;
    }
    .testi-badge-arrow {
      color: #9ca3af;
      font-weight: 700;
    }
    .testi-badge-value {
      font-size: 14px;
      font-weight: 700;
      color: #10b981;
    }
"""

new_css = new_css + "\n" + badge_css

# JavaScript logic for drag-to-scroll and button click scrolling
new_js = """
    document.addEventListener('DOMContentLoaded', () => {
      const stage = document.querySelector('.fg-stage');
      const slider = document.querySelector('.fg-scroll-container');
      if (!slider) return;

      // --- Mouse Drag Logic ---
      let isDown = false;
      let startX;
      let scrollLeft;

      slider.addEventListener('mousedown', (e) => {
        isDown = true;
        slider.classList.add('active');
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
        slider.style.scrollBehavior = 'auto';
      });

      slider.addEventListener('mouseleave', () => {
        isDown = false;
        slider.classList.remove('active');
      });

      slider.addEventListener('mouseup', () => {
        isDown = false;
        slider.classList.remove('active');
        slider.style.scrollBehavior = 'smooth';
      });

      slider.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 2;
        slider.scrollLeft = scrollLeft - walk;
      });

      // --- Header Scroll Reveal Logic ---
      const header = document.querySelector('.fg-header-inner');
      if (header) {
        const headerObserver = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.classList.add('visible');
              headerObserver.unobserve(entry.target);
            }
          });
        }, { threshold: 0.1 });
        headerObserver.observe(header);
      }
    });

    function scrollSlider(btn, direction) {
      const wrapper = btn.closest('section');
      if (!wrapper) return;
      
      const grid = wrapper.querySelector('.fg-scroll-container');
      if (grid) {
        const scrollAmount = window.innerWidth * 0.8;
        grid.scrollBy({ left: scrollAmount * direction, behavior: 'smooth' });
      }
    }
"""

files = [
    "graphic-design-course.html",
    "video-editing-course.html",
    "digital-marketing-course.html",
    "courses/digital-marketing-course-siliguri.html"
]

for file_path in files:
    full_path = os.path.join(base_dir, file_path)
    if not os.path.exists(full_path):
        print(f"Skipping: {file_path} (not found)")
        continue
    
    print(f"Processing: {file_path}")
    
    # Read file content
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Backup file
    with open(full_path + ".bak", 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Generate HTML cards for this file
    cards_html = ""
    file_key = file_path.replace("\\", "/")
    
    # Fallback to key matching name if not exact
    matching_key = file_key
    if matching_key not in testimonials_data:
        # try without leading courses/
        matching_key = os.path.basename(file_path)
        
    testimonials = testimonials_data.get(file_key, [])
    for t in testimonials:
        badge_code = t.get("badge_html", "")
        if badge_code:
            # Let's clean up badge code formatting a bit
            badge_code = badge_code.replace("testi-badge", "testi-badge") # keeping name for support
            badge_code = "\n              " + badge_code
            
        role_html = f'<p class="tm-role">{t["role"]}</p>' if t["role"] else ''
        
        cards_html += f"""
          <!-- Testimonial -->
          <div class="fg-card">
            <div class="fg-card-inner">
              <span class="tm-quote-mark">“</span>
              <p class="tm-quote">{t["quote"]}</p>{badge_code}
              <div class="tm-author-wrap">
                <div class="tm-avatar">
                  <img src="{t["src"]}" alt="{t["name"]}" onerror="{t["onerror"]}">
                </div>
                <div class="tm-details">
                  <h3 class="tm-name">{t["name"]}</h3>
                  {role_html}
                </div>
              </div>
            </div>
          </div>
"""

    new_html = f"""<!-- ── STUDENT TESTIMONIALS SECTION ── -->
  <section class="faculty-gallery" id="testimonials">
    <!-- Ambient background effects -->
    <div class="lp-bg-effects">
      <div class="lp-glow lp-glow--1"></div>
      <div class="lp-glow lp-glow--2"></div>
      <div class="lp-noise"></div>
    </div>

    <div class="fg-header">
      <div class="fg-header-inner reveal">
        <div class="fg-eyebrow">
          <span class="fg-dot"></span>
          <span class="fg-kicker">Student Success</span>
        </div>
        <h2 class="fg-title">2,400+ students.<br><span class="italic-playfair">Real</span> jumps. <span class="italic-playfair">Real</span> receipts.</h2>
        <p class="fg-desc">We don't pay influencers for testimonials. These are people from past cohorts — most are happy to jump on a call with you before you enroll.</p>
      </div>
    </div>

    <div class="fg-stage">
      <div class="fg-scroll-container">
        <div class="fg-grid">
          {cards_html.strip()}
        </div>
      </div>
      <div class="slider-controls">
        <button class="slider-btn" aria-label="Previous" onclick="scrollSlider(this, -1)">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
        </button>
        <button class="slider-btn" aria-label="Next" onclick="scrollSlider(this, 1)">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>
      </div>
    </div>
  </section>"""

    # 1. Replace HTML section
    # Find start and end of testi-section
    html_match = re.search(r'<section class="testi-section reveal">', content)
    if not html_match:
        html_match = re.search(r'<section class="testi-section">', content)
        
    if html_match:
        start_idx = html_match.start()
        end_idx = content.find('</section>', start_idx) + len('</section>')
        content = content[:start_idx] + new_html + content[end_idx:]
    else:
        print("Error: HTML section not found in file")
        continue

    # 2. Replace CSS blocks
    # Remove first block (/* Testimonials Section */)
    css_start_1 = content.find("/* Testimonials Section */")
    if css_start_1 != -1:
        # Find next block comment
        chunk_1 = content[css_start_1:css_start_1+15000]
        # Locate next comment start after /* Testimonials Section */
        next_comment_pos = chunk_1.find("/*", 50)
        if next_comment_pos != -1:
            css_end_1 = css_start_1 + next_comment_pos
            content = content[:css_start_1] + content[css_end_1:]
        else:
            print("Warning: Next CSS block comment not found, searching for closing tag or end of styles")
            
    # Remove second block (/* ─── TESTIMONIALS 3D COVERFLOW REDESIGN ─── */)
    css_start_2 = content.find("/* ─── TESTIMONIALS 3D COVERFLOW REDESIGN ─── */")
    if css_start_2 != -1:
        chunk_2 = content[css_start_2:css_start_2+15000]
        style_close_pos = chunk_2.find("</style>")
        if style_close_pos != -1:
            css_end_2 = css_start_2 + style_close_pos
            # Insert the new CSS right here before </style>
            content = content[:css_start_2] + "\n" + new_css + "\n" + content[css_end_2:]
            
    # 3. Replace JS block
    js_start = content.find("// ─── TESTIMONIALS COVERFLOW INTERACTION SYSTEM ───")
    if js_start != -1:
        chunk_js = content[js_start:js_start+15000]
        js_end_pos = chunk_js.find("</script>")
        if js_end_pos != -1:
            js_end = js_start + js_end_pos
            content = content[:js_start] + new_js + "\n" + content[js_end:]
    else:
        print("Warning: JS interaction block comment not found, trying regex")
        # try regex for interaction block if any
        
    # Save the updated file
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {file_path}")
