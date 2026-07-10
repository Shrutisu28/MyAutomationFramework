from Pages.home_page import HomePage
from Pages.login_page import LoginPage


def test_valid_login(test_page):

    home_page = HomePage(test_page)
    home_page.is_homepage_loaded()

def test_invalid_login(invalid_login_page, test_data, env_config):

    login_page = LoginPage(invalid_login_page,env_config["base_url"] )

    login_page.navigate()


    login_page.login(
        test_data["invalid_user"]["username"],
        test_data["invalid_user"]["password"]
    )

