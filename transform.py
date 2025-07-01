# transform.py

import re


def parse_price(price_str):
    if not price_str:
        return None
    try:
        return float(price_str.replace("$", "").replace(",", "").strip())
    except ValueError:
        return None


def parse_discount(discount_str):
    if not discount_str:
        return None
    try:
        return int(discount_str.replace("-", "").replace("%", "").strip())
    except ValueError:
        return None


def parse_review_count(review_str):
    if not review_str:
        return None
    try:
        # Example: "88,885 User Reviews" -> 88885
        num = re.findall(r"[\d,]+", review_str)
        if num:
            return int(num[0].replace(",", ""))
    except ValueError:
        return None
    return None


def transform_item(item):
    return {
        "title": item["title"],
        "thumbnail": item["thumbnail"],
        "tags": item["tags"],
        "review_score": item["review_score"].strip() if item["review_score"] else None,
        "review_count": parse_review_count(item["review_count"]),
        "original_price": parse_price(item["original_price"]),
        "discounted_price": parse_price(item["discounted_price"]),
        "discount_percent": parse_discount(item["discount_percent"]),
    }


def transform_all(items):
    return [transform_item(item) for item in items]
