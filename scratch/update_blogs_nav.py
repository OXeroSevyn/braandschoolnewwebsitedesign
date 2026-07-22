# python script to update blogs.html with unified menu bar

with open("blogs.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update <head>
head_insert = """    <!-- Unified Website Resources -->
    <link rel="stylesheet" href="assets/css/main.css">
    <link rel="stylesheet" href="assets/css/navbar.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
    <script src="assets/js/main.js" defer></script>
  </head>"""

html = html.replace("  </head>", head_insert)

# 2. Extract legacy header area
# We want to replace from <div class="site-preloader" id="preloader"> (line 106)
# to </header> (line 226)

import re
# Regex to find preloader and header blocks
pattern = re.compile(r'<div class="site-preloader" id="preloader">.*?<header class="site-header default-header">.*?</header>', re.DOTALL)

new_navbar_markup = """  <nav>
    <a href="/index.html" class="nav-logo">
      <div class="brand-logo-icon">
        <div class="logo-box box-1"></div>
        <div class="logo-box box-2"></div>
        <div class="logo-box box-main">
          <div class="logo-icon-text">B<span class="small-s">s</span></div>
        </div>
      </div>
    </a>

    <ul class="nav-links">
      <li><a href="/index.html">Home</a></li>
      <li class="nav-dropdown-wrapper">
        <div style="display: flex; align-items: center; gap: 4px;">
          <a href="/course.html" class="nav-courses-link" style="padding-right: 0;">
            Our Courses
          </a>
          <button type="button" class="nav-dropdown-toggle" id="desktop-courses-toggle" aria-label="Toggle Courses Dropdown" style="background: none; border: none; color: inherit; cursor: pointer; padding: 4px; display: flex; align-items: center; opacity: 0.7; transition: opacity 0.2s;">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
          </button>
        </div>
        <div class="nav-dropdown-menu" id="desktop-courses-submenu">
          <a href="/course/braanding-course">Brand & Design</a>
          <a href="/course/creator-course">Content & Video</a>
          <a href="/course/business-marketing-course">Business & Marketing</a>
        </div>
      </li>
      <style>
        .nav-dropdown-wrapper {
          position: relative;
        }
        .nav-dropdown-menu {
          position: absolute;
          top: 100%;
          left: 50%;
          transform: translateX(-50%) translateY(10px);
          margin-top: 25px;
          background: rgba(15, 15, 15, 0.95);
          backdrop-filter: blur(12px);
          border: 1px solid rgba(255, 255, 255, 0.1);
          border-radius: 12px;
          padding: 8px;
          display: flex;
          flex-direction: column;
          min-width: 200px;
          opacity: 0;
          visibility: hidden;
          transition: all 0.3s ease;
          box-shadow: 0 10px 30px rgba(0,0,0,0.5);
          z-index: 200;
        }
        .nav-dropdown-menu.open {
          opacity: 1;
          visibility: visible;
          transform: translateX(-50%) translateY(0);
        }
        .nav-dropdown-menu a {
          padding: 10px 16px !important;
          color: var(--white);
          text-decoration: none;
          font-size: 13px;
          font-weight: 500;
          border-radius: 8px;
          transition: background 0.2s, opacity 0.2s;
          opacity: 0.8;
          display: block;
        }
        .nav-dropdown-menu a:hover {
          background: rgba(255, 255, 255, 0.1);
          opacity: 1;
        }
        .nav-dropdown-toggle:hover {
          opacity: 1 !important;
        }
      </style>
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          const toggleBtn = document.getElementById('desktop-courses-toggle');
          const submenu = document.getElementById('desktop-courses-submenu');
          if (toggleBtn && submenu) {
            toggleBtn.addEventListener('click', (e) => {
              e.stopPropagation();
              submenu.classList.toggle('open');
            });
            document.addEventListener('click', (e) => {
              if (!submenu.contains(e.target) && !toggleBtn.contains(e.target)) {
                submenu.classList.remove('open');
              }
            });
          }
        });
      </script>
      <li><a href="/life-at-bs.html">Life at BS</a></li>
      <li><a href="/student-alumni.html">Student Alumni</a></li>
      <li><a href="/blogs.html">Blogs</a></li>
      <li><a href="/contact.html">Contact</a></li>
    </ul>
    <div class="nav-right">
      <button class="nav-cta">Enroll Now</button>
    </div>
    <button class="hamburger" id="hamburger" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </nav>

  <div class="mobile-menu" id="mobile-menu">
    <div class="mobile-menu-header">
      <div class="nav-logo">
        <div class="brand-logo-icon">
          <div class="logo-box box-1"></div>
          <div class="logo-box box-2"></div>
          <div class="logo-box box-main">
            <div class="logo-icon-text">B<span class="small-s">s</span></div>
          </div>
        </div>
      </div>
      <button type="button" id="mobile-menu-close" style="background:none; border:none; color:var(--white); padding: 5px; cursor: pointer;">
          <svg viewBox="0 0 24 24" width="32" height="32" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
    </div>
    <div class="mobile-menu-links">
      <a href="/index.html" class="mobile-nav-item accent">Home</a>
      
      <div class="mobile-nav-dropdown-group">
        <div class="mobile-nav-item-wrap">
          <a href="/course.html" class="mobile-nav-item" id="mobile-courses-link">Courses</a>
          <button type="button" class="mobile-nav-toggle" id="mobile-courses-toggle" aria-label="Toggle Courses">
            <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
          </button>
        </div>
        <div class="mobile-submenu" id="mobile-courses-submenu">
          <a href="/course/braanding-course" class="mobile-sub-item">Brand & Design</a>
          <a href="/course/creator-course" class="mobile-sub-item">Content & Video</a>
          <a href="/course/business-marketing-course" class="mobile-sub-item">Business & Marketing</a>
        </div>
      </div>

      <a href="/life-at-bs.html" class="mobile-nav-item">Life at BS</a>
      <a href="/student-alumni.html" class="mobile-nav-item">Student Alumni</a>
      <a href="/blogs.html" class="mobile-nav-item">Blogs</a>
      <a href="/contact.html" class="mobile-nav-item">Contact</a>
      <button type="button" class="mobile-menu-cta" style="margin-top:20px;">Enroll Now</button>
    </div>
  </div>"""

modified, count = re.subn(pattern, new_navbar_markup, html)
if count > 0:
    print("Preloader and legacy header successfully replaced using regex!")
    html = modified
else:
    print("Warning: regex replacement failed. Trying fallback manual substring replacement.")
    # Fallback to direct string replacement if formatting differs slightly
    preloader_start = '<div class="site-preloader" id="preloader">'
    header_end = '</header>'
    idx_start = html.find(preloader_start)
    idx_end = html.find(header_end, idx_start) if idx_start != -1 else -1
    if idx_start != -1 and idx_end != -1:
        # Include </header>
        idx_end += len(header_end)
        html = html[:idx_start] + new_navbar_markup + html[idx_end:]
        print("Preloader and legacy header successfully replaced using manual substring indexes!")
    else:
        print("Error: Could not locate preloader/header block.")

# 3. Inject enrollment modal popup before </body>
modal_popup = """    <!-- ── ENROLLMENT POPUP ── -->
    <div id="join-popup" class="join-popup">
      <div id="close-popup-bg" class="popup-backdrop"></div>
      <div class="popup-content">
        <button class="close-popup" id="close-popup">&times;</button>
        <div class="form-chat-icon">
          <svg viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
        </div>
        <h3>Secure your spot.</h3>
        <p>Submit your details and our team will get in touch with you shortly.</p>
        <form id="enrollment-form" class="enrollment-form">
          <div class="form-group">
            <label>Full Name</label>
            <input type="text" name="name" placeholder="John Doe" required>
          </div>
          <div class="form-group">
            <label>WhatsApp Number</label>
            <input type="tel" name="phone" placeholder="+91" required>
          </div>
          <div class="form-group">
            <label>Email Address</label>
            <input type="email" name="email" placeholder="john@example.com" required>
          </div>
          <div class="form-group">
            <label>Your Goal</label>
            <textarea name="goal" placeholder="What are you looking to achieve?" required></textarea>
          </div>
          <button type="submit" class="popup-cta">Apply Now</button>
          <p class="form-disclaimer">Zero spam. Only relevant course updates.</p>
        </form>
      </div>
    </div>
  </body>"""

html = html.replace("  </body>", modal_popup)

with open("blogs.html", "w", encoding="utf-8") as f:
    f.write(html)

print("blogs.html successfully updated!")
