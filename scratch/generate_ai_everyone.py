import re

# Read UI/UX page template
with open('the-ui-ux-design-course.html', 'r', encoding='utf-8') as f:
    template = f.read()

content = template

# Replace SEO meta
content = content.replace(
    "<title>Siliguri’s Premium UI/UX Design Course | Braand School</title>",
    "<title>Siliguri’s Premium AI for Everyone Course | Braand School</title>"
)
content = content.replace(
    'content="Master UI/UX Design in just 8 weeks at Braand School Siliguri. Learn wireframing, prototyping, Figma, and build a premium design portfolio. Enroll today!"',
    'content="Learn the creative and business power of Artificial Intelligence in just 4 weeks at Braand School Siliguri. Master Midjourney, Gemini, TensorFlow, and AI marketing. Enroll now!"'
)
content = content.replace(
    'content="Siliguri’s Premium UI/UX Design Course | Braand School"',
    'content="Siliguri’s Premium AI for Everyone Course | Braand School"'
)
content = content.replace(
    'content="https://braandschool.com/courses/the-ui-ux-design-course/"',
    'content="https://braandschool.com/courses/ai-for-everyone/"'
)

# Replace Hero Content
content = content.replace(
    '<div class="ch-kicker">Interactive Design Track</div>',
    '<div class="ch-kicker">Creative Artificial Intelligence Track</div>'
)
content = content.replace(
    '<h1 class="ch-title">Master the Art of <em>UI/UX.</em></h1>',
    '<h1 class="ch-title">Master the Art of <em>AI.</em></h1>'
)
content = content.replace(
    'Learn to craft visually stunning, highly intuitive interfaces. Master wireframing, interactive prototyping, user research, and design systems using Figma. Go from visual mockups to developer-ready projects in just 8 weeks.',
    'Unlock the creative and business possibilities of Artificial Intelligence. Learn machine learning concepts, neural networks, content generation, AI storytelling, AI branding, and product design using Midjourney, Gemini, TensorFlow, and Brandwatch. No tech background needed.'
)
content = content.replace(
    '<span class="badge-text">Duration: 8 Weeks</span>',
    '<span class="badge-text">Duration: 4 Weeks</span>'
)
content = content.replace(
    '<img src="/images/explore-courses/course_ui_ux.png" alt="UI/UX Design Mockups" class="hero-render-img">',
    '<img src="/images/explore-courses/course_ai_everyone.png" alt="AI Creative Concept Illustration" class="hero-render-img">'
)

