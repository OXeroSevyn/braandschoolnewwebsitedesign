import os

css_file = "/Users/isharoka/Downloads/MAin website/assets/css/main.css"

css_to_add = """
/* Add styling for native selects so they match the inputs if custom JS fails or loads late */
.form-group select {
  width: 100%;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 14px 16px;
  color: var(--white);
  font-family: var(--font-display);
  font-size: 14px;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  outline: none;
  -webkit-appearance: none;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'12\' height=\'12\' viewBox=\'0 0 24 24\' fill=\'none\' stroke=\'white\' stroke-width=\'2\' stroke-linecap=\'round\' stroke-linejoin=\'round\'%3E%3Cpolyline points=\'6 9 12 15 18 9\'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 16px center;
  cursor: pointer;
}

.form-group select:focus {
  border-color: var(--green, #bcff00);
  background: rgba(188, 255, 0, 0.05);
}
"""

with open(css_file, "a") as f:
    f.write("\n" + css_to_add)
    
print("Appended native select styling.")
