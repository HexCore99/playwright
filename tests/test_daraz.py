from app.daraz import Daraz


def test_daraz_product_price(page):
    daraz_page = Daraz()

    search_name = "motorola"
    product_name = "Motorola Edge 70 5g (8+256GB) Unofficial"
    expected_price = 10000

    daraz_page.open_site(page)
    daraz_page.search_product(page, search_name)

    actual_price = daraz_page.get_product_price(page, product_name)

    assert actual_price == expected_price


def test_daraz_search_results_count(page):
    daraz_page = Daraz()

    search_name = "motorola"

    daraz_page.open_site(page)
    daraz_page.search_product(page, search_name)

    product_count = daraz_page.get_all_products_count(page)

    assert product_count > 0
