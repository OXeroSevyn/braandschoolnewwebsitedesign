import os

blog_html_path = "/Users/isharoka/Downloads/MAin website/blog.html"
generated_blogs_path = "/Users/isharoka/Downloads/MAin website/scratch/generated_blogs.html"

# Load generated blogs html content
with open(generated_blogs_path, "r", encoding="utf-8") as f:
    blogs_html = f.read()

# Load blog.html content
with open(blog_html_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Locate replacement region (Start: line 498, End: line 796)
# Keep in mind python uses 0-indexed list for lines, so line 498 is lines[497]
# Let's verify the content of lines[497] and lines[795]
start_line_idx = 497  # line 498
end_line_idx = 796    # line 797 is lines[796], we want to include lines[795] which is pager ending </div>

print("Start line target:", lines[start_line_idx].strip())
print("End line target:", lines[end_line_idx - 1].strip())

# Construct the replacement payload
filters_html = """
                <!-- Blog Filter Tabs -->
                <div class="blog-filters">
                  <button class="filter-btn active" data-filter="all">All</button>
                  <button class="filter-btn" data-filter="blog">Blogs</button>
                  <button class="filter-btn" data-filter="siliguri">Siliguri</button>
                  <button class="filter-btn" data-filter="podcasts">Podcasts</button>
                  <button class="filter-btn" data-filter="updates">Updates</button>
                </div>
"""

pagination_html = """
                <!-- Pager container -->
                <div class="pager" style="margin-top: 50px;">
                  <!-- Dynamic JS pagination links will render here -->
                </div>
"""

custom_styles = """
    <style>
      .blog-filters {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        margin-bottom: 40px;
        padding: 5px 0;
      }
      .filter-btn {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #a1a1aa !important;
        padding: 10px 22px !important;
        border-radius: 100px !important;
        cursor: pointer;
        font-size: 12px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
      }
      .filter-btn:hover {
        border-color: rgba(201, 243, 29, 0.4) !important;
        color: #ffffff !important;
        background: rgba(255, 255, 255, 0.05) !important;
      }
      .filter-btn.active {
        background: #c9f31d !important;
        border-color: #c9f31d !important;
        color: #000000 !important;
      }
      @keyframes fadeInUp {
        from {
          opacity: 0;
          transform: translateY(20px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }
    </style>
"""

custom_js = """
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        const postsPerPage = 6;
        let currentPage = 1;
        let activeCategory = "all";
        let searchQuery = "";

        const items = Array.from(document.querySelectorAll(".onovo-blog-item.archive-item"));
        const pagerContainer = document.querySelector(".pager");
        const filterBtns = document.querySelectorAll(".filter-btn");
        const searchInput = document.getElementById("wp-block-search__input-1");
        const searchForm = document.querySelector(".wp-block-search");

        // Prevent default submit on search form
        if (searchForm) {
          searchForm.addEventListener("submit", function(e) {
            e.preventDefault();
            searchQuery = searchInput.value.toLowerCase().trim();
            currentPage = 1;
            updateGrid();
          });
          
          searchInput.addEventListener("input", function() {
            searchQuery = searchInput.value.toLowerCase().trim();
            currentPage = 1;
            updateGrid();
          });
        }

        // Filter button listeners
        filterBtns.forEach(btn => {
          btn.addEventListener("click", function() {
            filterBtns.forEach(b => b.classList.remove("active"));
            this.classList.add("active");
            activeCategory = this.getAttribute("data-filter");
            currentPage = 1;
            updateGrid();
          });
        });

        function updateGrid() {
          // Filter items
          let visibleItems = items.filter(item => {
            const categoryMatch = activeCategory === "all" || item.getAttribute("data-category") === activeCategory;
            
            const titleText = item.querySelector(".title").textContent.toLowerCase();
            const descText = item.querySelector(".onovo-text").textContent.toLowerCase();
            const searchMatch = !searchQuery || titleText.includes(searchQuery) || descText.includes(searchQuery);
            
            return categoryMatch && searchMatch;
          });

          // Hide all items first
          items.forEach(item => {
            item.style.display = "none";
          });

          // Show items for current page
          const totalPages = Math.ceil(visibleItems.length / postsPerPage) || 1;
          if (currentPage > totalPages) currentPage = totalPages;

          const start = (currentPage - 1) * postsPerPage;
          const end = start + postsPerPage;
          const pageItems = visibleItems.slice(start, end);

          pageItems.forEach(item => {
            item.style.display = "block";
            item.style.animation = "fadeInUp 0.5s ease forwards";
          });

          // Update pagination controls
          renderPager(totalPages);
        }

        function renderPager(totalPages) {
          if (!pagerContainer) return;
          pagerContainer.innerHTML = "";

          if (totalPages <= 1) {
            pagerContainer.style.display = "none";
            return;
          }
          pagerContainer.style.display = "flex";

          // Previous button
          if (currentPage > 1) {
            const prevLink = document.createElement("a");
            prevLink.className = "prev page-numbers";
            prevLink.href = "#";
            prevLink.innerHTML = "<i class='fa fa-chevron-left'></i>";
            prevLink.addEventListener("click", function(e) {
              e.preventDefault();
              currentPage--;
              updateGrid();
              scrollToGrid();
            });
            pagerContainer.appendChild(prevLink);
          }

          for (let i = 1; i <= totalPages; i++) {
            if (i === currentPage) {
              const span = document.createElement("span");
              span.className = "page-numbers current";
              span.textContent = i;
              pagerContainer.appendChild(span);
            } else {
              const link = document.createElement("a");
              link.className = "page-numbers";
              link.href = "#";
              link.textContent = i;
              link.addEventListener("click", function(e) {
                e.preventDefault();
                currentPage = i;
                updateGrid();
                scrollToGrid();
              });
              pagerContainer.appendChild(link);
            }
          }

          // Next button
          if (currentPage < totalPages) {
            const nextLink = document.createElement("a");
            nextLink.className = "next page-numbers";
            nextLink.href = "#";
            nextLink.innerHTML = "<i class='fa fa-chevron-right'></i>";
            nextLink.addEventListener("click", function(e) {
              e.preventDefault();
              currentPage++;
              updateGrid();
              scrollToGrid();
            });
            pagerContainer.appendChild(nextLink);
          }
        }

        function scrollToGrid() {
          const gridTop = document.querySelector(".onovo-archive-post").getBoundingClientRect().top + window.pageYOffset - 100;
          window.scrollTo({ top: gridTop, behavior: "smooth" });
        }

        // Initial update
        updateGrid();
      });
    </script>
"""

new_content = filters_html + blogs_html + pagination_html + custom_styles + custom_js

# Replace lines between start and end
updated_lines = lines[:start_line_idx] + [new_content] + lines[end_line_idx:]

with open(blog_html_path, "w", encoding="utf-8") as f:
    f.writelines(updated_lines)

print("Applied update to blog.html!")
