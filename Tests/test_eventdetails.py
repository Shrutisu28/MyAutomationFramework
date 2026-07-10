from Pages.home_page import HomePage
from Tests.test_login import test_valid_login


def test_event_details(test_page, test_data):

    homepage = HomePage(test_page)
    eventpage = homepage.browse_events()
    eventpage.event_search(test_data["event_data"]["search_text"], test_data["event_data"]["event_name"])
    eventpage.select_event(test_data["event_data"]["event_name"])
