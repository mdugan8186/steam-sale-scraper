# main.py

import csv
import os
from render import render_page
from extract import load_config, extract_items
from transform import transform_all

OUTPUT_FILE = "output/steam_specials.csv"


def save_to_csv(items, path):
    if not items:
        print("No items to save.")
        return

    keys = items[0].keys()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(items)

    print(f"✅ Data saved to: {path}")


def main():
    html = render_page()
    config = load_config()
    raw_items = extract_items(html, config)
    clean_items = transform_all(raw_items)

    # 🔧 Convert tags list to comma-separated string
    for item in clean_items:
        if isinstance(item["tags"], list):
            item["tags"] = ", ".join(item["tags"])

    save_to_csv(clean_items, OUTPUT_FILE)


if __name__ == "__main__":
    main()