# Replace Roadmap section
old_roadmap = """      <!-- Card 1 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 01</span>
        <h3 class="rm-title">UX Research & Design Foundations</h3>
        <ul class="rm-list">
          <li>UX Design principles & User-centered design framework</li>
          <li>Conducting user research, interviews, and user personas</li>
          <li>Information Architecture (IA), user flows & site mapping</li>
          <li>Competitive analysis & heuristic evaluations</li>
        </ul>
      </div>

      <!-- Card 2 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 02</span>
        <h3 class="rm-title">Wireframing & Low-Fidelity Layouts</h3>
        <ul class="rm-list">
          <li>Paper wireframing & rapid sketching techniques</li>
          <li>Digital wireframing in Figma & establishing core layouts</li>
          <li>Grids, alignments, and spatial relationships</li>
          <li>Translating user flows into functional screen structures</li>
        </ul>
      </div>

      <!-- Card 3 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 03</span>
        <h3 class="rm-title">Figma Mastery & High-Fidelity UI</h3>
        <ul class="rm-list">
          <li>Figma interface, shortcuts, and canvas setup</li>
          <li>Working with vector shapes, masks, and boolean operations</li>
          <li>Color theory, premium palettes, and typography scales</li>
          <li>Creating premium visual elements, shadows, and blurs</li>
        </ul>
      </div>

      <!-- Card 4 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 04</span>
        <h3 class="rm-title">Advanced Components & Auto Layout</h3>
        <ul class="rm-list">
          <li>Auto Layout 5.0 constraints, paddings, and resizing rules</li>
          <li>Component properties, variants, and boolean variables</li>
          <li>Design tokens, global styles, and variable modes</li>
          <li>Creating modular responsive UI assets & components</li>
        </ul>
      </div>

      <!-- Card 5 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 05</span>
        <h3 class="rm-title">Interactive Prototyping & Motion</h3>
        <ul class="rm-list">
          <li>Smart Animate, custom easing curves, and micro-interactions</li>
          <li>Prototyping state changes (hover, click, drag, active)</li>
          <li>Multi-device interactive flows & responsive transitions</li>
          <li>Conditional variables & logical prototyping flows</li>
        </ul>
      </div>

      <!-- Card 6 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 06</span>
        <h3 class="rm-title">Design Systems & UI Libraries</h3>
        <ul class="rm-list">
          <li>Building premium scalable component libraries from scratch</li>
          <li>Atomic design methodology implementation</li>
          <li>Documentation guidelines & component usage rules</li>
          <li>State management for buttons, inputs, headers, and menus</li>
        </ul>
      </div>

      <!-- Card 7 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 07</span>
        <h3 class="rm-title">Design Presentation & Portfolio Projects</h3>
        <ul class="rm-list">
          <li>Mocking up designs inside premium mockups & renders</li>
          <li>Preparing high-end case studies for Behance & Dribbble</li>
          <li>UX writing, clean copywriting, and presentation decks</li>
          <li>Portfolio structure, resume building, and job search strategies</li>
        </ul>
      </div>

      <!-- Card 8 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 08</span>
        <h3 class="rm-title">Developer Handoff & Specifications</h3>
        <ul class="rm-list">
          <li>Figma DevMode specs, measurements, and asset exports</li>
          <li>Communication with web developers & handoff documents</li>
          <li>Redlining, layouts, design audits, and QA checking</li>
          <li>Real client brief projects & final course review</li>
        </ul>
      </div>"""

new_roadmap = """      <!-- Card 1 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 01</span>
        <h3 class="rm-title">Learning Objectives & Basics</h3>
        <ul class="rm-list">
          <li>Define Artificial Intelligence and explore its branches</li>
          <li>Understand key concepts: machine learning, deep learning, neural networks</li>
          <li>Supervised vs. Unsupervised vs. Reinforcement learning</li>
          <li>Ethical considerations surrounding AI development</li>
        </ul>
      </div>

      <!-- Card 2 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 02</span>
        <h3 class="rm-title">Introduction to AI Core Fields</h3>
        <ul class="rm-list">
          <li>Machine Learning: training algorithms without explicit coding</li>
          <li>Deep Learning: multi-layered artificial neural networks</li>
          <li>Neural Networks: interconnected processing nodes & brain models</li>
          <li>Key tools and libraries overview (TensorFlow, PyTorch, Keras)</li>
        </ul>
      </div>

      <!-- Card 3 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 03</span>
        <h3 class="rm-title">AI in Action (Content & Branding)</h3>
        <ul class="rm-list">
          <li>Storytelling: scriptwriting & characters with Gemini & Midjourney</li>
          <li>Branding: sentiment analysis with Brandwatch & trend mapping</li>
          <li>Product Design: generative ideas and structures with IBM Maximo</li>
          <li>Ethical Implications: bias in algorithms, privacy, job displacement</li>
        </ul>
      </div>

      <!-- Card 4 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 04</span>
        <h3 class="rm-title">Activities & Interactive Practice</h3>
        <ul class="rm-list">
          <li>Interactive quizzes on subfields and AI generation tools</li>
          <li>Group discussions on ethical creative solutions</li>
          <li>Guest lecture on practical real-world creative AI applications</li>
          <li>Comparing outputs between different LLMs and generative systems</li>
        </ul>
      </div>

      <!-- Card 5 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 05</span>
        <h3 class="rm-title">AI Perks & Penalty</h3>
        <ul class="rm-list">
          <li>Analyzing structural benefits vs. risks of implementation</li>
          <li>Deep dive into AI functionalities in creative workflows</li>
          <li>Case studies of AI applications in media, business, and tech</li>
          <li>Legal compliance, copyright, and IP considerations</li>
        </ul>
      </div>

      <!-- Card 6 -->
      <div class="roadmap-card">
        <span class="rm-num">Module 06</span>
        <h3 class="rm-title">Final Project & Portfolio Development</h3>
        <ul class="rm-list">
          <li>Integrating skills from all modules into a comprehensive project</li>
          <li>Building a professional design/AI implementation case study</li>
          <li>Presenting and showcasing completed projects</li>
          <li>Peer evaluations and final course grading review</li>
        </ul>
      </div>"""

