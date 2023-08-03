import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class Iphone_search_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    filter_popular = '//*[@class="dropdown-filter__btn dropdown-filter__btn--sorter"]'
    filter_color = '//*[text()="Цвет"]'
    price_high_to_low = '//*[text()="По убыванию цены"]'
    color_grey = '//*[text()="серый"]'

    # Getters

    def get_filter_popular(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_popular)))

    def get_filter_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_color)))

    def get_price_high_to_low(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_high_to_low)))

    def get_color_grey(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_grey)))

    def get_filtered_price(self):
        # Метод для получения списка продуктов по фильтрам
        product_element = self.driver.find_element(By.XPATH, '//*[@id="c149295404"]/div/a')
        product_price_text = product_element.find_element(By.XPATH, '//*[@id="c149295404"]/div/div[3]/p/span/ins').text
        product_price = float(product_price_text.replace(' ₽', '').replace(' ', ''))  # Преобразуем текст цены в число
        print(product_price)
        return product_price
    # Actions

    def click_filter_popular(self):
        self.get_filter_popular().click()
        print('popular clicked')

    def click_price_high_to_low(self):
        time.sleep(3)
        self.get_price_high_to_low().click()
        print('Price high2low chosen')

    def click_filter_color(self):
        self.get_filter_color().click()
        print('color filter opened')

    def click_grey_color(self):
        self.get_color_grey().click()
        print('chose grey color')

    # Methods

    def filters(self):
        self.click_filter_popular()
        self.click_price_high_to_low()
        self.click_filter_color()
        self.click_grey_color()
        time.sleep(10)


