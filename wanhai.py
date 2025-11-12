from playwright.sync_api import sync_playwright

def scrape_wanhai():
    URL = "https://www.wanhai.com/views/skd/SkdBySvc.xhtml?file_num=64836&parent_id=64834&top_file_num=64735"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            viewport={"width":1280, "height":800},
        )
        page = context.new_page()

        print("Loading page...")
        page.goto(URL, timeout=120000, wait_until="domcontentloaded")
        page.wait_for_timeout(8000)

        html = page.content()
        print("Title:", page.title())

        with open("wanhai_page.xhtml", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved wanhai_page.xhtml")

        browser.close()

if __name__ == "__main__":
    scrape_wanhai()
