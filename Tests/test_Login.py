from playwright.sync_api import expect
from Pages.Loginpage import LoginPage


def test_valid_login(page, test_data):

    login_page = LoginPage(page)

    login_page.navigate()

    user = test_data["Valid_User"]
    username =user["Username"]
    password = user["Password"]
    login_page.login(username, password)



def test_invalid_login(page, test_data):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        test_data["Invalid_User"]["Username"],
        test_data["Invalid_User"]["Password"]
    )

    login_page.get_error()