content = content.replace(old_roadmap, new_roadmap)

# Replace Syllabus/Outcomes section
old_outcomes = """      <!-- Outcome Card 1 -->
      <div class="syl-card">
        <div class="syl-icon-wrapper">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="16" x2="12" y2="12"></line>
            <line x1="12" y1="8" x2="12.01" y2="8"></line>
          </svg>
        </div>
        <h3 class="syl-card-title">User Research & Personas</h3>
        <p class="syl-card-desc">
          Master target audience research, heuristic evaluations, site maps, user journeys, and wireframe documentation.
        </p>
      </div>

      <!-- Outcome Card 2 -->
      <div class="syl-card">
        <div class="syl-icon-wrapper">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="9" y1="3" x2="9" y2="21"></line>
            <line x1="15" y1="3" x2="15" y2="21"></line>
            <line x1="3" y1="9" x2="21" y2="9"></line>
            <line x1="3" y1="15" x2="21" y2="15"></line>
          </svg>
        </div>
        <h3 class="syl-card-title">Wireframing & Auto Layout</h3>
        <p class="syl-card-desc">
          Build high-performance low-fidelity digital wireframes and master Auto Layout components with ease.
        </p>
      </div>

      <!-- Outcome Card 3 -->
      <div class="syl-card">
        <div class="syl-icon-wrapper">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
          </svg>
        </div>
        <h3 class="syl-card-title">Premium Design Systems</h3>
        <p class="syl-card-desc">
          Create scalable UI kits, advanced variants, interactive components, responsive layouts, and unified color systems.
        </p>
      </div>

      <!-- Outcome Card 4 -->
      <div class="syl-card">
        <div class="syl-icon-wrapper">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
          </svg>
        </div>
        <h3 class="syl-card-title">Interactive Handoff</h3>
        <p class="syl-card-desc">
          Structure micro-animations, prototyping workflows, DevMode variables, redlines, and specifications for engineering handoff.
        </p>
      </div>"""

new_outcomes = """      <!-- Outcome Card 1 -->
      <div class="syl-card">
        <div class="syl-icon-wrapper">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
            <polyline points="2 17 12 22 22 17"></polyline>
            <polyline points="2 12 12 17 22 12"></polyline>
          </svg>
        </div>
        <h3 class="syl-card-title">Machine & Deep Learning</h3>
        <p class="syl-card-desc">
          Learn the fundamentals of how algorithms learn from data using TensorFlow, PyTorch, and Keras.
        </p>
      </div>

      <!-- Outcome Card 2 -->
      <div class="syl-card">
        <div class="syl-icon-wrapper">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 20h9M3 20v-8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2v8M12 11h.01"></path>
          </svg>
        </div>
        <h3 class="syl-card-title">Generative Content & Art</h3>
        <p class="syl-card-desc">
          Generate scripts, characters, graphics, and music using Midjourney, Gemini, and Amper Music.
        </p>
      </div>

      <!-- Outcome Card 3 -->
      <div class="syl-card">
        <div class="syl-icon-wrapper">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="16" x2="12" y2="12"></line>
            <line x1="12" y1="8" x2="12.01" y2="8"></line>
          </svg>
        </div>
        <h3 class="syl-card-title">AI Branding & Analytics</h3>
        <p class="syl-card-desc">
          Analyze consumer sentiment, predict market trends, and create unique assets with Brandwatch.
        </p>
      </div>

      <!-- Outcome Card 4 -->
      <div class="syl-card">
        <div class="syl-icon-wrapper">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
          </svg>
        </div>
        <h3 class="syl-card-title">Ethical AI & Operations</h3>
        <p class="syl-card-desc">
          Address bias, ensure privacy compliance, explore displacement, and prototype with IBM Maximo.
        </p>
      </div>"""

