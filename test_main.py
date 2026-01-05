from playwright.sync_api import Page

def test_data(page:Page):
    page.goto("https://www.opencart.com/index.php?route=common/home")
    page.locator("//a[@class='btn btn-link navbar-btn']").click()

    page.wait_for_timeout(50000)