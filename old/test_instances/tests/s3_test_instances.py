import unittest
import time
import random
import os
import pyautogui

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# from locators.cookies import get_cookie
cookie = {"name": "user-token",
          "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDlkYzFiNmY4ZjUxNWY0MmIzZjJmZTYiLCJpZCI6IjYwOWRjMWI2ZjhmNTE1ZjQyYjNmMmZlNiIsInN1YiI6IjYwOWRjMWI2ZjhmNTE1ZjQyYjNmMmZlNiIsIm5hbWUiOiJzZWxlbml1bSIsInNldHRpbmdzIjp7ImxheW91dFRoZW1lIjoic2xhdGVEYXJrMSIsInRpbWVab25lIjoiQXNpYS9Ib19DaGlfTWluaCJ9LCJ1c2VySW5mbyI6eyJidXNpbmVzc1Bob25lcyI6WyIwMzkzNjExODY2Il0sImVtcGxveWVlSWQiOiJWRy05OTk5OSIsImRpc3BsYXlOYW1lIjoiU2VsZW5pdW0iLCJkZXBhcnRtZW50IjoiUiZEIiwiam9iVGl0bGUiOiJTZW5pb3IgVGVzdGVyIiwibWFpbCI6InRlc3RAdm5nLmNvbS52biIsIm1vYmlsZVBob25lIjoiKCs4NCkgMDM5MzYxMTg2NiJ9LCJyb2xlcyI6WyJVU0VSIiwiQURNSU4iXSwicmlnaHQiOlsiVEVTVCJdLCJ1c2VyIjoic2VsZW5pdW0iLCJzdGF0dXMiOiJBQ1RJVkUiLCJpYXQiOjE2MjA5NTE2NjZ9.MiWBU2a-f_-C1BK9yHPKD3rmiA0FG3ABNT_z7YBzcko"}


class TestBucket(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.set_window_size(1320, 750)
        self.driver.get("https://s3.engineering.vng.vn/s3/buckets")
        # cookie = get_cookie()
        self.driver.add_cookie(cookie)
        self.driver.implicitly_wait(10)

    def test_1case_create_bucket(self):
        self.driver.get("https://s3.engineering.vng.vn/s3/buckets")
        self.driver.find_element_by_link_text("Create bucket").click()
        self.assertIn("https://s3.engineering.vng.vn/s3/buckets/create", self.driver.current_url)
        random_number = str(random.randint(1000, 2000))
        self.driver.find_element_by_id("bucket_name").send_keys('hangltt3-selenium-' + random_number)
        region = self.driver.find_element_by_id("zone")
        region.send_keys('zoneshare-staging')
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.driver.find_elements_by_xpath(
            "/html/body/div[1]/section/section/main/div/div/div/div/form/div[3]/div/div/div/div/button/span")[0].click()
        element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[1]"))
        WebDriverWait(self.driver, 10).until(element_present)
        time.sleep(1)
        assert "Created bucket" in self.driver.page_source
        self.assertIn("https://s3.engineering.vng.vn/s3/buckets/" + "hangltt3-selenium-" + random_number,
                      self.driver.current_url)

    def test_2case_upload_file(self):
        self.driver.get("https://s3.engineering.vng.vn/s3/buckets/")
        time.sleep(3)
        bucket = self.driver.find_element_by_class_name("ant-table-row-level-0")
        time.sleep(3)
        bucket.find_element_by_xpath(
            "/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/a/span").click()
        time.sleep(3)
        element_present = EC.presence_of_element_located((By.XPATH,
                                                          "/html/body/div/section/section/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/span/div/span/button/div"))
        WebDriverWait(self.driver, 10).until(element_present).click()
        pyautogui.write('12.png')
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div/section/section/main/div/div/div/div/div/div[3]/button/span").click()
        time.sleep(3)

        assert "Upload file(s) successfully" in self.driver.page_source

    def test_3case_delete_file(self):
        self.driver.get("https://s3.engineering.vng.vn/s3/buckets")
        # time.sleep(1)
        bucket = self.driver.find_element_by_class_name("ant-table-row-level-0")
        bucket.find_element_by_xpath(
            "/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/a").click()
        # time.sleep(1)
        files = self.driver.find_elements_by_xpath(
            "/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[*]/table/tbody/tr[*]/td[*]/div/div")
        for file in files:
            file.click()
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[2]/div").click()
            self.driver.find_element_by_xpath("/html/body/div[*]/div/div/ul/li[2]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "/html/body/div[*]/div/div[2]/div/div[2]/div/div/div[*]/button[2]/span").click()
            # time.sleep(1)
            element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[*]/div/div/div/div/div/div[*]"))
            WebDriverWait(self.driver, 10).until(element_present)
            time.sleep(1)
            assert "Delete file is successful!" in self.driver.page_source

    def test_4case_delete_bucket(self):
        self.driver.get("https://s3.engineering.vng.vn/s3/buckets")
        bucket = self.driver.find_elements_by_class_name("ant-table-row-level-0")
        for btn in bucket:
            btn.find_elements_by_class_name("ant-radio-wrapper")[0].click()
            self.driver.find_elements_by_xpath(
                "/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[3]/div")[
                0].click()
            self.driver.find_elements_by_xpath("/html/body/div[*]/div/div/ul/li[2]")[0].click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "/html/body/div[*]/div/div[2]/div/div[2]/div/div/div[*]/button[2]/span").click()
            # time.sleep(4)
            element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[*]/div/div/div/div/div/div[*]"))
            WebDriverWait(self.driver, 10).until(element_present)
            time.sleep(1)
            assert "Delete bucket is successful!" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()