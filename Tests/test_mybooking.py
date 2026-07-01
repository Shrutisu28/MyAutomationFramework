from Pages.Homepage import HomePage
from Tests.test_Login import test_valid_login


def test_mybooking(page, test_data):

    test_valid_login(page, test_data)

    home_page = HomePage(page)

    event_page = home_page.browse_events()

    booking_page = event_page.select_event(
        test_data["event_data"]["event_name"]
    )

    my_booking_page = booking_page.book_event(
        test_data["Event_Booking"]["Full_Name"],
        test_data["Event_Booking"]["Email"],
        test_data["Event_Booking"]["Phone_number"]
    )

    my_booking_page.verify_booking(
        test_data["event_data"]["event_name"]
    )

    my_booking_page.clear_all_bookings()