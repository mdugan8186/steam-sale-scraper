# test_render.py

import os
from render import render_page

html = render_page()

# Ensure output/ directory exists
os.makedirs("output", exist_ok=True)

# Save the rendered HTML to a file
with open("output/test_rendered_page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Page rendered and saved to output/test_rendered_page.html")
