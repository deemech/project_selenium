from selenium import webdriver

from pages.iphone_search_page import Iphone_search_page
from pages.main_page import Main_page


def test_searching_iphone():
    driver = webdriver.Chrome()

    print('lets search some iphone')

    main = Main_page(driver)
    main.search()
    sph = Iphone_search_page(driver)
    sph.filters()

    assert sph.get_filtered_price() >= 119000
