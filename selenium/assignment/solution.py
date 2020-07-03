from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import random

class Crawler:
    def __init__(self, is_headless=False):
        # for more info on arguments, see https://peter.sh/experiments/chromium-command-line-switches/
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        if is_headless:
            options.add_argument('--headless')
            # options.add_argument('headless')
        self.driver = webdriver.Chrome('../chromedriver', options=options)
        # wait up to 10 seconds for the elements to become available
        self.driver.implicitly_wait(10)

        self.dsi_url = 'http://webscraping-dsi1050.herokuapp.com/login'
        self.ebay_url = 'https://www.ebay.com/'
        self.amazon_url = 'https://www.amazon.com'

        self.static_word = None
        self.dynamic_word = None

    def login(self):
        self.driver.get(self.dsi_url)

        username = self.driver.find_element_by_css_selector('input[type=text]')
        password = self.driver.find_element_by_css_selector('input[type=password]')
        login = self.driver.find_element_by_css_selector('#login-form .button-primary')

        username.send_keys('bruno')
        password.send_keys('Blueno123!')
        login.click()

    def __set_static_word(self):
        # note this renders as such because of the implicitly_wait call in the constructor, 
        # if not, would have to use time.sleep() or something along those lines
        self.static_word = self.driver.find_element_by_css_selector('p:nth-of-type(2)').text.split()[-1]

    def __set_dynamic_word(self):
        render_word = self.driver.find_element_by_id('js-render-btn')
        render_word.click()
        self.dynamic_word = self.driver.find_element_by_id('js-val').text.split()[-1]

    def set_static_and_dynamic_words(self):
        self.login()
        self.__set_static_word()
        self.__set_dynamic_word()

    def quit_driver(self):
        self.driver.quit()

    def search_amazon(self, search_input):
        self.driver.get(self.amazon_url)
        self.__sleep_random_time_interval()
        searchbar = self.driver.find_element_by_css_selector('#twotabsearchtextbox')
        submit = self.driver.find_element_by_css_selector('#nav-search .nav-right .nav-input[type=submit]')
        self.__sleep_random_time_interval()
        searchbar.send_keys(search_input)
        self.__sleep_random_time_interval()
        submit.click()
        self.__sleep_random_time_interval()

    def run(self):
        self.set_static_and_dynamic_words()
        self.search_amazon(self.static_word)
        self.search_amazon(self.dynamic_word)

    def __sleep_random_time_interval(self):
        time.sleep(random.randint(1,5))

    

c = Crawler(is_headless=False)
c.run()
c.quit_driver()
