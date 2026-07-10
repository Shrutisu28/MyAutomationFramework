from Pages.home_page import HomePage



def test_mybooking(test_page, test_data):

    home_page = HomePage(test_page)

    event_page = home_page.browse_events()

    booking_page = event_page.select_event(
        test_data["event_data"]["event_name"]
    )

    my_booking_page = booking_page.book_event(
        test_data["event_booking"]["full_name"],
        test_data["event_booking"]["email"],
        test_data["event_booking"]["phone_number"]
    )

    my_booking_page.verify_booking(
        test_data["event_data"]["event_name"]
    )

    my_booking_page.clear_all_bookings()