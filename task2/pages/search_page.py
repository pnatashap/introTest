from task2.pages.base_page import BasePage
from task2.pages.locators import SearchResultsLocators, FilterMenuLocators


class SearchPage(BasePage):

    def choose_category(self, name):
        self.wait_visible(SearchResultsLocators.FILTER)
        departments = self.find_elements(FilterMenuLocators.DEPARTMENT_ITEM)
        for dep in departments:
            if dep.text.lower() == name.lower():
                self.logger.info(f"Select department {dep.text}")
                dep.click()
                break

    def select_sort(self, sort_by):
        self.wait_visible(SearchResultsLocators.SORT)
        current_sort = self.find_elements(SearchResultsLocators.SORT_VALUES)
        for item in current_sort:
            if item.is_selected():
                if item.text.lower() == sort_by.lower():
                    self.logger.info("Sorting is already correct")
                    return
                else:
                    self.logger.info(f"Current sort is '{item.text}'. Going to change it to '{sort_by}'")
                    break
        # change sort
        sort = self.find_element(SearchResultsLocators.SORT)
        sort.click()
        sort_items = self.find_elements(SearchResultsLocators.SORT_ITEMS)
        for item in sort_items:
            if item.text.lower() == sort_by.lower():
                item.click()
                break

    def open_item(self, n):
        items = self.find_elements(SearchResultsLocators.AVAILABLE_ITEMS)
        items[n].click()
