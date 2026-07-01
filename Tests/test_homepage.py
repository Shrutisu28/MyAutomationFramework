
from Pages.Homepage import HomePage
from Tests.test_Login import test_valid_login


def test_homepage(page, test_data):
    test_valid_login(page, test_data)
    eventpage=HomePage(page)
    eventpage.browse_events()

def test_nobooking(page, test_data):
    test_valid_login(page, test_data)
    bookingpage = HomePage(page)
    bookingpage.my_booking()







