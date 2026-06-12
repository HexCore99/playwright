from app.daraz import Daraz


def test_product_price_equal(page):
    daraz_page = Daraz()

    search_name = "motorola"
    product_name = "Motorola Edge 70 5g (8+256GB) Unofficial"
    expected_price = 44999

    daraz_page.open_site(page)
    daraz_page.search_product(page, search_name)

    actual_price = daraz_page.get_product_price(page, product_name)
    assert actual_price == expected_price


def test_product_price_less_than_or_equal(page):
    daraz_page = Daraz()

    search_name = "motorola"
    product_name = "Motorola Edge 70 5g (8+256GB) Unofficial"
    maximum_price = 50000

    daraz_page.open_site(page)
    daraz_page.search_product(page, search_name)

    actual_price = daraz_page.get_product_price(page, product_name)

    assert actual_price <= maximum_price


def test_product_price_greater_than_or_equal(page):
    daraz_page = Daraz()

    search_name = "motorola"
    product_name = "Motorola Edge 70 5g (8+256GB) Unofficial"
    minimum_price = 40000

    daraz_page.open_site(page)
    daraz_page.search_product(page, search_name)

    actual_price = daraz_page.get_product_price(page, product_name)

    assert actual_price >= minimum_price
