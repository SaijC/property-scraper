from scraper.scraper_base import Scraper
from utils.utils import save_to_csv

def main():
    scraper = Scraper()

    url = "https://stackoverflow.com/questions/46775952/how-to-move-a-line-up-or-down-in-visual-studio-code-for-mac"
    html = scraper.fetch_page(url)

    if html:
        headlines = scraper.parse_headlines(html)
        if headlines:
            save_to_csv(headlines, "data/headlines.csv")
        else:
            print("No headlines found")
    else:
        print("Failed to fetch the page")

if __name__ == "__main__":
    main()
