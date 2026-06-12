import re

from playwright.sync_api import sync_playwright

BROWSER_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def get_all_products(page):
    results = page.locator(".Bm3ON")
    count = results.count()
    print(f"Found {count} results")

    for item in results.all():
        text = item.inner_text()
        print(f"{text}\n")
        match = re.search(r"৳\s*[\d,]+", text)
        # match2 = re.findall(r"[a-z]*৳\s*[\d,]+", text)
        # if match2:
        #     print(f"match2: {match2}\n")
        if match:
            price_text = match.group()
            print(price_text)
            price = re.sub(r"[^\d]", "", price_text)
            print(int(price))
        else:
            print("No price found")
        print("\n")


def get_first_product_details(browser, page, name: str):
    result = page.locator(".Bm3ON", has_text=name).first
    # or
    # result = page.locator(f'.Bm3ON [title="{name}"]').first # Css Attribute Selector
    link = "kichu pai nai"
    link = result.locator("a").first.get_attribute("href")
    print(link)

    result.click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)
    page.go_back(wait_until="domcontentloaded")

    # print(result.inner_text())
    # create new window
    # product_page = browser.new_page()
    # link = "https:" + link
    # product_page.goto(link)
    # product_page.wait_for_load_state("domcontentloaded")
    # # print(product_page.inner_text())
    # product_page.wait_for_timeout(2000)
    # product_page.close()


def sort_by_dropdown(page):
    result = page.get_by_text("Best Match").first.click()
    result = page.get_by_text("Price low to high").first.click()

    page.wait_for_timeout(2000)


def check_daraz_price(prod_name: str, expected_price: int):
    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=False, executable_path=BROWSER_PATH, args=["--start-maximized"]
        )

        page = browser.new_page()

        page.goto("https://daraz.com.bd", wait_until="domcontentloaded")
        search_box = page.get_by_placeholder("Search in Daraz")
        # search_box = page.locator("input[type='search, input[name='q']").first
        page.wait_for_timeout(1000)
        search_box.fill(prod_name)
        search_box.press("Enter")

        page.wait_for_timeout(2000)
        # get_all_products(page=page)
        get_first_product_details(
            browser=browser, page=page, name="Motorola Edge 70 5g (8+256GB) Unofficial"
        )
        page.wait_for_timeout(5000)
        sort_by_dropdown(page=page)
        page.wait_for_timeout(5000)
        browser.close()


check_daraz_price("motorola", 10000)


# TODO:
# How to list the same class components
# Filter taka wihtout regex
"""

text = item.inner_text()

for line in text.splitlines():
    if line.startswith("৳"):
        price_text = line
        break

price_number = int(price_text.replace("৳", "").replace(",", "").strip())

print(price_text)
print(price_number)

"""

# How to get the link of the product?
"""
links = result.locator("a[href]")

first_link = links.nth(0).get_attribute("href")
second_link = links.nth(1).get_attribute("href")
third_link = links.nth(2).get_attribute("href")
"""
