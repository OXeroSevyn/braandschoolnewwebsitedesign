/* BRAAND SCHOOL - MAIN SCRIPTS */

document.addEventListener('DOMContentLoaded', () => {
  // ─── SMOOTH SCROLL (LENIS) ───
  if (typeof Lenis !== 'undefined') {
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: 'vertical',
      gestureOrientation: 'vertical',
      smoothWheel: true,
      wheelMultiplier: 1,
      smoothTouch: true,
      touchMultiplier: 1.5,
      infinite: false,
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    // Track anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          lenis.scrollTo(target, { offset: -120 });
        }
      });
    });

    window.lenis = lenis;
  }

  // ─── MOBILE MENU ───
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      const isOpen = hamburger.classList.toggle('open');
      mobileMenu.classList.toggle('open', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    mobileMenu.querySelectorAll('a, button').forEach(el => {
      el.addEventListener('click', (e) => {
        // Do not close if clicking the courses toggle or the courses link itself
        if (el.id === 'mobile-courses-link' || el.classList.contains('mobile-nav-toggle') || el.closest('.mobile-nav-toggle')) {
          return;
        }
        hamburger.classList.remove('open');
        mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  // ─── JOIN POPUP ───
  const popup = document.getElementById('join-popup');
  const closeBtn = document.getElementById('close-popup');
  const popupBg = document.getElementById('close-popup-bg');
  
  if (popup && closeBtn) {
    // Auto-open after 4s if not closed previously
    setTimeout(() => {
      if (!sessionStorage.getItem('join-popup-closed')) {
        popup.style.display = 'flex';
        // Small delay to allow display:flex to apply before adding active class
        setTimeout(() => popup.classList.add('active'), 10);
      }
    }, 4000);

    const closePopup = () => {
      popup.classList.remove('active');
      sessionStorage.setItem('join-popup-closed', 'true');
      setTimeout(() => {
        popup.style.display = 'none';
      }, 500); // Wait for transition
    };

    // Close button logic
    closeBtn.addEventListener('click', closePopup);
    
    // Close on background click
    if (popupBg) {
      popupBg.addEventListener('click', closePopup);
    }

    // Manually open popup on Enroll Now button click
    const enrollBtns = document.querySelectorAll('.nav-cta, .mobile-menu-cta, .enroll-btn');
    enrollBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault(); // Prevent default link behavior if it's an 'a' tag
        
        // If mobile menu is open, close it
        const mobileMenu = document.getElementById('mobile-menu');
        const hamburger = document.getElementById('hamburger');
        if (mobileMenu && mobileMenu.classList.contains('open')) {
          mobileMenu.classList.remove('open');
          if (hamburger) hamburger.classList.remove('open');
          document.body.style.overflow = '';
        }

        // Open popup
        popup.style.display = 'flex';
        // Small delay to allow display:flex to apply before adding active class
        setTimeout(() => {
          popup.classList.add('active');
        }, 10);
      });
    });
    
    // Prevent form default submission for now
    const enrollForm = document.getElementById('enrollment-form');
    if (enrollForm) {
      enrollForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const submitBtn = enrollForm.querySelector('.popup-cta');
        const originalText = submitBtn.innerText;
        submitBtn.innerText = 'Application Sent ✓';
        submitBtn.style.background = 'var(--white)';
        
        setTimeout(() => {
          closePopup();
          setTimeout(() => {
            submitBtn.innerText = originalText;
            submitBtn.style.background = 'var(--green)';
            enrollForm.reset();
          }, 500);
        }, 2000);
      });
    }
  }

  // ─── REVEAL ANIMATION OBSERVER ───
  const revealElements = document.querySelectorAll('.reveal');
  if (revealElements.length > 0 && typeof anime !== 'undefined') {
    const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          anime({
            targets: entry.target,
            translateY: [30, 0],
            opacity: [0, 1],
            duration: 1000,
            easing: 'cubicBezier(0.16, 1, 0.3, 1)'
          });
          revealObserver.unobserve(entry.target);
        }
      });
    }, observerOptions);

    revealElements.forEach(el => revealObserver.observe(el));
  }
});

