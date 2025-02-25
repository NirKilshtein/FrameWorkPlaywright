import allure
from playwright.sync_api import expect

class TestLoginPage:
        
    @allure.feature("Login Tests")
    @allure.story("Login to OrangeHRM")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test Login Functionality with Valid Credentials")
    @allure.description("This test verifies that a user can log in successfully using valid credentials in the OrangeHRM application.")
    @allure.tag("smoke", "login", "UI")
    def test_first_tests(self, context):
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        page.get_by_placeholder("Username").fill("Admin")
        page.get_by_placeholder("Password").fill("admin123")
        text = page.locator('[type="email"]')
        text.fill("Test")
        expect(text).to_have_value("Test")


    @allure.feature("Multiple Tabs")
    def test_first_with_two_tabs(self, context):
        page = context.new_page()
        page.goto("https://google.co.il")

        page1 = context.new_page()
        page1.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        page1.get_by_placeholder("Username").fill("Admin")
        page1.get_by_placeholder("Password").fill("admin123")

        page.bring_to_front()
        text = page.locator('[type="email"]')
        text.fill("Test")
        expect(text).to_have_value("1")


    @allure.feature("Tab Switching")
    def test_switch_tabs(self, context):
        new_tab = context.new_page()
        new_tab.goto("https://google.com")

        print("New tab URL:", new_tab.url)
