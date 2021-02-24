from selenium.webdriver.common.by import By


# --- Navigation Menu Locators ---
class HeaderLocators(object):
    CART = (By.ID, "nav-cart")
    LOGO = (By.ID, "nav-logo")
    SEARCH = (By.ID, "twotabsearchtextbox")
    ALL_MENU = (By.ID, "nav-hamburger-menu")
    LANGUAGE = (By.ID, "icp-nav-flyout")
    LANGAUGE_OPTIONS = (By.CSS_SELECTOR, "span.a-radio-label")


# --- Floating Menu Locators ---
class FloatingMenuLocators(object):
    MENU = (By.ID, "hmenu-canvas")
    VISIBLE_MENU = (By.CSS_SELECTOR, ".hmenu-visible")
    MENU_TITLE = (By.CSS_SELECTOR, ".hmenu-title")
    MENU_ITEM = (By.CSS_SELECTOR, ".hmenu-item")
    BACK_TO_MAIN_MENU = (By.CSS_SELECTOR, ".hmenu-back-button")


# --- Filter Menu Locators
class FilterMenuLocators(object):
    DEPARTMENT_ITEM = (By.CSS_SELECTOR, "#departments li span.a-list-item")


# --- Search Page Locators
class SearchResultsLocators(object):
    FILTER = (By.ID, "s-refinements")
    SORT = (By.CSS_SELECTOR, "#a-autoid-0")
    SORT_VALUES = (By.CSS_SELECTOR, "#s-result-sort-select option")
    SORT_ITEMS = (By.CSS_SELECTOR, "div.a-popover-wrapper a.a-dropdown-link")
    AVAILABLE_ITEMS = (By.CSS_SELECTOR, ".s-result-list h2")


# --- Item Page Locators ---
class ItemLocators(object):
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    TITLE = (By.ID, "productTitle")
    PRICE = (By.ID, "price_inside_buybox")


# --- Cart Page Locators ---
class BucketLocators(object):
    ITEM = (By.CSS_SELECTOR, ".sc-list-item")
    ITEM_TITLE = (By.CSS_SELECTOR, "span.sc-product-title")
    SUBTOTAL = (By.CSS_SELECTOR, ".sc-subtotal-activecart")
