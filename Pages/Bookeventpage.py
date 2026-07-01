from playwright.sync_api import expect

from Pages.MyBookingpage import MyBookingsPage


class BookEventPage:
    def __init__(self, page):
        self.page = page

    def book_event(self, fullname, email, phonenumber):
            self.page.get_by_placeholder("Your full name").fill(fullname)
            self.page.get_by_placeholder("you@email.com").fill(email)
            self.page.get_by_placeholder("+91 98765 43210").fill(phonenumber)
            self.page.get_by_role("button", name="Confirm Booking").click()
            expect(self.page.get_by_text("Booking Confirmed")).to_be_visible()
            self.page.get_by_role("button", name="View My Bookings").click()
            return MyBookingsPage(self.page)