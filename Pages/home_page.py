from playwright.sync_api import expect

from Pages.event_page import EventPage
from Pages.my_booking_page import MyBookingsPage


class HomePage:

    def __init__(self, page):
        self.page = page

    def is_homepage_loaded(self):

       expect(self.page.get_by_text("Discover & Book")).to_be_visible()


    def browse_events(self):
        self.page.get_by_role("link", name="Browse Events →").click()
        expect(self.page.get_by_text("Upcoming Events")).to_be_visible()
        return EventPage(self.page)

    def my_booking(self):
        self.page.get_by_role("button", name="My Bookings").click()
        return MyBookingsPage(self.page)
