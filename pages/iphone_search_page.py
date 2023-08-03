from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class Iphone_search_page(Base):

    def __init__(self, driver):
        super.__init__(driver)
        self.driver = driver

    #Locators

    filter_popular = '//*[@id="OGJjNzM0NzYtNWNkZS1jN2Q4LTQwZTgtNDYxOGVjZTAyZDA1"]/button'
    filter_color = '//*[@id="YzExZWEzMmUtZTI1Ni01MTIwLWNkZjAtOGRhZTM4Mjg1MjE1"]/button'
    price_high_to_low = '//*[@id="OGJjNzM0NzYtNWNkZS1jN2Q4LTQwZTgtNDYxOGVjZTAyZDA1"]/div/div/ul/li[4]/div/span[2]'
    color_grey = '//*[@id="OGJjNzM0NzYtNWNkZS1jN2Q4LTQwZTgtNDYxOGVjZTAyZDA1"]/div/div/ul/li[4]/div/span[2]'

    #Getters

    def get_filter_popular(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(By.XPATH, self.filter_popular))

    def get_filter_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(By.XPATH, self.filter_color))

    def get_price_high_to_low(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(By.XPATH, self.price_high_to_low))

    def get_color_grey(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(By.XPATH, self.color_grey))

    def get_filtered_phones(self):
        #Метод для получения списка продуктов по фильтрам
        products = []
        product_elements = self.driver.find_elements(By.XPATH, '//*[@class="product-card product-card--hoverable j-card-item"]')
        for element in product_elements:
            #парсим цену
            product_price = element.find_element(By.XPATH, ".//*[@class='price__lower-price']")
            products.append(product_price)
        print(products)

    #Actions

    def click_filter_popular(self):
        self.get_filter_popular().click()
        print('popular clicked')

    def click_price_high_to_low(self):
        self.get_price_high_to_low().click()
        print('Price high2low chosen')

    def click_filter_color(self):
        self.get_filter_color().click()
        print('color filter opened')

    def click_grey_color(self):
        self.get_color_grey().click()
        print('chose grey color')


    #Methods

    def filters(self):
        self.click_filter_popular()
        self.click_price_high_to_low()
        self.click_filter_color()
        self.click_grey_color()
        self.get_filtered_phones()



