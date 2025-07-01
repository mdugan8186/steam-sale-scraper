# test_transform.py

from extract import load_config, extract_items
from transform import transform_all

with open("output/test_rendered_page.html", "r", encoding="utf-8") as f:
    html = f.read()

config = load_config()
raw_items = extract_items(html, config)
clean_items = transform_all(raw_items)

for item in clean_items[:3]:
    print(item)
