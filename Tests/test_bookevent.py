
from Pages.home_page import HomePage



def test_event_booking(test_page, test_data):

    home = HomePage(test_page)
    eventpage=home.browse_events()
    bookingpage=eventpage.select_event(test_data["event_data"]["event_name"])
    mybookingpage=bookingpage.book_event(test_data["event_booking"]["full_name"], test_data["event_booking"]["email"], test_data["event_booking"]["phone_number"])

    mybookingpage.verify_booking(test_data["event_data"]["event_name"])
    mybookingpage.clear_all_bookings()