content = content.replace(old_outcomes, new_outcomes)

# Replace Tools section
old_tools = """    <div class="tools-grid">
      <div class="tool-card">
        <img src="/images/tools/figma.png" alt="Figma Layouts">
        <span class="tool-name">Figma</span>
      </div>
      <div class="tool-card">
        <img src="/images/tools/adobe.png" alt="Adobe XD Prototyping">
        <span class="tool-name">Adobe XD</span>
      </div>
      <div class="tool-card">
        <img src="/images/tools/adobe_photoshop.png" alt="Adobe Photoshop Graphics">
        <span class="tool-name">Photoshop</span>
      </div>
      <div class="tool-card">
        <img src="/images/tools/behance.png" alt="Behance Case Studies">
        <span class="tool-name">Behance</span>
      </div>
    </div>"""

new_tools = """    <div class="tools-grid">
      <div class="tool-card">
        <svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="var(--green)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="opacity: 0.85;">
          <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
          <polyline points="2 17 12 22 22 17"></polyline>
          <polyline points="2 12 12 17 22 12"></polyline>
        </svg>
        <span class="tool-name">TensorFlow</span>
      </div>
      <div class="tool-card">
        <svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="var(--green)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="opacity: 0.85;">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
        </svg>
        <span class="tool-name">PyTorch</span>
      </div>
      <div class="tool-card">
        <svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="var(--green)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="opacity: 0.85;">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M8 12h8M12 8v8"></path>
        </svg>
        <span class="tool-name">Midjourney</span>
      </div>
      <div class="tool-card">
        <svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="var(--green)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="opacity: 0.85;">
          <line x1="18" y1="20" x2="18" y2="10"></line>
          <line x1="12" y1="20" x2="12" y2="4"></line>
          <line x1="6" y1="20" x2="6" y2="14"></line>
        </svg>
        <span class="tool-name">Google Trends</span>
      </div>
      <div class="tool-card">
        <img src="/images/tools/adobe_creative-cloud.png" alt="Adobe Creative Cloud" style="max-height: 48px; width: auto; object-fit: contain;">
        <span class="tool-name">Creative Cloud</span>
      </div>
      <div class="tool-card">
        <img src="/images/tools/figma.png" alt="Figma Layouts" style="max-height: 48px; width: auto; object-fit: contain;">
        <span class="tool-name">Figma</span>
      </div>
    </div>"""

content = content.replace(old_tools, new_tools)

# Replace FAQs section
old_faqs = """      <!-- Question 1 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-1">
          <span class="faq-question">What sets this course apart from others?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-1" hidden>
          <div class="faq-answer-content">
            Our course goes beyond just graphic design – it covers a range of design disciplines, from Social Media, Print, Video Editing & Motion, AR/VR and even Podcasting, equipping you with a diverse skill set. Plus, our practical approach ensures yo u're industry-ready. Throughout the course, you'll work on real-world projects and assignments. This practical approach ensures you not only learn but also apply your knowledge to build a killer portfolio that showcases your talents.
          </div>
        </div>
      </div>

      <!-- Question 2 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-2">
          <span class="faq-question">What exactly will I learn in this course?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-2" hidden>
          <div class="faq-answer-content">
            This course is a comprehensive journey covering graphic design, UI/UX design, AR/VR design, video editing, after effects, podcasting, and more. You'll master design principles, color theory, typography, layout, and also learn to use cutting-edge software and AI tools for creating stunning graphics and interactive experiences.
          </div>
        </div>
      </div>

      <!-- Question 3 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-3">
          <span class="faq-question">What are the requirements to join the course?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-3" hidden>
          <div class="faq-answer-content">
            All you need is enthusiasm and a laptop of your own. Bring your creative energy, and we'll guide you through the rest!
          </div>
        </div>
      </div>

      <!-- Question 4 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-4">
          <span class="faq-question">What kind of support will I get after completing the course?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-4" hidden>
          <div class="faq-answer-content">
            We've got your back! Our dedicated placement cell will help you connect with potential job opportunities in the design industry. Your success is our goal even after you graduate.
          </div>
        </div>
      </div>

      <!-- Question 5 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-5">
          <span class="faq-question">Can I pay the fee in installments?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-5" hidden>
          <div class="faq-answer-content">
            Absolutely! We understand the importance of flexibility. You can fill up the form on our website and reach out to our team for more details about our fees installment options. We're here to make it work for you!
          </div>
        </div>
      </div>

      <!-- Question 6 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-6">
          <span class="faq-question">What is Braand School?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-6" hidden>
          <div class="faq-answer-content">
            Braand School is an institute located in Siliguri. We specialize in teaching marketing, branding, and business courses tailored for North Bengal. Our focus is to provide affordable education with practical experiences, emphasizing real client projects.
          </div>
        </div>
      </div>"""

