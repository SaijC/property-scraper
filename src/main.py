from src.scraper.scraper_base import fetch_page, parse_headlines
from src.utils.utils import save_to_csv

def main():
    url = "https://example-news-site.com"  # Replace with real site
    html = fetch_page(url)
    
    if html:
        headlines = parse_headlines(html)
        if headlines:
            save_to_csv(headlines, "data/headlines.csv")
        else:
            print("No headlines found")
    else:
        print("Failed to fetch the page")

if __name__ == "__main__":
    main()
