# Playwright Python `expect()` Examples

Import first:

```python
import re
from playwright.sync_api import expect
```

---

# 1. Visibility Checks

## `to_be_visible()`

Checks that an element is visible.

```python
expect(page.locator("#login-button")).to_be_visible()
```

## `to_be_hidden()`

Checks that an element is hidden or not visible.

```python
expect(page.locator(".loading-spinner")).to_be_hidden()
```

## `to_be_in_viewport()`

Checks that an element is inside the visible screen area.

```python
expect(page.locator("#footer")).to_be_in_viewport()
```

---

# 2. Element State Checks

## `to_be_enabled()`

Checks that an element is enabled.

```python
expect(page.locator("#login-button")).to_be_enabled()
```

## `to_be_disabled()`

Checks that an element is disabled.

```python
expect(page.locator("#submit-button")).to_be_disabled()
```

## `to_be_editable()`

Checks that an input field can be edited.

```python
expect(page.locator("#user-name")).to_be_editable()
```

## `to_be_focused()`

Checks that an element is currently focused.

```python
page.locator("#user-name").click()
expect(page.locator("#user-name")).to_be_focused()
```

## `to_be_checked()`

Checks that a checkbox or radio button is checked.

```python
expect(page.locator("#remember-me")).to_be_checked()
```

## `to_be_empty()`

Checks that an element or input is empty.

```python
expect(page.locator("#user-name")).to_be_empty()
```

## `to_be_attached()`

Checks that an element exists in the DOM.

```python
expect(page.locator("#login-button")).to_be_attached()
```

---

# 3. Text Checks

## `to_have_text()`

Checks exact text.

```python
expect(page.locator(".title")).to_have_text("Products")
```

## `to_contain_text()`

Checks that an element contains specific text.

```python
expect(page.locator('[data-test="error"]')).to_contain_text(
    "Username and password do not match"
)
```

---

# 4. Input Value Checks

## `to_have_value()`

Checks the value inside an input field.

```python
page.locator("#user-name").fill("standard_user")
expect(page.locator("#user-name")).to_have_value("standard_user")
```

## `to_have_values()`

Checks selected values in a multi-select field.

```python
expect(page.locator("select")).to_have_values(["option1", "option2"])
```

---

# 5. Attribute / Class / ID Checks

## `to_have_attribute()`

Checks an HTML attribute.

```python
expect(page.locator("a")).to_have_attribute("href", "https://example.com/")
```

## `to_have_class()`

Checks the exact class value.

```python
expect(page.locator("#login-button")).to_have_class("submit-button btn_action")
```

## `to_contain_class()`

Checks that an element contains a specific class.

```python
expect(page.locator("#login-button")).to_contain_class("btn_action")
```

## `to_have_id()`

Checks the element ID.

```python
expect(page.locator("#login-button")).to_have_id("login-button")
```

---

# 6. CSS / JavaScript Property Checks

## `to_have_css()`

Checks a CSS property.

```python
expect(page.locator("#login-button")).to_have_css("display", "block")
```

## `to_have_js_property()`

Checks a JavaScript property.

```python
expect(page.locator("#remember-me")).to_have_js_property("checked", True)
```

---

# 7. Count Checks

## `to_have_count()`

Checks how many elements match a locator.

```python
expect(page.locator(".inventory_item")).to_have_count(6)
```

---

# 8. Page Checks

## `to_have_title()`

Checks the page title.

```python
expect(page).to_have_title("Swag Labs")
```

## `to_have_url()`

Checks the page URL.

```python
expect(page).to_have_url(re.compile(".*inventory.html"))
```

---

# 9. Accessibility Checks

## `to_have_role()`

Checks the ARIA role.

```python
expect(page.locator("#login-button")).to_have_role("button")
```

## `to_have_accessible_name()`

Checks the accessible name of an element.

```python
expect(page.locator("button")).to_have_accessible_name("Login")
```

## `to_have_accessible_description()`

Checks the accessible description of an element.

```python
expect(page.locator("#help-icon")).to_have_accessible_description("Help information")
```

## `to_match_aria_snapshot()`

Checks the accessibility tree snapshot.

```python
expect(page.locator("body")).to_match_aria_snapshot("""
- button "Login"
""")
```

---

# 10. Response Checks

## `to_be_ok()`

Checks that the HTTP response status is OK.

```python
response = page.goto("https://www.saucedemo.com/")
expect(response).to_be_ok()
```

---

# 11. Soft Assertions

Soft assertions do not stop the test immediately if they fail.  
The test continues, but pytest still marks the test as failed.

```python
expect.soft(page.locator(".title")).to_have_text("Products")
expect.soft(page.locator(".inventory_item")).to_have_count(6)
expect.soft(page.locator("#shopping_cart_container")).to_be_visible()
```

---

# 12. Custom Expect Message

You can add a custom message to explain what the check is doing.

```python
expect(
    page.locator("#login-button"),
    "Login button should be visible on login page"
).to_be_visible()
```

---

# 13. Custom Timeout

## Per assertion timeout

```python
expect(page.locator(".inventory_item")).to_have_count(6, timeout=10000)
```

## Global timeout

Add this in `conftest.py`:

```python
from playwright.sync_api import expect

expect.set_options(timeout=10000)
```

---

# 14. Most Useful Examples for Exam

## Check login success URL

```python
expect(page).to_have_url(re.compile(".*inventory.html"))
```

## Check error message visible

```python
expect(page.locator('[data-test="error"]')).to_be_visible()
```

## Check error message text

```python
expect(page.locator('[data-test="error"]')).to_contain_text(
    "Username and password do not match"
)
```

## Check product count

```python
expect(page.locator(".inventory_item")).to_have_count(6)
```

## Check page title

```python
expect(page).to_have_title("Swag Labs")
```

## Check input value

```python
page.locator("#user-name").fill("standard_user")
expect(page.locator("#user-name")).to_have_value("standard_user")
```

## Check button enabled

```python
expect(page.locator("#login-button")).to_be_enabled()
```

## Check element hidden

```python
expect(page.locator(".loading-spinner")).to_be_hidden()
```

---

# 15. Quick Rule

Use `expect()` for checking UI/page elements:

```python
expect(page.locator("#login-button")).to_be_visible()
```

Use `assert` for checking normal Python values:

```python
actual_price = 44999
expected_price = 44999

assert actual_price == expected_price
```
