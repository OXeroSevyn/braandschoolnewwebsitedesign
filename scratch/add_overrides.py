# python script to add specific overrides to blogs.html (including body background grid)

with open("blogs.html", "r", encoding="utf-8") as f:
    html = f.read()

# We need to strip out the old override block if it exists, or just overwrite it.
# Let's search for "Navbar Override Styles" block and replace it cleanly.
import re
pattern = re.compile(r'<!-- Navbar Override Styles.*?/style>', re.DOTALL)
html = re.sub(pattern, '', html)

override_styles = """<!-- Navbar Override Styles to prevent theme conflicts -->
    <style>
      /* Enforce the exact neon green radial gradient and white subtle grid background */
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

      /* Reset/Override theme styles for nav components */
      nav {
        position: fixed !important;
        top: 24px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        width: calc(100% - 48px) !important;
        max-width: 1600px !important;
        border-radius: 100px !important;
        z-index: 99999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        padding: 0 40px !important;
        height: 75px !important;
        background: rgba(15, 15, 15, 0.4) !important;
        backdrop-filter: blur(24px) saturate(150%) !important;
        -webkit-backdrop-filter: blur(24px) saturate(150%) !important;
        border: none !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4) !important;
        box-sizing: border-box !important;
      }
      
      .brand-logo-icon {
        position: relative !important;
        width: 300px !important;
        height: 75px !important;
        flex-shrink: 0 !important;
        background: url('images/logo.png') center/contain no-repeat !important;
        background-position: left center !important;
        display: block !important;
      }
      
      .nav-links {
        position: absolute !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        display: flex !important;
        align-items: center !important;
        gap: 40px !important;
        list-style: none !important;
        margin: 0 !important;
        padding: 0 !important;
      }
      
      .nav-links li {
        margin: 0 !important;
        padding: 0 !important;
        list-style: none !important;
      }
      
      .nav-links a {
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        color: #f5f5f0 !important;
        text-decoration: none !important;
        opacity: 0.7 !important;
        transition: opacity 0.2s !important;
      }
      
      .nav-links a:hover {
        opacity: 1 !important;
      }
      
      .nav-right {
        display: flex !important;
        align-items: center !important;
        gap: 20px !important;
      }
      
      .nav-cta {
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
      }
      
      .nav-cta:hover {
        background: rgba(167, 254, 43, 0.15) !important;
        border-color: #a7fe2b !important;
        transform: translateY(-1px) !important;
      }
      
      /* Hamburger button */
      .hamburger {
        display: none !important;
        flex-direction: column !important;
        gap: 5px !important;
        cursor: pointer !important;
        padding: 6px !important;
        background: none !important;
        border: none !important;
        z-index: 200 !important;
      }
      
      .hamburger span {
        display: block !important;
        width: 22px !important;
        height: 1.5px !important;
        background: #f5f5f0 !important;
        transition: all 0.3s ease !important;
      }
      
      @media (max-width: 1024px) {
        .brand-logo-icon { width: 180px !important; height: 60px !important; }
        .nav-links, .nav-right { display: none !important; }
        .hamburger { display: flex !important; }
      }
      
      @media (max-width: 600px) {
        nav {
          height: 56px !important;
          padding: 0 16px !important;
          top: 16px !important;
          width: calc(100% - 32px) !important;
        }
        .brand-logo-icon {
          width: 140px !important;
          height: 48px !important;
        }
      }
    </style>
  </head>"""

# Replace in html
html = html.replace("  </head>", override_styles)

with open("blogs.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated overrides with body background style in blogs.html!")
