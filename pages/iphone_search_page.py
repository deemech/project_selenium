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
        #  Тут немного лирического отступления:
        # У меня сначала была идея сравнить цены всех отфильтрованных товаров, путем добавления их в массив. Даже написал для этого код
        #      products = []
        #  product_elements = self.driver.find_elements(By.XPATH, '//*[@class="product-card product-card--hoverable j-card-item"]')
        #  for element in product_elements:
        #          Парсим цену продукта и добавляем в список
        #          product_price_text = element.find_element(By.XPATH, ".//*[@class='price__lower-price']").text
        #         product_price = float(product_price_text.replace(' ₽', '').replace(' ', ''))  # Преобразуем текст цены в число
        #          products.append(product_price)
        # print(products)
        # return products
        #  Но он не заработал как надо, получалось парсить какой-то рандомный элемент, и он уходил в массив в одиночестве
        #  Так и не поняв, как решить проблему, я просто записал следующий код
        product_element = self.driver.find_element(By.XPATH, '//*[@id="c149295404"]/div/a')
        # Тут я специально оставил из старого метода вычленение одного элемента из другого путем xpath, потому что это прикольно
        product_price_text = product_element.find_element(By.XPATH, '//*[@id="c149295404"]/div/div[3]/p/span/ins').text
        product_price = float(product_price_text.replace(' ₽', '').replace(' ', ''))  # Преобразуем текст цены в число
        print('most expensive phone coast ' + str(product_price))
        return product_price
        # А потом в тесте я сравниваю цену с ценой немного меньше самой дорогой на текущий момент. Не думаю, что они подешевеют(

    # Actions

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

    # Methods

    def filters(self):
        self.get_current_url()
        self.click_filter_popular()
        self.click_price_high_to_low()
        self.click_filter_color()
        self.click_grey_color()
        time.sleep(5)


