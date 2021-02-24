from task2.pages.base_page import BasePage
from task2.pages.locators import BucketLocators


class BucketPage(BasePage):

    def get_items_title(self):
        self.wait_visible(BucketLocators.SUBTOTAL)
        items_titles = self.find_elements(BucketLocators.ITEM_TITLE)
        titles = []
        for item in items_titles:
            titles.append(item.text)
        return titles
