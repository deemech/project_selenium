import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):
    url = 'https://www.wildberries.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    search_panel = '//*[@id="searchInput"]'
    burger_menu = '/html/body/div[1]/header/div/div[2]/div[1]/button'
    zoo_staff = '/html/body/div[2]/div/div[2]/ul/li[14]/a'
    horses_staff = '/html/body/div[2]/div/div[3]/div/div[14]/div/div[1]/ul/li[5]/a'

    # Getters

    def get_search_panel(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_panel)))

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_zoo_staff(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zoo_staff)))

    def get_horses_staff(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.horses_staff)))

    # Actions

    def search_iphone(self):
        time.sleep(5)
        self.get_search_panel().send_keys("iphone 13 pro max\n")
        print('searching for new phone')

    def click_burger_menu(self):
        self.get_burger_menu().click()
        print('Burger menu opened')

    def click_zoo_staff(self):
        self.get_zoo_staff().click()
        print('Zoo menu opened')

    def click_horses_staff(self):
        self.get_horses_staff().click()
        print('Lets find horses things')

    # Methods

    def search(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.search_iphone()

    def go_horses(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_burger_menu()
        self.click_zoo_staff()
        self.click_horses_staff()
