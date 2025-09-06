# Testing – Steam Specials Scraper

## Render → Extract → Transform (manual flow)
1. `python test_render.py`  
   - Saves HTML to `output/test_rendered_page.html`

2. `python test_extract.py`  
   - Loads saved HTML, uses `config.json`, prints first few raw items

3. `python test_transform.py`  
   - Runs parsing/normalization and prints cleaned items

## Sanity Checks
- [ ] `python -m playwright install chromium` completed successfully
- [ ] `python main.py` creates `output/steam_specials.csv`
- [ ] CSV has expected columns and non-empty rows
- [ ] Changing `headless` in `render.py` behaves as expected

## Selector Maintenance
- [ ] If Steam markup changes, update `config.json` selectors
- [ ] Re-run the 3 test scripts and validate outputs

## Data Quality
- [ ] Prices normalize correctly (currency format consistent)
- [ ] `discount_percent` parses as number
- [ ] Tags saved as comma-separated values
- [ ] Timestamps included (`scraped_at`)
