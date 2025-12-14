# ================================
# PROJECT: Web Scraping + CSV/Excel Exporter
# AUTHOR: Santhosh Kumar (santhoshk-dev)
# USE CASE: Freelancing / Client Projects
# =================================

"""
This project scrapes product data from a website and saves it into CSV and Excel.
You can show this project to freelance clients.

FEATURES:
- Requests + BeautifulSoup scraping
- Clean data extraction
- CSV and Excel export
- Error handling

NOTE:
This demo uses a sample website structure.
You can adapt selectors for Amazon/Flipkart/any site.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# ---------------- CONFIG ----------------
URL = "https://books.toscrape.com/catalogue/page-1.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

CSV_FILE = "products.csv"
EXCEL_FILE = "products.xlsx"

# ---------------- SCRAPER FUNCTION ----------------
def scrape_products():
    print("[+] Starting web scraping...")

    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("article", class_="product_pod")

    data = []

    for product in products:
        title = product.h3.a["title"]
        price = product.find("p", class_="price_color").text.strip()
        availability = product.find("p", class_="instock availability").text.strip()

        data.append({
            "Product Name": title,
            "Price": price,
            "Availability": availability,
            "Scraped At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    print(f"[+] Scraped {len(data)} products")
    return data

# ---------------- SAVE FUNCTIONS ----------------
def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv(CSV_FILE, index=False)
    print(f"[+] Data saved to {CSV_FILE}")


def save_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel(EXCEL_FILE, index=False)
    print(f"[+] Data saved to {EXCEL_FILE}")

# ---------------- MAIN ----------------
def main():
    try:
        data = scrape_products()
        save_to_csv(data)
        save_to_excel(data)
        print("[✓] Web scraping completed successfully")
    except Exception as e:
        print("[!] Error occurred:", e)


if __name__ == "__main__":
    main()

# ================================
# HOW TO RUN:
# 1. pip install requests beautifulsoup4 pandas openpyxl
# 2. python scraper.py
# ================================
