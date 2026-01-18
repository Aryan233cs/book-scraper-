# book-scraper-
# Book Scraper (Python)

A Python web scraper that extracts book data from https://books.toscrape.com

## Features
- Scrapes all pages automatically
- Handles pagination safely
- Extracts title, price, and availability
- Saves clean data to CSV and JSON
- Uses sessions, headers, and encoding handling

## Technologies Used
- Python
- requests
- BeautifulSoup
- CSV / JSON

## How It Works
1. Starts from the first page
2. Extracts all books on the page
3. Detects and follows the "Next" button
4. Repeats until last page
5. Saves data after scraping completes

## How to Run
```bash
pip install -r requirements.txt
python scraper.py
