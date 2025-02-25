from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.locator('role=textbox[name="Email address"]')
        self.password_input = page.locator('role=textbox[name="Password"]')
        self.login_button = page.locator('role=button[name="Login"]')

    def enter_email(self, email: str):
        self.email_input.click()
        self.email_input.fill(email)

    def enter_password(self, password: str):
        self.password_input.click()
        self.password_input.fill(password)


    def submit_login(self):
        self.login_button.click()

    def login(self, email: str, password: str):
        self.enter_email(email)
        self.enter_password(password)
        self.submit_login()
