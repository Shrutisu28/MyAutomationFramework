from playwright.sync_api import expect

from Pages.Bookeventpage import BookEventPage


class EventPage:

    def __init__(self, page):
        self.page = page
        self.search_box = page.get_by_placeholder("Search events, venues…")

    def event_search(self, search_text, event_name):
        self.search_box.fill(search_text)
        expect(self.page.get_by_text(event_name)).to_be_visible()
        self.search_box.clear()

    def select_event(self, event_name):
        event_card = self.page.locator(".p-4").filter(has_text=event_name)
        event_card.get_by_role("link", name="Book Now").click()
        return BookEventPage(self.page)


