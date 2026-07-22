# ⚡ Braand School — Premium Web Experience

[![Aesthetics: Premium](https://img.shields.io/badge/Aesthetics-Premium-a7fe2b?style=flat-square&logoColor=black)](https://github.com/OXeroSevyn/braandschoolnewwebsitedesign)
[![Hosting: Hostinger Subfolder](https://img.shields.io/badge/Hosting-Hostinger%20Subfolder-000000?style=flat-square&logo=hostinger&logoColor=white)](https://github.com/OXeroSevyn/braandschoolnewwebsitedesign)
[![Engine: Vanilla HTML5 / CSS3](https://img.shields.io/badge/Engine-HTML5%20%2F%20CSS3-orange?style=flat-square)](https://github.com/OXeroSevyn/braandschoolnewwebsitedesign)

> *"We believe thinking is more valuable than tools. We believe impact is more important than aesthetics. The industry doesn't need more pixel-pushers. It needs practitioners who know why."*
> — **The Braand School Manifesto**

Welcome to the brand new **Braand School** web platform. This is a state-of-the-art, high-fidelity, and pixel-perfect design system built using modern vanilla HTML5, custom CSS styling, smooth layout transitions, and high-performance micro-animations. The entire application is tailor-engineered for deploying in custom directories, such as Hostinger subfolders (`/bipdesign/`), utilizing clean extensionless URL routing.

---

## 🎨 Visual Identity & Tech Stack

This platform is engineered using modern front-end best practices to achieve a stunning, premium aesthetic right out of the box:
* **Typography**: Custom pairing of **Space Grotesk** (display & headings) and **Space Mono** (monospaced accents, kickers, and code-like CTA badges) from Google Fonts.
* **Palette**: An ultra-sleek dark mode baseline (`#080808`) highlighted by a vibrant, high-contrast neon green accent (`#a7fe2b`) and glassmorphic overlays.
* **Micro-Animations**: Powered by **Anime.js** for high-framerate scroll reveals, popup animations, and magnetic interactions.
* **Aesthetic Anchors**: Custom grain noise vector filters, dynamic interactive elements, and highly polished responsive breakpoints.

---

## 📁 Repository Structure

Below is an overview of the core files and folders in this workspace:

```text
├── index.html                       # The high-fidelity homepage
├── course.html                      # The courses hub landing page
├── braanding-course.html            # Specialized Course: Visual & Strategic Branding
├── business-marketing-course.html   # Specialized Course: Brand Business & Growth Marketing
├── creator-course.html              # Specialized Course: The Creator Economy & Content Strategy
├── life-at-bs.html                  # Immersive gallery showing the student experience
├── assets/                          # Core brand logos and brand graphics
├── images/                          # Content graphics, mockups, student works, and avatars
├── uploads/                         # Dynamic design assets and interactive attachments
├── .htaccess                        # Main production rewrite engine for clean URLs
├── dev_server.py                    # Local utility server for clean URL testing
├── scraps/                          # Automation scripts, tools, and developer helpers
│   └── copy_to_filezilla.ps1        # PowerShell automated packaging script for FTP
└── for filezilla/                   # [Production Only] Automated clean folder for server upload
```

---

## ✨ Features & Engineering Details

### 1. Unified Premium Footers
The global site footer has been beautifully standardized across all major course landing pages:
* **Zero Variable Bleed**: Engineered with scoped, isolated CSS variables. No layout colors, column formatting, or text sizes spill out into parent container modules.
* **Mockup Perfect**: Perfectly mirrors the visual layout, matching font-weights, line-heights, social icon alignment, and spacing to the exact design specifications.
* **Interactive Hover States**: Subtle hover micro-animations on all footer navigation links, email endpoints, and terms.

### 2. Clean Routing & Subfolder Compatibility
Designed to support a clean, modern browser address bar experience without `.html` extensions (e.g. `domain.com/bipdesign/course` instead of `domain.com/bipdesign/course.html`).
* **Apache Rewrite Engine**: The custom `.htaccess` file inside `for filezilla/` is pre-configured with a subfolder base:
  ```apache
  RewriteEngine On
  RewriteBase /bipdesign/
  ```
* **Relative Substitution Rules**: Rewrites are carefully targeted to prevent trailing slash loops and ensure paths resolve cleanly relative to the `/bipdesign/` subdirectory without breaking absolute domain configurations.

---

## 💻 Local Development

Double-clicking `.html` files directly in your browser will prevent extensionless URL links from resolving. To run a fully compatible local server that mimics the production `.htaccess` rewrite rules:

1. **Launch the custom Dev Server**:
   Run the pre-configured Python utility server in your terminal:
   ```bash
   python dev_server.py
   ```
2. **Open the Local Preview**:
   Navigate to **`http://localhost:8000`** in your browser.
3. All extensionless navigation links (such as `/course`, `/braanding-course`) will resolve flawlessly to their corresponding HTML files locally!

---

## 🚀 Production Packaging & Deployment Guide

To deploy this project to Hostinger (in your `/public_html/bipdesign/` folder) without uploading developer clutter like `.zip` backups or temporary Git files:

### Step 1: Run the Package Script
We have included a highly efficient PowerShell utility to package only production-ready files:
1. Open PowerShell inside your project folder.
2. Run the packaging utility:
   ```powershell
   ./scraps/copy_to_filezilla.ps1
   ```
3. This will create or update a clean directory named **`for filezilla/`** containing only compiled HTML pages, images, assets, uploads, and the optimized `.htaccess` routing file.

### Step 2: Upload via FileZilla (or Hostinger File Manager)
1. Open **FileZilla** and connect to your Hostinger server.
2. Navigate to your remote folder: `/public_html/bipdesign/`.
3. Open the local **`for filezilla/`** folder.
4. Drag and drop all contents from `for filezilla/` directly into `/public_html/bipdesign/`.

Your premium website will immediately go live with fully responsive features, clean URLs, and unified interactive components!

---

## ⚙️ Maintenance & Contribution Guidelines

* **CSS Modularity**: When adding styling to individual course pages, encapsulate them within specific CSS classes or namespaces to avoid styling conflicts.
* **Asset Optimization**: Compress large mockup images or media overlays before committing to keep repository footprints small and page load speeds under 1.5 seconds.
* **Routing Pathing**: Ensure any new pages are written as self-contained static HTML pages and are properly routed inside both the `dev_server.py` router and the production `.htaccess` rewrite rules.

---

<div align="center">
  <sub>Built with ❤️ by the <b>Braand School Creative Team</b>. &copy; 2026. All rights reserved.</sub>
</div>
