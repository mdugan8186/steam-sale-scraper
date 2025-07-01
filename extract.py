# extract.py

import json
from selectolax.parser import HTMLParser


def load_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_items(html, config):
    tree = HTMLParser(html)
    items = tree.css(config["item_selector"])
    results = []

    for item in items:
        data = {}

        for field, selector in config["fields"].items():
            # Special case: extract ALL tags into a list
            if field == "tags":
                tag_nodes = item.css(selector)
                data[field] = [tag.text(strip=True)
                               for tag in tag_nodes] if tag_nodes else None
                continue

            # Standard extraction for everything else
            node = item.css_first(selector)
            if node:
                attr_type = config["attributes"].get(field, "text")
                if attr_type == "text":
                    data[field] = node.text(strip=True)
                else:
                    data[field] = node.attributes.get(attr_type, "")
            else:
                data[field] = None  # Handle missing fields safely

        results.append(data)

    return results
