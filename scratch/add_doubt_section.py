with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find the end of testimonials styles (ends around line 4805)
insert_idx = -1
for idx, line in enumerate(lines):
    # Testimonials styles has .fg-header, .fg-stage, etc.
    # Let's search from line 4200 onwards for the closing </style> tag that ends the testimonials style.
    if idx >= 4200 and "</style>" in line:
        # Check if this </style> tag belongs to the testimonials section
        # The next block starts with authorized-section styles.
        if idx + 2 < len(lines) and "/*  AUTHORIZED SECTION" in lines[idx + 2]:
            insert_idx = idx
            break

if insert_idx == -1:
    # Fallback search
    for idx, line in enumerate(lines):
        if idx >= 4790 and idx <= 4815 and "</style>" in line:
            insert_idx = idx
            break

if insert_idx == -1:
    print("Could not find insert index!")
    exit(1)

print(f"Found insert index at line {insert_idx+1}: {repr(lines[insert_idx])}")

doubt_section_content = """
  <!-- ── DOUBT & CONTACT SECTION ── -->
  <section class="doubt-section reveal" id="doubt-section">
    <div class="doubt-container">
      <div class="doubt-content">
        <h2 class="doubt-title">Still in doubts?</h2>
        <p class="doubt-text">Speak directly with our learning advisors or visit our creative hub in person.</p>
        
        <div class="doubt-actions">
          <!-- Call Us Now Card -->
          <a href="tel:+919083596000" class="doubt-card call-card">
            <div class="doubt-icon-box">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="doubt-icon">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 9.92z"></path>
              </svg>
            </div>
            <div class="doubt-card-text">
              <span class="doubt-card-lbl">CALL US NOW</span>
              <span class="doubt-card-val">+91 90835 96000</span>
            </div>
          </a>

          <!-- Visit Campus Button -->
          <a href="contact.html" class="doubt-btn-campus">
            Visit our Campus
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
          </a>
        </div>
      </div>
    </div>
  </section>

  <style>
    .doubt-section {
      background-color: #060808;
      background-image: linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
      background-size: 24px 24px;
      padding: 80px 40px;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      position: relative;
      overflow: hidden;
      z-index: 10;
    }
    
    .doubt-container {
      max-width: 1200px;
      margin: 0 auto;
      position: relative;
      z-index: 2;
    }
    
    .doubt-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 24px;
    }
    
    .doubt-title {
      font-size: clamp(32px, 5vw, 48px);
      font-weight: 800;
      color: #fff;
      letter-spacing: -0.02em;
      margin: 0;
    }
    
    .doubt-text {
      font-size: clamp(14px, 1.8vw, 17px);
      color: rgba(255, 255, 255, 0.6);
      max-width: 600px;
      margin: 0;
      line-height: 1.5;
    }
    
    .doubt-actions {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 24px;
      margin-top: 16px;
      flex-wrap: wrap;
      width: 100%;
    }
    
    .doubt-card {
      display: flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 16px 28px;
      gap: 16px;
      text-decoration: none;
      transition: all 0.3s ease;
      box-shadow: 0 4px 20px rgba(0,0,0,0.2);
      height: 80px;
      box-sizing: border-box;
    }
    
    .doubt-card:hover {
      background: rgba(255, 255, 255, 0.06);
      border-color: var(--green);
      transform: translateY(-2px);
    }
    
    .doubt-icon-box {
      width: 48px;
      height: 48px;
      background: linear-gradient(135deg, #d4ff70, #90F412);
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #000;
      box-shadow: inset 0 2px 4px rgba(255,255,255,0.4);
    }
    
    .doubt-icon {
      width: 22px;
      height: 22px;
      stroke: #1b2f02;
    }
    
    .doubt-card-text {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 3px;
    }
    
    .doubt-card-lbl {
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      color: var(--green);
      letter-spacing: 0.1em;
    }
    
    .doubt-card-val {
      font-size: 18px;
      font-weight: 700;
      color: #fff;
    }
    
    .doubt-btn-campus {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: var(--green);
      color: #000;
      padding: 20px 36px;
      border-radius: 100px;
      text-decoration: none;
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      transition: all 0.3s ease;
      height: 80px;
      box-sizing: border-box;
      justify-content: center;
    }
    
    .doubt-btn-campus:hover {
      background: #b6ff2f;
      transform: translateY(-2px);
      box-shadow: 0 0 30px rgba(167, 254, 43, 0.2);
    }

    @media (max-width: 768px) {
      .doubt-section {
        padding: 60px 24px;
      }
      .doubt-actions {
        flex-direction: column;
        gap: 16px;
      }
      .doubt-card, .doubt-btn-campus {
        width: 100%;
        justify-content: center;
      }
      .doubt-btn-campus {
        height: auto;
        padding: 18px 24px;
      }
    }
  </style>
"""

# Insert right after insert_idx
final_lines = lines[:insert_idx+1] + [doubt_section_content] + lines[insert_idx+1:]

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(final_lines)

print("Successfully inserted the Doubt section!")
