import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """Fetch HTML content of a page"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an error for bad status
        return response.text
    except requests.RequestException as e:
        print("Error fetching page:", e)
        return None

def parse_headlines(html):
    """Parse HTML and extract headlines"""
    soup = BeautifulSoup(html, "html.parser")
    headlines = [h.text.strip() for h in soup.find_all("h2")]
    return headlines
