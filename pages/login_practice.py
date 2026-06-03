from playwright.sync_api import Page



class LoginPage(Page):
    def __init__(self, page: Page):
        """
        Constructor to initialize the Playwright page object
        and define all necessary locators.
        """

        self.page = page

        # ===== Locators =====
        # Using Playwright's 'locator' method to identify UI elements
        self.txt_email = page.get_by_placeholder("E-Mail Address")
        self.txt_password = page.get_by_placeholder("Password")
        self.button_login = page.locator("input[type='submit']")
        self.alert_error_message = page.locator("div .alert.alert-danger.alert-dismissible")


    def enter_email(self, email):
        """Enter the email address in the Email field."""
        try:
            self.txt_email.fill(email)
        except Exception as e:
            print(f" Exception while entering email: {e}")
            raise


    def enter_password(self, password):
        """Enter the password in the Password field."""
        try:
            self.txt_password.fill(password)
        except Exception as e:
            print(f" Exception while entering password: {e}")
            raise


    def click_login(self):
        """Click the login button."""
        try:
            self.button_login.click()
        except Exception as e:
            print(f" Exception while clicking login: {e}")


    def get_login_error(self):
        """
        Return the error message element if login fails.
        Example use:
            error_text = login_page.get_login_error().inner_text()
        """
        try:
            return self.alert_error_message
        except Exception as e:
            print(f" Exception while fetching login error message: {e}")
            return None

    def login(self, email, password):
        try:
            self.txt_email.fill(email)
            self.txt_password.fill(password)
            self.button_login.click()
        except Exception as e:
            print(f" Exception while logging in: {e}")
            raise



