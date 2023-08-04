from selenium import webdriver

from pages.cart_page import Cart_page
from pages.horse_filter_page import Horse_filter_page
from pages.main_page import Main_page


def test_cart():
    driver = webdriver.Chrome()

    print('go buy some horse staff')

    main = Main_page(driver)
    main.go_horses()
    hp = Horse_filter_page(driver)
    hp.add_trim_and_go2cart()
    cp = Cart_page(driver)
    cp.check_cart()