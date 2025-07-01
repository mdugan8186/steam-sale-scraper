# test_extract.py

from extract import load_config, extract_items

with open("output/test_rendered_page.html", "r", encoding="utf-8") as f:
    html = f.read()

config = load_config()
items = extract_items(html, config)

# Print first 3 results
for item in items[:3]:
    print(item)
