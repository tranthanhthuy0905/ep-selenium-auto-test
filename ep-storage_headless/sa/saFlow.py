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

class TestSA(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        self.driver.set_window_size(1320, 750)
        self.driver.get("https://s3.engineering.vng.vn/s3/sa")
        self.driver.add_cookie({'name': 'user-token',
                                'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDlkYzFiNmY4ZjUxNWY0MmIzZjJmZTYiLCJpZCI6IjYwOWRjMWI2ZjhmNTE1ZjQyYjNmMmZlNiIsInN1YiI6IjYwOWRjMWI2ZjhmNTE1ZjQyYjNmMmZlNiIsIm5hbWUiOiJzZWxlbml1bSIsInNldHRpbmdzIjp7ImxheW91dFRoZW1lIjoic2xhdGVEYXJrMSIsInRpbWVab25lIjoiQXNpYS9Ib19DaGlfTWluaCJ9LCJ1c2VySW5mbyI6eyJidXNpbmVzc1Bob25lcyI6WyIwMzkzNjExODY2Il0sImVtcGxveWVlSWQiOiJWRy05OTk5OSIsImRpc3BsYXlOYW1lIjoiU2VsZW5pdW0iLCJkZXBhcnRtZW50IjoiUiZEIiwiam9iVGl0bGUiOiJTZW5pb3IgVGVzdGVyIiwibWFpbCI6InRlc3RAdm5nLmNvbS52biIsIm1vYmlsZVBob25lIjoiKCs4NCkgMDM5MzYxMTg2NiJ9LCJyb2xlcyI6WyJVU0VSIiwiQURNSU4iXSwicmlnaHQiOlsiVEVTVCJdLCJ1c2VyIjoic2VsZW5pdW0iLCJzdGF0dXMiOiJBQ1RJVkUiLCJpYXQiOjE2MjA5NTE2NjZ9.MiWBU2a-f_-C1BK9yHPKD3rmiA0FG3ABNT_z7YBzcko'})
        self.driver.implicitly_wait(10)

    def test_1case_create_sa(self):
        self.driver.get("https://s3.engineering.vng.vn/s3/sa")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/a/span").click()
        random_number = str(random.randint(1000,2000))
        self.driver.find_element_by_xpath("/html/body/div/section/section/main/div/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/div/div/input").send_keys('hangltt3-selenium-' + random_number)
        self.driver.find_element_by_xpath("/html/body/div/section/section/main/div/div/div/div/div/form/div[3]/div/div/div/div/button/span").click()
        # Service Account is created!
        element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[1]"))
        WebDriverWait(self.driver, 10).until(element_present)
        assert "Service Account is created!" in self.driver.page_source

    def test_2case_delete_sa(self):
        self.driver.get("https://s3.engineering.vng.vn/s3/sa")
        sa_names = self.driver.find_elements_by_xpath("/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]")
        for name in sa_names:
            time.sleep(2)
            name.find_element_by_class_name("ant-table-selection-column").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[2]/div").click()
            self.driver.find_element_by_xpath("/html/body/div[*]/div/div/ul/li").click()
            self.driver.find_element_by_xpath("/html/body/div[*]/div/div[2]/div/div[2]/div/div/div[*]/button[2]/span").click()
            # time.sleep(5)
            assert "Service account is deleting..." in self.driver.page_source

    def tearDown(self):
        # pass
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()