// Helper for navigation between pages with section focus
window.navigateToSection = (page, sectionId) => {
    if (window.location.pathname.endsWith(page)) {
        const target = document.getElementById(sectionId);
        if (target && window.lenis) {
            window.lenis.scrollTo(target, { offset: -120 });
        }
    } else {
        sessionStorage.setItem('target-section', sectionId);
        window.location.href = page;
    }
};

// Check for target section on load
document.addEventListener('DOMContentLoaded', () => {
    const targetSection = sessionStorage.getItem('target-section');
    if (targetSection) {
        sessionStorage.removeItem('target-section');
        setTimeout(() => {
            const target = document.getElementById(targetSection);
            if (target && window.lenis) {
                window.lenis.scrollTo(target, { offset: -120, immediate: true });
            }
        }, 500);
    }
});

// ─── DEMO FORM RADIO BUTTONS ───
document.addEventListener('DOMContentLoaded', () => {
  const radioGroups = document.querySelectorAll('.demo-radio-group');
  radioGroups.forEach(group => {
    const btns = group.querySelectorAll('.demo-radio-btn');
    btns.forEach(btn => {
      btn.addEventListener('click', () => {
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });
  });
});

// --- INTERACTIVE GRID HOVER EFFECT (GLOBAL) ---
(function () {
  'use strict';

  var SECTIONS = [
    { selector: '.hero',              cellSize: 24, color: '167,254,43', maxAlpha: 0.35, radius: 1.2 },
    { selector: '.matrix-section',    cellSize: 40, color: '167,254,43', maxAlpha: 0.30, radius: 1.2 },
    { selector: '.manifesto-section', cellSize: 24, color: '167,254,43', maxAlpha: 0.35, radius: 1.2 },
    { selector: '.how-it-works-section', cellSize: 24, color: '167,254,43', maxAlpha: 0.30, radius: 1.2 },
    { selector: '.faculty-gallery',   cellSize: 50, color: '167,254,43', maxAlpha: 0.25, radius: 1.2 },
    { selector: '.timeline-section',  cellSize: 40, color: '167,254,43', maxAlpha: 0.30, radius: 1.2 },
    { selector: '.scrolling-section', cellSize: 40, color: '167,254,43', maxAlpha: 0.35, radius: 1.2 },
    { selector: '.bg-system',         cellSize: 24, color: '167,254,43', maxAlpha: 0.30, radius: 1.2 }
  ];

  function initGridHover(section, cfg) {
    if (section.querySelector('canvas.interactive-grid-canvas')) return; 

    var canvas = document.createElement('canvas');
    canvas.className = 'interactive-grid-canvas';
    canvas.setAttribute('aria-hidden', 'true');
    canvas.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0;display:block;';
    
    if (window.getComputedStyle(section).position === 'static') {
      section.style.position = 'relative';
    }
    section.insertBefore(canvas, section.firstChild);

    var ctx = canvas.getContext('2d');
    var C = cfg.cellSize;
    var W = 0, H = 0;
    var mX = -9999, mY = -9999;
    var alphaGrid = null;
    var raf = null;
    var inside = false;
    var canvasRect = null;
    
    // Performance optimization: queue/set for tracking active cells
    var activeCells = [];
    var activeSet = new Set();

    function updateRect() {
      canvasRect = canvas.getBoundingClientRect();
    }

    function addActiveCell(r, c) {
      var key = r + ',' + c;
      if (!activeSet.has(key)) {
        activeSet.add(key);
        activeCells.push({ r: r, c: c });
      }
    }

    function resize() {
      W = section.offsetWidth;
      H = section.offsetHeight;
      canvas.width  = W;
      canvas.height = H;
      var cols = Math.ceil(W / C) + 1;
      var rows = Math.ceil(H / C) + 1;
      alphaGrid = [];
      for (var r = 0; r < rows; r++) {
        alphaGrid.push(new Float32Array(cols));
      }
      activeCells = [];
      activeSet.clear();
      updateRect();
    }

    function loop() {
      ctx.clearRect(0, 0, W, H);
      var anyAlive = false;
      
      var mouseC = Math.floor(mX / C);
      var mouseR = Math.floor(mY / C);

      // Add the currently hovered cell to active list
      if (inside && mouseR >= 0 && mouseR < alphaGrid.length && mouseC >= 0 && mouseC < alphaGrid[0].length) {
        addActiveCell(mouseR, mouseC);
      }

      var nextActiveCells = [];
      var nextActiveSet = new Set();

      // Only iterate over cells that have non-zero alpha values
      for (var i = 0; i < activeCells.length; i++) {
        var cell = activeCells[i];
        var r = cell.r;
        var c = cell.c;

        var target = 0;
        if (inside && r === mouseR && c === mouseC) {
          target = cfg.maxAlpha;
        }

        var prev = alphaGrid[r][c];
        var speed = target > prev ? 0.35 : 0.10;
        var newVal = prev + (target - prev) * speed;
        alphaGrid[r][c] = newVal;

        if (newVal > 0.004) {
          anyAlive = true;
          ctx.fillStyle = 'rgba(' + cfg.color + ',' + newVal.toFixed(3) + ')';
          ctx.fillRect(c * C + 1, r * C + 1, C - 2, C - 2);

          var key = r + ',' + c;
          nextActiveSet.add(key);
          nextActiveCells.push(cell);
        } else {
          alphaGrid[r][c] = 0;
        }
      }

      activeCells = nextActiveCells;
      activeSet = nextActiveSet;

      if (anyAlive || inside) {
        raf = requestAnimationFrame(loop);
      } else {
        raf = null;
      }
    }

    function startLoop() {
      if (!raf) raf = requestAnimationFrame(loop);
    }

    section.addEventListener('mouseenter', function () {
      updateRect();
    }, { passive: true });

    section.addEventListener('mousemove', function (e) {
      if (!canvasRect) updateRect();
      mX = e.clientX - canvasRect.left;
      mY = e.clientY - canvasRect.top;
      inside = true;
      startLoop();
    }, { passive: true });

    section.addEventListener('mouseleave', function () {
      inside = false;
      startLoop();
    }, { passive: true });

    // Handle scroll to update bounds since client coords change relative to viewport
    window.addEventListener('scroll', function () {
      if (inside) {
        updateRect();
      }
    }, { passive: true });

    resize();
    
    // Throttled/passive window resize listener
    var resizeTimeout;
    window.addEventListener('resize', function () {
      if (resizeTimeout) clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(resize, 150);
    }, { passive: true });
  }

  function bootstrap() {
    SECTIONS.forEach(function (cfg) {
      document.querySelectorAll(cfg.selector).forEach(function (el) {
        initGridHover(el, cfg);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrap);
  } else {
    bootstrap();
  }
})();


/**
 * Braand School Form Handler & Discord Webhook Integration
 * Handles secure submission of all website lead forms to Discord Webhooks.
 */
(function () {
  // The Discord Webhook URL is Base64 encoded to protect it from simple bot scraping.
  // To change the URL in the future:
  // 1. Convert your new Discord Webhook URL to Base64 (e.g. using https://www.base64encode.org/)
  // 2. Replace the string below with your new Base64 string.
  const ENCODED_WEBHOOK_URL = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTQ4OTI4MTM3MzIzNDY1OTMzOC9ZazJ2WkJFUUpqRVYycEdwR045Z05uUzVRaDFBcml4OVNaSk0tSUltVnNvZ0Zpc1d5c0lGMHQyMTlTbkI3NW9kMGRsUQ==";

  function getWebhookUrl() {
    try {
      return atob(ENCODED_WEBHOOK_URL);
    } catch (e) {
      console.error("Failed to decode webhook URL:", e);
      return null;
    }
  }

  async function getIpAndLocation() {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 1200);
      const response = await fetch('https://ipapi.co/json/', { signal: controller.signal });
      clearTimeout(timeoutId);
      if (response.ok) {
        const data = await response.json();
        const city = data.city || '';
        const region = data.region || '';
        const country = data.country_name || '';
        const loc = [city, region, country].filter(Boolean).join(', ');
        return {
          ip: data.ip || 'Unknown',
          location: loc || 'Unknown'
        };
      }
    } catch (e) {
      console.warn("ipapi lookup failed or timed out, trying db-ip fallback", e);
    }
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 1000);
      const response = await fetch('https://api.db-ip.com/v2/free/self', { signal: controller.signal });
      clearTimeout(timeoutId);
      if (response.ok) {
        const data = await response.json();
        return {
          ip: data.ipAddress || 'Unknown',
          location: data.countryName || 'Unknown'
        };
      }
    } catch (e) {
      console.warn("Fallback IP lookup failed:", e);
    }
    return { ip: 'Unknown', location: 'Unknown' };
  }

  async function sendToDiscord(embed) {
    const ipInfo = await getIpAndLocation();
    const fields = [
      ...(embed.fields || []),
      { name: "🌐 IP Address", value: `\`${ipInfo.ip}\``, inline: true },
      { name: "📍 Location", value: `\`${ipInfo.location}\``, inline: true },
      { name: "📄 Source Page", value: `\`${window.location.pathname || '/'}\``, inline: true }
    ];

    const payload = {
      username: "Braand School Leads",
      embeds: [{
        ...embed,
        fields: fields,
        color: embed.color || 11009579, // #a7fe2b (Braand green)
        timestamp: new Date().toISOString(),
        footer: { text: "Braand School Leads System" }
      }]
    };

    try {
      const response = await fetch("/api/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      return response.ok;
    } catch (error) {
      console.error("Error sending lead to Discord:", error);
      return false;
    }
  }

  document.addEventListener("DOMContentLoaded", () => {
    // 1. ENROLL / ADMISSION MODAL FORM (#enroll-form)
    const enrollForm = document.getElementById("enroll-form");
    if (enrollForm && typeof window.handleFormSubmit === "undefined") {
      enrollForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const name = enrollForm.querySelector('input[name="name"]')?.value || "N/A";
        const email = enrollForm.querySelector('input[name="email"]')?.value || "N/A";
        const phone = enrollForm.querySelector('input[name="phone"]')?.value || "N/A";
        const interestSelect = enrollForm.querySelector('select[name="interest"]');
        const interest = interestSelect ? interestSelect.options[interestSelect.selectedIndex]?.text : "N/A";

        sendToDiscord({
          title: "🎓 New Admission Application",
          fields: [
            { name: "👤 Full Name", value: `**${name}**`, inline: true },
            { name: "✉️ Email Address", value: `**${email}**`, inline: true },
            { name: "📞 Phone Number", value: `**${phone}**`, inline: true },
            { name: "🎯 Interested Course", value: `**${interest}**`, inline: true }
          ]
        });
      });
    }

    // 2. COHORT REGISTRATION FORM (#apply-form)
    const applyForm = document.getElementById("apply-form");
    if (applyForm && typeof window.handleFormSubmit === "undefined") {
      applyForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const name = applyForm.querySelector('input[name="name"]')?.value || "N/A";
        const phone = applyForm.querySelector('input[name="phone"]')?.value || "N/A";
        const email = applyForm.querySelector('input[name="email"]')?.value || "N/A";
        const goal = applyForm.querySelector('textarea[name="goal"]')?.value || "N/A";

        sendToDiscord({
          title: "⚡ New Cohort Seat Application",
          fields: [
            { name: "👤 Full Name", value: `**${name}**`, inline: true },
            { name: "📞 WhatsApp Number", value: `**${phone}**`, inline: true },
            { name: "✉️ Email Address", value: `**${email}**`, inline: true },
            { name: "💡 Goal / Intent", value: `**${goal}**` }
          ]
        });
      });
    }

    // 3. MANIFESTO / GENERAL ENQUIRY FORM (.mf-enquiry)
    const enquiryForm = document.querySelector(".mf-enquiry");
    if (enquiryForm) {
      enquiryForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const name = enquiryForm.querySelector('input[name="name"]')?.value || "N/A";
        const phone = enquiryForm.querySelector('input[name="phone"]')?.value || "N/A";
        const interestSelect = enquiryForm.querySelector('select[name="interest"]');
        const interest = interestSelect ? interestSelect.options[interestSelect.selectedIndex]?.text : "N/A";

        const embed = {
          title: "❓ New General Inquiry",
          fields: [
            { name: "👤 Full Name", value: `**${name}**`, inline: true },
            { name: "📞 Phone", value: `**${phone}**`, inline: true },
            { name: "🎯 Interested In", value: `**${interest}**`, inline: true }
          ]
        };

        const submitBtn = enquiryForm.querySelector('button[type="submit"]');
        if (submitBtn) {
          const originalText = submitBtn.innerHTML;
          submitBtn.innerHTML = "Submitting...";
          submitBtn.disabled = true;

          const success = await sendToDiscord(embed);
          if (success) {
            submitBtn.innerHTML = "Enquired ✓";
            enquiryForm.reset();
          } else {
            submitBtn.innerHTML = "Error. Try again";
            setTimeout(() => {
              submitBtn.innerHTML = originalText;
              submitBtn.disabled = false;
            }, 3000);
          }
        } else {
          sendToDiscord(embed);
        }
      });
    }

    // 4. DEMO BOOKING FORM (.demo-section form)
    const demoForms = document.querySelectorAll(".demo-section form");
    demoForms.forEach((demoForm) => {
      demoForm.removeAttribute("onsubmit");
      
      demoForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        const name = demoForm.querySelector('input[type="text"]')?.value || "N/A";
        const phone = demoForm.querySelector('input[placeholder*="PHONE"], input[placeholder*="90835"]')?.value || "N/A";
        const email = demoForm.querySelector('input[type="email"]')?.value || "N/A";
        
        const activeRadio = demoForm.querySelector(".demo-radio-btn.active");
        const goal = activeRadio ? activeRadio.textContent.trim() : "N/A";

        const embed = {
          title: "📅 New Demo Booking",
          fields: [
            { name: "👤 Full Name", value: `**${name}**`, inline: true },
            { name: "📞 WhatsApp Number", value: `**${phone}**`, inline: true },
            { name: "✉️ Email Address", value: `**${email}**`, inline: true },
            { name: "💡 Goal / Intent", value: `**${goal}**`, inline: true }
          ]
        };

        const submitBtn = demoForm.querySelector('button[type="submit"]');
        if (submitBtn) {
          const originalText = submitBtn.innerHTML;
          submitBtn.innerHTML = "Booking...";
          submitBtn.disabled = true;

          const success = await sendToDiscord(embed);
          if (success) {
            submitBtn.innerHTML = "Demo Booked! ✓";
            demoForm.reset();
          } else {
            submitBtn.innerHTML = "Error. Try again";
            setTimeout(() => {
              submitBtn.innerHTML = originalText;
              submitBtn.disabled = false;
            }, 3000);
          }
        } else {
          sendToDiscord(embed);
        }
      });
    });
  });
})();

