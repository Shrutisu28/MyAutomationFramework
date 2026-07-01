from Config.Config import BASE_URL
from Pages.Homepage import HomePage


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
            self.page.goto(BASE_URL)

    def login(self, userEmail, userPassword):
            self.page.get_by_placeholder("you@email.com").fill(userEmail)
            self.page.get_by_placeholder("••••••").fill(userPassword)
            self.page.get_by_role("button", name="Sign In").click()
            return HomePage(self.page)

    def get_error(self):
        return self.page.get_by_text("Invalid email or password")







