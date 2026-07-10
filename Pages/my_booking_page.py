from playwright.sync_api import expect



class MyBookingsPage:
 def __init__(self, page):
     self.page=page


 def verify_booking(self, event_name):

     booking_card=self.page.get_by_text(event_name).first
     expect(booking_card).to_be_visible()


 def clear_all_bookings(self):

     self.page.on("dialog", lambda dialog: dialog.accept())
     self.page.get_by_role("button", name="Clear all bookings").click()
     expect(self.page.get_by_text("No bookings yet")).to_be_visible()






