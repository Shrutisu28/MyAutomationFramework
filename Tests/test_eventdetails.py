from Pages.Homepage import HomePage
from Tests.test_Login import test_valid_login


def test_event_details(page, test_data):
    test_valid_login(page, test_data)
    homepage = HomePage(page)
    eventpage = homepage.browse_events()
    eventpage.event_search(test_data["event_data"]["search_text"], test_data["event_data"]["event_name"])
    eventpage.select_event(test_data["event_data"]["event_name"])
