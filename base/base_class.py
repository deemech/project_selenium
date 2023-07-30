import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """ Methods Get current URL"""

    def get_current_url(self):
        get_url = self.get_current_url()
        print('current url', get_url)

    """ Method assert word """

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('good word value')

    """ Method screenshot"""

    def make_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m%d.%H.%M.%S')
        screenshot_name = 'screenshot' + now_date + '.ng'
        self.driver.save_screenshot('C:\\prog\\java_maven_test\\helloci\\final_progect\\screen')

    """ Method assert url """

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert  get_url == result
        print('get value url')