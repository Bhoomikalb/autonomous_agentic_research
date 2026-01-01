import requests
from bs4 import BeautifulSoup

def scrape_text(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.get_text()[:3000]
    except Exception as e:
        return f"Failed to scrape {url}: {e}"
