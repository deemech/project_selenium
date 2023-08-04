import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Horse_filter_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    trimmer_card = '//*[@id="c156222287"]/div/a'
    horse_trimmer = '//*[@id="c156222287"]/div/div[4]/p[3]/a'
    cart = '//*[@id="basketContent"]/div[3]/a/span'
    filter_popular = '//*[text()="По популярности"]'
    price_high_to_low = '//*[text()="По убыванию цены"]'

    # Getters

    def get_horse_trimmer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.horse_trimmer)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_filter_popular(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_popular)))

    def get_price_high_to_low(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_high_to_low)))

    def get_trimmer_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.trimmer_card)))

        # Actions

    def click_filter_popular(self):
        self.get_filter_popular().click()
        print('popular clicked')

    def click_price_high_to_low(self):
        self.get_price_high_to_low().click()
        print('Price high2low chosen')

    def click_horse_trimmer(self):
        ActionChains(self.driver).move_to_element(self.get_trimmer_card()).perform()
        self.get_horse_trimmer().click()
        print('add horse trimmer to cart')

    def go_to_cart(self):
        self.get_cart().click()
        print('go to cart')

    # Methods

    def add_trim_and_go2cart(self):
        self.get_current_url()
        self.click_filter_popular()
        self.click_price_high_to_low()
        self.click_horse_trimmer()
        time.sleep(1)
        self.go_to_cart()
