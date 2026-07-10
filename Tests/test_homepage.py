
from Pages.home_page import HomePage

def test_homepage(test_page):

    eventpage=HomePage(test_page)
    eventpage.browse_events()

def test_nobooking(test_page):
    bookingpage = HomePage(test_page)
    bookingpage.my_booking()







