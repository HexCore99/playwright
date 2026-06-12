class SauceDemo:
    def __init__(self) -> None:
        self.url = "https://www.saucedemo.com/"
        self.username_id = "user-name"
        self.password_id = "password"
        self.login_button_id = "login-button"

    def open_page(self, page) -> None:
        page.goto(self.url, wait_until="domcontentloaded")

    def login(self, page, username, password):
        page.wait_for_timeout(2000)
        page.locator(f"#{self.username_id}").fill(username)
        page.locator(f"#{self.password_id}").fill(password)
        page.locator(f"#{self.login_button_id}").click()
        page.wait_for_timeout(2000)
