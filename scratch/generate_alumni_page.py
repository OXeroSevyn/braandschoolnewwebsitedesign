import json
import os

# Load parsed student data
with open(r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\scratch\parsed_students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

# Load footer styling
with open(r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\scratch\clean_footer_css.css", "r", encoding="utf-8") as f:
    footer_css = f.read()

# SVG Icons dictionary
SVG_ICONS = {
    "linkedin": '<svg viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.779-1.75-1.75s.784-1.75 1.75-1.75 1.75.779 1.75 1.75-.784 1.75-1.75 1.75zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>',
    "behance": '<svg viewBox="0 0 24 24"><path d="M22 14.05h-7c.04 1.77 1.29 2.5 2.91 2.5 1.21 0 2.22-.5 2.78-1.42h2c-.67 2-2.58 3.42-4.78 3.42-3.8 0-6.13-2.67-6.13-6.05s2.34-6.05 6-6.05c3.54 0 5.8 2.53 5.8 5.75-.02.43-.07.83-.58.85zm-7-2.05h4.74c-.09-1.52-1.12-2.31-2.34-2.31-1.34 0-2.27.79-2.4 2.31zm-10 6.05h-3.5v-13h3.75c2.34 0 3.75 1.08 3.75 2.92 0 1.25-.66 2.08-1.75 2.5 1.34.33 2.25 1.33 2.25 2.75-.05 2.25-1.84 4.83-4.5 4.83zm-1.5-7.5h1.25c1.08 0 1.75-.42 1.75-1.25s-.67-1.25-1.75-1.25h-1.25v2.5zm0 5h1.5c1.08 0 1.75-.5 1.75-1.42s-.67-1.42-1.75-1.42h-1.5v2.84zm14.5-9.05h5v1.5h-5v-1.5z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24"><path d="M23.498 6.163c-.272-.997-1.077-1.782-2.102-2.053C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.396.61c-1.025.271-1.83 1.056-2.102 2.053C0 8.028 0 12 0 12s0 3.972.502 5.837c.272.997 1.077 1.782 2.102 2.053C4.5 20.5 12 20.5 12 20.5s7.5 0 9.396-.61c1.025-.271 1.83-1.056 2.102-2.053C24 15.972 24 12 24 12s0-3.972-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>',
    "website": '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.53c-.26-.81-1-1.4-1.9-1.4h-1v-3c0-.55-.45-1-1-1h-6v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.4z"/></svg>',
    "social": '<svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zm0 10.162a3.999 3.999 0 1 1 0-7.998 3.999 3.999 0 0 1 0 7.998zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>'
}

def get_link_svg(label):
    lbl = label.lower()
    if "linkedin" in lbl:
        return SVG_ICONS["linkedin"]
    elif "behance" in lbl:
        return SVG_ICONS["behance"]
    elif "youtube" in lbl:
        return SVG_ICONS["youtube"]
    elif "website" in lbl:
        return SVG_ICONS["website"]
    else:
        return SVG_ICONS["social"]

# Rebuild the HTML content of student-alumni.html
html = """<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>2025 Batch - Braand School</title>
    
    <!-- SEO Framework Meta -->
    <meta name="robots" content="max-snippet:-1,max-image-preview:large,max-video-preview:-1" />
    <link rel="canonical" href="https://braandschool.com/2025-batch/" />
    <meta name="description" content="Meet the exceptionally talented student alumni of Braand School, Cohort of 2025. Explore their portfolios across branding, marketing, design, and video." />
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&family=Caveat:wght@400;600;700&display=swap" rel="stylesheet">
    
    <!-- Shared Resources -->
    <link rel="stylesheet" href="assets/css/main.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
    <script src="assets/js/main.js" defer></script>
    <style>
      /* --- BACKGROUND SYSTEM OVERRIDES --- */
      body {
        background-color: #050505 !important;
        background-image: 
          radial-gradient(circle at 50% 30%, rgba(167, 254, 43, 0.16) 0%, rgba(167, 254, 43, 0.03) 45%, transparent 70%),
          linear-gradient(to right, rgba(255, 255, 255, 0.07) 1px, transparent 1px),
          linear-gradient(to bottom, rgba(255, 255, 255, 0.07) 1px, transparent 1px) !important;
        background-size: 100% 1000px, 24px 24px, 24px 24px !important;
        background-repeat: no-repeat, repeat, repeat !important;
        background-attachment: scroll, fixed, fixed !important;
        position: relative;
      }

      /* --- ALUMNI PAGE STYLES --- */
      .alumni-hero {
        text-align: center;
        padding: 160px 20px 60px;
        max-width: 900px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
      }
      .alumni-hero h1 {
        font-size: clamp(2.8rem, 6vw, 4.8rem);
        font-weight: 800;
        line-height: 1.1;
        letter-spacing: -0.03em;
        margin-bottom: 20px;
        color: #fff;
      }
      .alumni-hero h1 em {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        color: var(--green);
        font-weight: 400;
      }
      .alumni-hero p {
        font-size: clamp(15px, 1.8vw, 17px);
        line-height: 1.6;
        color: rgba(255, 255, 255, 0.6);
        max-width: 620px;
        margin: 0 auto;
      }
      .hero-kicker {
        font-family: var(--font-mono);
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: var(--green);
        margin-bottom: 16px;
        display: inline-block;
      }

      /* Filter & Search Bar */
      .controls-panel {
        max-width: 1200px;
        margin: 0 auto 50px;
        padding: 0 24px;
        display: flex;
        flex-direction: column;
        gap: 24px;
        align-items: center;
        position: relative;
        z-index: 2;
      }
      
      .search-wrapper {
        position: relative;
        width: 100%;
        max-width: 440px;
      }
      .search-wrapper input {
        width: 100%;
        background: rgba(15, 15, 15, 0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.16);
        border-radius: 100px;
        padding: 14px 20px 14px 48px;
        color: var(--white);
        font-family: var(--font-display);
        font-size: 14px;
        transition: all 0.3s ease;
        outline: none;
      }
      .search-wrapper input::placeholder {
        color: rgba(255, 255, 255, 0.5);
        opacity: 1;
      }
      .search-wrapper input:focus {
        border-color: rgba(167, 254, 43, 0.6);
        background: rgba(20, 20, 20, 0.95);
        box-shadow: 0 0 20px rgba(167, 254, 43, 0.15);
      }
      .search-icon {
        position: absolute;
        left: 18px;
        top: 50%;
        transform: translateY(-50%);
        width: 16px;
        height: 16px;
        stroke: rgba(255, 255, 255, 0.6);
        fill: none;
        pointer-events: none;
        transition: stroke 0.3s;
      }
      .search-wrapper input:focus + .search-icon {
        stroke: var(--green);
      }

      /* Course Filters */
      .filter-pills {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
      }
      .filter-pill {
        font-family: var(--font-mono);
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: rgba(255, 255, 255, 0.5);
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 100px;
        padding: 8px 18px;
        cursor: pointer;
        transition: all 0.3s ease;
        outline: none;
      }
      .filter-pill:hover, .filter-pill.active {
        color: var(--black);
        background: var(--green);
        border-color: var(--green);
        box-shadow: 0 6px 15px rgba(167, 254, 43, 0.2);
      }

      /* Student Grid & Cards */
      .students-container {
        max-width: 900px;
        margin: 0 auto 100px;
        padding: 0 24px;
        position: relative;
        z-index: 2;
      }
      .students-grid {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 40px;
        width: 100%;
      }
      
      .student-card {
        background: #fdfdfd;
        border: 1px solid rgba(0, 0, 0, 0.15);
        border-radius: 16px;
        padding: 32px;
        display: flex;
        flex-direction: row;
        align-items: stretch;
        justify-content: space-between;
        gap: 32px;
        width: 100%;
        max-width: 780px;
        min-height: 360px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
        color: #111111;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.35);
      }
      
      .student-card:hover {
        transform: translateY(-6px);
        border-color: var(--green);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.55), 0 0 30px rgba(167, 254, 43, 0.3);
      }

      .card-left {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
      }

      .card-brand {
        font-family: var(--font-mono);
        font-size: 14px;
        font-weight: 800;
        letter-spacing: 0.1em;
        color: #111;
        border-bottom: 2.5px solid #111;
        padding-bottom: 8px;
        margin-bottom: 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }

      .card-brand span {
        font-size: 9px;
        font-weight: 700;
        background: #111;
        color: var(--green);
        padding: 3px 8px;
        border-radius: 2px;
      }

      .student-signature {
        font-family: 'Caveat', cursive;
        font-size: 48px;
        font-weight: 600;
        color: #111;
        opacity: 0.95;
        margin: 12px 0 20px -4px;
        transform: rotate(-2.5deg);
        transform-origin: left center;
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden;
      }

      .detail-grid {
        display: flex;
        flex-direction: column;
        gap: 8px;
        margin-bottom: 8px;
      }

      .detail-row {
        display: flex;
        font-size: 12px;
        line-height: 1.5;
      }

      .detail-label {
        font-family: var(--font-mono);
        font-weight: 700;
        color: #666;
        width: 100px;
        flex-shrink: 0;
      }

      .detail-val {
        font-family: var(--font-display);
        font-weight: 600;
        color: #111;
        text-transform: uppercase;
      }

      /* Right Side: Portrait */
      .card-right {
        width: 200px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        border-left: 1px dashed rgba(0, 0, 0, 0.2);
        padding-left: 32px;
        flex-shrink: 0;
      }

      .card-badge-header {
        font-family: var(--font-mono);
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 0.1em;
        color: #666;
        text-transform: uppercase;
        margin-bottom: 12px;
        text-align: center;
      }

      .student-img-wrapper {
        width: 168px;
        height: 218px;
        border-radius: 8px;
        overflow: hidden;
        border: 1.5px solid #111;
        background: #eaeaea;
        position: relative;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      }

      .student-img-wrapper img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
      }

      .portrait-caption {
        font-family: var(--font-mono);
        font-size: 8px;
        color: #777;
        margin-top: 8px;
        margin-bottom: 16px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
      }

      .student-links {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        width: 100%;
      }

      .student-link {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: transparent;
        border: 1px solid rgba(0, 0, 0, 0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #111;
        transition: all 0.3s ease;
        text-decoration: none;
        flex-shrink: 0;
      }

      .student-link:hover {
        background: #111;
        color: var(--green);
        border-color: #111;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
      }

      .student-link svg {
        width: 14px;
        height: 14px;
        fill: currentColor;
        flex-shrink: 0;
      }

      /* Empty state */
      .no-results {
        text-align: center;
        padding: 50px 20px;
        color: rgba(255, 255, 255, 0.4);
        font-size: 15px;
        display: none;
        width: 100%;
      }


      @media (max-width: 500px) {
        .students-grid {
          grid-template-columns: 1fr;
        }
        .student-card {
          flex-direction: column;
          align-items: stretch;
          gap: 24px;
        }
        .card-right {
          border-left: none;
          border-top: 1px dashed rgba(0, 0, 0, 0.2);
          padding-left: 0;
          padding-top: 20px;
          width: 100%;
          flex-direction: row;
          justify-content: space-between;
          align-items: center;
        }
        .student-img-wrapper {
          width: 80px;
          height: 105px;
        }
        .portrait-caption {
          display: none;
        }
        .student-links {
          width: auto;
        }
      }


      /* --- OVERRIDE BUTTON CONFLICTS --- */
      nav .nav-cta {
        font-family: 'Space Mono', monospace !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        color: #a7fe2b !important;
        background: rgba(167, 254, 43, 0.08) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        padding: 8px 24px !important;
        border: 1px solid rgba(167, 254, 43, 0.3) !important;
        border-radius: 100px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        display: inline-block !important;
        box-shadow: none !important;
        height: auto !important;
        line-height: normal !important;
      }
      nav .nav-cta:hover {
        background: rgba(167, 254, 43, 0.15) !important;
        border-color: #a7fe2b !important;
        transform: translateY(-1px) !important;
        color: #a7fe2b !important;
      }
      
      /* FOOTER_CSS_PLACEHOLDER */
    </style>
  </head>
  
  <body>
    <!-- Unified Background System -->
    <div class="bg-system">
      <div class="bg-glow"></div>
      <div class="bg-pattern"></div>
      <div class="bg-vignette"></div>
    </div>

    <!-- ── NAV ── -->
    <nav>
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

    <!-- Mobile Navigation Menu -->
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
    </div>

    <!-- ── HERO ── -->
    <header class="alumni-hero">
      <span class="hero-kicker">Alumni</span>
      <h1>2025 Batch<br><em>Student Showcase.</em></h1>
      <p>Meet the exceptionally talented student alumni of Braand School. Browse through their profiles, explore their professional roles, and connect directly with their portfolios.</p>
    </header>

    <!-- ── CONTROLS PANEL (FILTER/SEARCH) ── -->
    <section class="controls-panel">
      <!-- Search -->
      <div class="search-wrapper">
        <input type="text" id="student-search" placeholder="Search by name, role, or location...">
        <svg class="search-icon" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      </div>

      <!-- Course Pills -->
      <div class="filter-pills">
        <button class="filter-pill active" data-filter="all">All Courses</button>
        <button class="filter-pill" data-filter="Branding Course">Branding Course</button>
        <button class="filter-pill" data-filter="Ultimate Design Course">Ultimate Design Course</button>
        <button class="filter-pill" data-filter="Creator Course">Creator Course</button>
        <button class="filter-pill" data-filter="Digital Marketing">Digital Marketing</button>
        <button class="filter-pill" data-filter="Graphic Design">Graphic Design</button>
      </div>
    </section>

    <!-- ── STUDENTS CONTAINER ── -->
    <main class="students-container">
      <div class="students-grid" id="students-grid">
"""

# Build student cards
for idx, s in enumerate(students):
    name = s["name"]
    role = s["role"] if s["role"] != "NA" else "Creative Professional"
    image = s["image"]
    course = s["course"]
    location = s["location"]
    member_no = f"BS-25{idx+1:02d}"
    
    # Generate link buttons
    links_html = ""
    for link in s["links"]:
        lbl = link["label"]
        url = link["url"]
        svg = get_link_svg(lbl)
        links_html += f'          <a href="{url}" target="_blank" rel="noopener" class="student-link" title="{lbl}">{svg}</a>\n'

    # Filter Course Data-Attribute Heuristic matching
    filter_course = "other"
    c_lower = course.lower()
    if "brand" in c_lower:
        filter_course = "Branding Course"
    elif "ultimate" in c_lower:
        filter_course = "Ultimate Design Course"
    elif "creator" in c_lower:
        filter_course = "Creator Course"
    elif "marketing" in c_lower:
        filter_course = "Digital Marketing"
    elif "graphic" in c_lower:
        filter_course = "Graphic Design"

    card_html = f"""        <!-- Student Card: {name} -->
        <div class="student-card" data-course="{filter_course}" data-name="{name.lower()}" data-role="{role.lower()}" data-location="{location.lower()}">
          
          <!-- Left side details -->
          <div class="card-left">
            <div class="card-brand">
              BRAAND SCHOOL<sup>&reg;</sup>
              <span>2025</span>
            </div>
            
            <div class="student-signature">{name}</div>
            
            <div class="detail-grid">
              <div class="detail-row">
                <span class="detail-label">NAME</span>
                <span class="detail-val">{name}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">MEMBER NO</span>
                <span class="detail-val">{member_no}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">COURSE</span>
                <span class="detail-val">{course}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">ROLE</span>
                <span class="detail-val">{role}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">LOCATION</span>
                <span class="detail-val">{location}</span>
              </div>
            </div>
          </div>

          <!-- Right side portrait & socials -->
          <div class="card-right">
            <div class="card-badge-header">ALUMNI PASS</div>
            <div class="student-img-wrapper">
              <img src="{image}" alt="{name}" loading="lazy">
            </div>
            <div class="portrait-caption">Frontal View</div>
            <div class="student-links">
{links_html}            </div>
          </div>
          
        </div>
"""
    html += card_html

# End grid, add no-results message, add footer, add scripts and close tags
html += """        <!-- No results template -->
        <div class="no-results" id="no-results">
          No students found matching your criteria.
        </div>
      </div>
    </main>

    <!-- ── FOOTER ── -->
    <footer class="unified-footer-wrapper">
      <div class="footer-bg-container"></div>
      <div class="footer-card" style="position: relative; z-index: 2; padding: 0;">
        <div class="premium-footer-bento">
          
          <!-- Brand Bento -->
          <div class="bento-box footer-brand-bento">
            <div class="brand-logo-icon" style="transform: scale(1.8); transform-origin: left center; margin-bottom: 36px;">
              <div class="logo-box box-1"></div>
              <div class="logo-box box-2"></div>
              <div class="logo-box box-main">
                <div class="logo-icon-text">B<span class="small-s">s</span></div>
              </div>
            </div>
            <h3 class="pf-mission">The outcome-first school for the next generation of creative practitioners.</h3>
            <p class="pf-desc">Run by active practitioners, structured around real client work.</p>
            
            <div class="pf-socials">
              <a href="https://www.instagram.com/braandschool/" target="_blank" class="pf-social-btn"><svg viewBox="0 0 24 24" stroke="currentColor" fill="none"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
              <a href="https://www.linkedin.com/school/braandschool/posts/?feedView=all" target="_blank" class="pf-social-btn"><svg viewBox="0 0 24 24" stroke="currentColor" fill="none"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
              <a href="https://www.youtube.com/@braandschool" target="_blank" class="pf-social-btn"><svg viewBox="0 0 24 24" stroke="currentColor" fill="none"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg></a>
              <a href="https://wa.me/919083596000" target="_blank" class="pf-social-btn"><svg viewBox="0 0 24 24" stroke="currentColor" fill="none"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg></a>
            </div>
          </div>

          <!-- Links Bento -->
          <div class="bento-box footer-links-bento">
            <div class="pf-nav-col">
              <div class="pf-nav-header">Programs</div>
              <a href="course.html" onclick="sessionStorage.setItem('selected-course', 'braanding');" class="pf-link">Brand Design</a>
              <a href="course.html" onclick="sessionStorage.setItem('selected-course', 'marketing');" class="pf-link">Marketing Strategy</a>
              <a href="course.html" onclick="sessionStorage.setItem('selected-course', 'creator');" class="pf-link">Content Creation</a>
              <a href="course.html" onclick="sessionStorage.setItem('selected-course', 'creator');" class="pf-link">Motion & Video</a>
            </div>
            <div class="pf-nav-col">
              <div class="pf-nav-header">School</div>
              <a href="index.html#manifesto" class="pf-link">Manifesto</a>
              <a href="index.html#testimonials" class="pf-link">Testimonials</a>
              <a href="index.html#faq" class="pf-link">FAQ</a>
              <a href="index.html#apply" class="pf-link" style="color: var(--green);">Apply Now <span class="pf-arr">↗</span></a>
            </div>
          </div>

          <!-- Contact Bento -->
          <div class="bento-box footer-contact-bento">
            <div class="pf-nav-header">Contact</div>
            <div class="pf-contact-item">
              <div class="pf-contact-icon">
                <svg viewBox="0 0 24 24" stroke="currentColor" fill="none"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              </div>
              <div class="pf-contact-text">
                <span class="pf-contact-label">Call Us</span>
                <a href="tel:+919083596000">+91 90835-96000</a>
              </div>
            </div>
            <div class="pf-contact-item">
              <div class="pf-contact-icon">
                <svg viewBox="0 0 24 24" stroke="currentColor" fill="none"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              </div>
              <div class="pf-contact-text">
                <span class="pf-contact-label">Email Us</span>
                <a href="mailto:hello@braandschool.com">hello@braandschool.com</a>
              </div>
            </div>
            <div class="pf-contact-item">
              <div class="pf-contact-icon">
                <svg viewBox="0 0 24 24" stroke="currentColor" fill="none"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              </div>
              <div class="pf-contact-text">
                <span class="pf-contact-label">Address</span>
                <span>2nd Floor, Pradhan Bldg,<br>Siliguri, WB 734001</span>
              </div>
            </div>
          </div>

        </div>

        <div class="pf-footer-bottom">
          <div class="pf-fb-left">© 2026 Braand School · All rights reserved</div>
          <div class="pf-fb-right">
            <a href="index.html#apply" class="footer-apply-btn" style="background: var(--green); color: #000; padding: 12px 16px 12px 24px; border-radius: 100px; font-weight: 800; font-size: 14px; text-transform: uppercase; letter-spacing: 0.05em; display: inline-flex; align-items: center; gap: 12px; text-decoration: none; transition: transform 0.3s ease;">
              Request Admission
              <span class="btn-badge" style="display: inline-block; background: #000; color: var(--green); padding: 8px 16px; border-radius: 100px; font-size: 11px; font-weight: 800;">APPLY</span>
            </a>
          </div>
        </div>
      </div>
    </footer>

    <!-- ── ENROLLMENT POPUP ── -->
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

    <!-- ── SEARCH / FILTER JS LOGIC ── -->
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        const searchInput = document.getElementById('student-search');
        const filterPills = document.querySelectorAll('.filter-pill');
        const studentCards = document.querySelectorAll('.student-card');
        const noResults = document.getElementById('no-results');

        let currentFilter = 'all';
        let currentSearch = '';

        function filterStudents() {
          let visibleCount = 0;
          studentCards.forEach(card => {
            const course = card.getAttribute('data-course');
            const name = card.getAttribute('data-name');
            const role = card.getAttribute('data-role');
            const location = card.getAttribute('data-location');

            const matchesFilter = (currentFilter === 'all' || course === currentFilter);
            const matchesSearch = (
              name.includes(currentSearch) ||
              role.includes(currentSearch) ||
              location.includes(currentSearch) ||
              course.toLowerCase().includes(currentSearch)
            );

            if (matchesFilter && matchesSearch) {
              card.style.display = 'flex';
              visibleCount++;
            } else {
              card.style.display = 'none';
            }
          });

          if (visibleCount === 0) {
            noResults.style.display = 'block';
          } else {
            noResults.style.display = 'none';
          }
        }

        // Search Input listener
        searchInput.addEventListener('input', (e) => {
          currentSearch = e.target.value.toLowerCase().trim();
          filterStudents();
        });

        // Filter Pills listener
        filterPills.forEach(pill => {
          pill.addEventListener('click', () => {
            filterPills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            currentFilter = pill.getAttribute('data-filter');
            filterStudents();
          });
        });
      });
    </script>
  </body>
</html>
"""

# Replace placeholder with dynamic CSS content
html = html.replace("/* FOOTER_CSS_PLACEHOLDER */", footer_css)

with open(r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\student-alumni.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Redesigned student-alumni.html successfully generated!")
