from playwright.sync_api import expect

from app.saucedemo import SauceDemo


def test_valid_login(page):
    username = "standard_user"
    password = "secret_sauce"

    sauce_demo = SauceDemo()
    sauce_demo.open_page(page=page)
    sauce_demo.login(page=page, username=username, password=password)

    assert "inventory.html" in page.url


def test_invalid_login(page):
    username = "standard"
    password = "secret_sauce"

    sauce_demo = SauceDemo()
    sauce_demo.open_page(page=page)
    sauce_demo.login(page=page, username=username, password=password)

    error_field = page.locator("[data-test=error]")
    assert error_field.is_visible()
    assert (
        "Username and password do not match any user in this service"
        in error_field.inner_text()
    )
    expect(error_field).to_contain_text(
        "Username and password do not match any user in this service"
    )
