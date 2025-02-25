import pytest
from Pages.login_page import LoginPage
from playwright.sync_api import expect
from playwright.sync_api import sync_playwright, Page

class TestLoginPage:

    @pytest.fixture(autouse=True)
    def class_setup(self, page):
        page.goto("http://www.google.com")
        self.login_page = LoginPage(page)

    def test_valid_login(self, page: Page):
        # self.login_page.login("firstname@gmail.com", "Aa123456!")
        page.goto("https://www.google.co.il")
        expect(page).to_have_title("Google")    
        print(page.title())
        expect(page).to_have_url("https://www.google.co.il/")

        
        