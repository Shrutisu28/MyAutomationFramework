from Pages.home_page import HomePage


class LoginPage:

    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url


    def navigate(self):
        self.page.goto(self.base_url)


    def login(self, userEmail, userPassword):

        self.page.get_by_placeholder(
            "you@email.com"
        ).fill(userEmail)


        self.page.get_by_placeholder(
            "••••••"
        ).fill(userPassword)


        self.page.get_by_role(
            "button",
            name="Sign In"
        ).click()


        return HomePage(self.page)


    def get_error(self):

        return self.page.get_by_text(
            "Invalid email or password"
        )