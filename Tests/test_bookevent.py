import pytest

from Pages.Homepage import HomePage
from Tests.test_Login import test_valid_login


def test_event_booking(page, test_data):
    test_valid_login(page, test_data)
    home = HomePage(page)
    eventpage=home.browse_events()
    bookingpage=eventpage.select_event(test_data["event_data"]["event_name"])
    mybookingpage=bookingpage.book_event(test_data["Event_Booking"]["Full_Name"], test_data["Event_Booking"]["Email"], test_data["Event_Booking"]["Phone_number"])

    mybookingpage.verify_booking(test_data["event_data"]["event_name"])
    mybookingpage.clear_all_bookings()