new_faqs = """      <!-- Question 1 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-1">
          <span class="faq-question">What sets this course apart from others?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-1" hidden>
          <div class="faq-answer-content">
            Our course is specifically tailored to creative practitioners, writers, designers, and business owners. Instead of complex math and programming, we focus on the practical application of AI tools in design, branding, content generation, and product prototyping, making it accessible to everyone.
          </div>
        </div>
      </div>

      <!-- Question 2 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-2">
          <span class="faq-question">What exactly will I learn in this course?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-2" hidden>
          <div class="faq-answer-content">
            You'll learn the core concepts of Machine Learning and Deep Learning, generative AI storytelling, image generation with Midjourney, AI analytics with Brandwatch, trend prediction with Google Trends, and ethical guidelines for responsible AI usage.
          </div>
        </div>
      </div>

      <!-- Question 3 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-3">
          <span class="faq-question">What are the requirements to join the course?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-3" hidden>
          <div class="faq-answer-content">
            All you need is enthusiasm and a laptop of your own. Bring your creative energy, and we'll guide you through the rest!
          </div>
        </div>
      </div>

      <!-- Question 4 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-4">
          <span class="faq-question">What kind of support will I get after completing the course?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-4" hidden>
          <div class="faq-answer-content">
            We've got your back! Our dedicated placement cell will help you connect with potential job opportunities in design and technology industries. Your success is our goal even after you graduate.
          </div>
        </div>
      </div>

      <!-- Question 5 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-5">
          <span class="faq-question">Can I pay the fee in installments?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-5" hidden>
          <div class="faq-answer-content">
            Absolutely! We understand the importance of flexibility. You can fill up the form on our website and reach out to our team for more details about our fees installment options. We're here to make it work for you!
          </div>
        </div>
      </div>

      <!-- Question 6 -->
      <div class="faq-item">
        <button class="faq-trigger" aria-expanded="false" aria-controls="faq-ans-6">
          <span class="faq-question">What is Braand School?</span>
          <span class="faq-icon-indicator"></span>
        </button>
        <div class="faq-answer-panel" id="faq-ans-6" hidden>
          <div class="faq-answer-content">
            Braand School is an institute located in Siliguri. We specialize in teaching marketing, branding, and business courses tailored for individuals in North Bengal. Our focus is to provide affordable education with practical experiences, emphasizing real client projects.
          </div>
        </div>
      </div>"""

content = content.replace(old_faqs, new_faqs)

# Replace form parameters or labels
content = content.replace('UI/UX Design Course Syllabus', 'AI for Everyone Course Syllabus')
content = content.replace(
    '<input type="hidden" name="Course" value="UI/UX Design Course">',
    '<input type="hidden" name="Course" value="AI for Everyone Course">'
)

# Write output to ai-for-everyone.html
with open('ai-for-everyone.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated ai-for-everyone.html successfully!")
