# Steam Specials Scraper

This project scrapes the most discounted games from the [Steam Specials page](https://store.steampowered.com/specials) using Playwright to render JavaScript and Selectolax to parse HTML. It outputs structured game data to a CSV file.

---

## 🔍 Features

- Renders JavaScript-heavy pages using Playwright
- Extracts structured data:
  - Game title
  - Tags (genres, features)
  - Review score and review count
  - Original price, discounted price, discount percentage
  - Thumbnail image URL
- Outputs to clean CSV format

---

## 📁 Output

The resulting file is saved to:

`output/steam_specials.csv`

Each row contains full structured data for one game.

---

## 🧰 Tech Stack

- [Playwright (Python)](https://playwright.dev/python/) — headless browser automation
- [Selectolax](https://github.com/rushter/selectolax) — fast HTML parser
- Python 3.10+

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/steam-specials-scraper.git
cd steam-specials-scraper

# (Optional) Set up a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: .\\venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Install browser binaries for Playwright
python -m playwright install chromium

# Run the scraper
python main.py
```

---

## 📝 Notes

- This scraper is modular and easy to maintain.
- If Steam updates its layout or CSS classes, update the `config.json` selectors.
- Designed for educational, portfolio, or internal use only.

---

## 💼 Use Cases

- Game deal newsletters and alerts
- Competitor price analysis
- Personal deal tracker
- Freelance data collection project

---

## 📊 Sample Output

| Title           | Discount | Review Score            | Review Count |
| --------------- | -------- | ----------------------- | ------------ |
| Cyberpunk 2077  | 65% off  | Very Positive           | 754,433      |
| Baldur's Gate 3 | 20% off  | Overwhelmingly Positive | 674,651      |
