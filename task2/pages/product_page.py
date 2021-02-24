from task2.pages.base_page import BasePage
from task2.pages.locators import ItemLocators


class ProductPage(BasePage):

    def get_name(self):
        return self.find_element(ItemLocators.TITLE).text

    def add_to_cart(self):
        self.find_element(ItemLocators.ADD_TO_CART).click()
