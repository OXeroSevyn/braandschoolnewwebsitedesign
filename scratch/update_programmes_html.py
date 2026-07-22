with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's replace Card 1
card1_old = """        <!-- Card 1: Business & Marketing -->
        <div class="mc-card">
          <div class="mc-visual mc-visual--bm">
          </div>
          <div class="mc-body">
            <div class="mc-title-group">
              <h3 class="mc-title">BUSINESS & MARKETING</h3>
            </div>"""

card1_new = """        <!-- Card 1: Business & Marketing -->
        <div class="mc-card" onclick="window.location.href='/course/digital-marketing-course-siliguri';">
          <div class="mc-visual mc-visual--bm">
            <div class="mc-image-arrow">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </div>
          </div>
          <div class="mc-body">
            <div class="mc-mobile-info">
              <div class="mc-mob-category">Marketing</div>
              <h3 class="mc-mob-title">The Business & Marketing <span class="mc-mob-underline">Course</span></h3>
            </div>
            <div class="mc-title-group">
              <h3 class="mc-title">BUSINESS & MARKETING</h3>
            </div>"""

# Let's replace Card 2
card2_old = """        <!-- Card 2: Brand & Design -->
        <div class="mc-card">
          <div class="mc-visual mc-visual--bd">
          </div>
          <div class="mc-body">
            <div class="mc-title-group">
              <h3 class="mc-title">BRAND & DESIGN</h3>
            </div>"""

card2_new = """        <!-- Card 2: Brand & Design -->
        <div class="mc-card" onclick="window.location.href='/course/graphic-design-course-siliguri';">
          <div class="mc-visual mc-visual--bd">
            <div class="mc-image-arrow">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </div>
          </div>
          <div class="mc-body">
            <div class="mc-mobile-info">
              <div class="mc-mob-category">Design</div>
              <h3 class="mc-mob-title">The Graphic Design <span class="mc-mob-underline">Course</span></h3>
            </div>
            <div class="mc-title-group">
              <h3 class="mc-title">BRAND & DESIGN</h3>
            </div>"""

# Let's replace Card 3
card3_old = """        <!-- Card 3: Content & Video -->
        <div class="mc-card">
          <div class="mc-visual mc-visual--cv">
          </div>
          <div class="mc-body">
            <div class="mc-title-group">
              <h3 class="mc-title">CONTENT & VIDEO</h3>
            </div>"""

card3_new = """        <!-- Card 3: Content & Video -->
        <div class="mc-card" onclick="window.location.href='/course/video-motion-course-siliguri';">
          <div class="mc-visual mc-visual--cv">
            <div class="mc-image-arrow">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </div>
          </div>
          <div class="mc-body">
            <div class="mc-mobile-info">
              <div class="mc-mob-category">Creator</div>
              <h3 class="mc-mob-title">The Content & Video <span class="mc-mob-underline">Course</span></h3>
            </div>
            <div class="mc-title-group">
              <h3 class="mc-title">CONTENT & VIDEO</h3>
            </div>"""

if card1_old in html:
    html = html.replace(card1_old, card1_new)
else:
    print("WARNING: card1_old not found!")

if card2_old in html:
    html = html.replace(card2_old, card2_new)
else:
    print("WARNING: card2_old not found!")

if card3_old in html:
    html = html.replace(card3_old, card3_new)
else:
    print("WARNING: card3_old not found!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated Card HTML blocks!")
