from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions

from task2.log import LoggingProxy
from task2.pages.locators import HeaderLocators, FloatingMenuLocators


class BasePage(LoggingProxy):

    def __init__(self, driver, url="", wait=10):
        super().__init__()
        self.driver = driver
        self.base_url = url
        self.wait = wait

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(conditions.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(conditions.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def wait_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(conditions.visibility_of_any_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def load(self):
        return self.driver.get(self.base_url)

    def switch_language(self, language):
        menu_button = self.find_element(HeaderLocators.ALL_MENU)
        if language == "English - EN" and menu_button.text == "All":
            self.info("The language is already English, don't need to change")
            return
        self.find_element(HeaderLocators.LANGUAGE).click()
        lang_items = self.find_elements(HeaderLocators.LANGAUGE_OPTIONS)
        for lang in lang_items:
            if lang.text.startswith(language):
                self.info(f"Select language '{lang.text}'")
                lang.click()

    def select_menu(self, *args):
        menu_button = self.find_element(HeaderLocators.ALL_MENU)
        menu_button.click()
        self.wait_visible(FloatingMenuLocators.MENU)
        wait_back = 0 if len(args) == 1 else 1

        for item_name in args:
            menu_items = self.find_elements(FloatingMenuLocators.MENU_ITEM)
            for menu_item in menu_items:
                if menu_item.text.lower() == item_name.lower():
                    self.info(f"Select menu '{menu_item.text}'")
                    menu_item.click()
                    if wait_back:
                        self.wait_visible(FloatingMenuLocators.BACK_TO_MAIN_MENU)
                        wait_back = 0
                    break

    def go_to_bucket(self):
        self.find_element(HeaderLocators.CART).click()
