from playwright.sync_api import sync_playwright

URL = "https://www.realestate.com.au/buy/in-sydney,+nsw+2000/list-1"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,  # set True later when it works
        args=["--disable-blink-features=AutomationControlled"]
    )

    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        locale="en-AU",
        viewport={"width": 1280, "height": 800}
    )
    print("browser:", browser)

    # page = context.new_page()
    # page.goto(URL, timeout=60000)

    # # Wait for listings to appear
    # page.wait_for_selector('a[href*="/property-"]', timeout=60000)

    # # Scroll to trigger lazy loading
    # for _ in range(5):
    #     page.mouse.wheel(0, 3000)
    #     page.wait_for_timeout(1500)

    # listings = page.query_selector_all('a[href*="/property-"]')

    # seen = set()
    # results = []

    # for l in listings:
    #     title = l.inner_text().strip()
    #     link = l.get_attribute("href")

    #     if link and "/property-" in link:
    #         full_url = "https://www.realestate.com.au" + link
    #         if full_url not in seen:
    #             seen.add(full_url)
    #             results.append((title, full_url))

    # print(f"\nFound {len(results)} listings:\n")

    # for title, link in results[:10]:
    #     print(title)
    #     print(link)
    #     print("-" * 60)

    # input("Press ENTER to close browser...")
    browser.close()