document.addEventListener("DOMContentLoaded", function() {
  const selects = document.querySelectorAll("select[name=\"interest\"], #enroll-interest");
  selects.forEach(select => {
    select.style.display = "none";
    
    const wrapper = document.createElement("div");
    wrapper.className = "custom-select-wrapper";
    select.parentNode.insertBefore(wrapper, select);
    wrapper.appendChild(select);
    
    const selectedDiv = document.createElement("div");
    selectedDiv.className = "custom-select-trigger";
    
    let initialText = "Select...";
    if(select.options.length > 0) {
        initialText = select.options[0].text;
        for(let i=0; i<select.options.length; i++){
            if(select.options[i].selected && !select.options[i].disabled) {
                initialText = select.options[i].text;
                break;
            }
        }
    }
    selectedDiv.innerHTML = `<span>${initialText}</span><div class="custom-select-arrow"></div>`;
    wrapper.appendChild(selectedDiv);
    
    const optionsDiv = document.createElement("div");
    optionsDiv.className = "custom-select-options";
    
    document.body.appendChild(optionsDiv);

    // Add touch-hover tracking for mobile to simulate desktop hover
    optionsDiv.addEventListener("touchmove", function(e) {
        if (!e.touches.length) return;
        const touch = e.touches[0];
        const elem = document.elementFromPoint(touch.clientX, touch.clientY);
        
        // Remove touch-hover from all
        optionsDiv.querySelectorAll(".custom-select-option").forEach(el => el.classList.remove("touch-hover"));
        
        // Add to current
        if (elem && elem.classList.contains("custom-select-option")) {
            elem.classList.add("touch-hover");
        }
    }, {passive: true});
    
    optionsDiv.addEventListener("touchend", function() {
        setTimeout(() => {
            optionsDiv.querySelectorAll(".custom-select-option").forEach(el => el.classList.remove("touch-hover"));
        }, 150);
    });

    
    Array.from(select.options).forEach((opt, index) => {
      if (opt.disabled && opt.hidden) return;
      const optDiv = document.createElement("div");
      optDiv.className = "custom-select-option";
      optDiv.textContent = opt.text;
      if (opt.selected) optDiv.classList.add("selected");
      
      
      optDiv.addEventListener("touchstart", function() {
          optDiv.classList.add("touch-hover");
      }, {passive: true});
      optDiv.addEventListener("touchend", function() {
          setTimeout(() => optDiv.classList.remove("touch-hover"), 150);
      });
      optDiv.addEventListener("touchcancel", function() {
          optDiv.classList.remove("touch-hover");
      });
      
      optDiv.addEventListener("click", function(e) {

        select.selectedIndex = index;
        select.dispatchEvent(new Event("change"));
        
        selectedDiv.querySelector("span").textContent = opt.text;
        
        optionsDiv.querySelectorAll(".custom-select-option").forEach(el => el.classList.remove("selected"));
        optDiv.classList.add("selected");
        
        wrapper.classList.remove("open");
        optionsDiv.classList.remove("open");
        optionsDiv.style.display = "";
      });
      optionsDiv.appendChild(optDiv);
    });
    
    function updatePosition() {
        if (!optionsDiv.classList.contains("open")) return;
        const rect = selectedDiv.getBoundingClientRect();
        const spaceBelow = window.innerHeight - rect.bottom;
        const dropdownHeight = optionsDiv.offsetHeight || 250;
        
        optionsDiv.style.position = "fixed";
        optionsDiv.style.left = rect.left + "px";
        optionsDiv.style.width = rect.width + "px";
        optionsDiv.style.zIndex = "999999";
        
        if (spaceBelow < dropdownHeight && rect.top > dropdownHeight) {
            // Open upwards
            optionsDiv.style.top = "auto";
            optionsDiv.style.bottom = (window.innerHeight - rect.top + 4) + "px";
        } else {
            // Open downwards
            optionsDiv.style.top = (rect.bottom + 4) + "px";
            optionsDiv.style.bottom = "auto";
        }
    }
    
    selectedDiv.addEventListener("click", function(e) {
      e.stopPropagation();
      const isOpen = wrapper.classList.contains("open");
      
      document.querySelectorAll(".custom-select-wrapper").forEach(w => w.classList.remove("open"));
      document.querySelectorAll(".custom-select-options").forEach(o => {
          o.classList.remove("open");
          o.style.display = "";
      });
      
      if (!isOpen) {
        wrapper.classList.add("open");
        optionsDiv.classList.add("open");
        
        // Temporarily display block to get height
        optionsDiv.style.display = "block";
        updatePosition();
      }
    });
    
    window.addEventListener("scroll", updatePosition, true);
    window.addEventListener("resize", updatePosition);
  });
  
  document.addEventListener("click", function(e) {
    if (!e.target.closest(".custom-select-options")) {
      document.querySelectorAll(".custom-select-wrapper").forEach(w => w.classList.remove("open"));
      document.querySelectorAll(".custom-select-options").forEach(o => {
          o.classList.remove("open");
          o.style.display = ""; // Reset inline display
      });
    }
  });
});


document.addEventListener("touchstart", function() {}, {passive: true});
