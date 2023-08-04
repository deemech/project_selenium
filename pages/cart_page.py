import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    trimmer = '//*[@class = "good-info__good-name"]'


    # Getters

    def get_trimmer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.trimmer)))

    # Methods

    def check_cart(self):
        self.get_current_url()
        time.sleep(2)
        self.make_screenshot()
        self.assert_word(self.get_trimmer(), 'Машинка для стрижки лошадей и КРС Xplorer, 2-я аккум.')



