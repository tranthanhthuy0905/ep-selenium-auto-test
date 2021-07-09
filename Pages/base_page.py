from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import logging


class BasePage(object):
    def __init__(self, driver, base_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def authenticate(self, user_token):
        _cookie = { "name": "user-token", "value": user_token}
        self.driver.add_cookie(_cookie)
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        if "session/signin" in self.driver.current_url:
            self.driver.quit()
            logging.error("Something's wrong with authentication. Test cancelled.")
            raise Exception("Authentication may not be successful. User-token may need to be updated!")
        logging.info(f"Authenticated successfully to {self.base_url}")

    def access_page(self):
        self.driver.get(self.base_url)
        logging.info(f"Access to {self.base_url}")

    def find_element(self, *locator):
        try:
            return self.driver.find_element(*locator)
        except TimeoutException:
            _msg = "\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1])
            logging.error(_msg)
            print(_msg)
            self.driver.get_screenshot_as_file('error_snapshot/{filename}.png'.format(filename='find_element'))
            self.driver.quit()

    def open(self, url):
        try:
            url = self.base_url + url
            self.driver.get(url)
        except TimeoutException:
            self.driver.get_screenshot_as_file('error_snapshot/{filename}.png'.format(filename='open_url'))
            self.driver.quit()

    def get_title(self):
        try:
            return self.driver.title
        except TimeoutException:
            self.driver.get_screenshot_as_file('error_snapshot/{filename}.png'.format(filename='get_title'))
            self.driver.quit()

    def get_url(self):
        try:
            return self.driver.current_url
        except TimeoutException:
            self.driver.get_screenshot_as_file('error_snapshot/{filename}.png'.format(filename='get_url'))
            self.driver.quit()

    def hover(self, *locator):
        try:
            element = self.find_element(*locator)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
        except TimeoutException:
            self.driver.get_screenshot_as_file('error_snapshot/{filename}.png'.format(filename='hover'))
            self.driver.quit()

    def click_button(self, locator):
        try:
            self.find_element(*locator).click()
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file('error_snapshot/{filename}.png'.format(filename='click_button'))
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()

    def click_button_and_return_page(self, locator, page):
        try:
            self.find_element(*locator).click()
            return page
        except TimeoutException:
            self.driver.get_screenshot_as_file('error_snapshot/{filename}.png'.format(filename='click_button_and_return_page'))
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()

    def wait_and_click_button(self, locator):
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='wait_and_click_button'))
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()

    def check_element_existence(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
            logging.info(f"CHECK ELEMENT EXISTENCE: Element {locator} exists.")
            return self
        except TimeoutException:
            _msg = "\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1])
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='check_element_existence'))
            print(_msg)
            logging.error(f"CHECK ELEMENT EXISTENCE: Element {locator} does not exist.")
            self.driver.quit()
            return False

    def fill_form(self, value, locator):
        try:
            form = self.find_element(*locator)
            form.send_keys(Keys.COMMAND + "a" + Keys.DELETE)
            form.send_keys(value)
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='fill_form'))
            self.driver.quit()
