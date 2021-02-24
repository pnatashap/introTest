from task2.pages.bucket_page import BucketPage
from task2.pages.main_page import MainPage
from task2.pages.product_page import ProductPage
from task2.pages.search_page import SearchPage


def test_amazon_bucket(browser):
    main_page = MainPage(browser)
    main_page.load()
    # use english language
    main_page.switch_language("English - EN")
    main_page.select_menu("Computers", "Computers & Tablets")
    search_page = SearchPage(browser)
    search_page.select_sort("Price: High to Low")
    search_page.choose_category("Laptops")


    selected_products = []
    for i in 0, 1:
        search_page.open_item(i)
        product_page = ProductPage(browser)
        selected_products.append(product_page.get_name())
        product_page.add_to_cart()
        browser.back()
        browser.back()
    # make sure that we select different products
    assert selected_products[0] != selected_products[1]

    main_page.go_to_bucket()
    bucket_page = BucketPage(browser)
    bucket_list = bucket_page.get_items_title()

    assert len(bucket_list) == 2
    diff = set(selected_products) ^ set(bucket_list)
    assert not diff
