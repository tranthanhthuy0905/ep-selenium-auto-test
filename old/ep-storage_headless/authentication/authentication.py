import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestAuthentication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.set_window_size(1320, 750)
        self.driver.get("http://localhost:3000/s3/buckets")
        self.driver.add_cookie({'name': 'user-token',
                                'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MDkzYzA3NTExNjhhNWQ1ZTNlMjZkODMiLCJuYW1lIjoiaGFuZ2x0dDMiLCJpYXQiOjE2MjA2OTI4MzksImV4cCI6MTYyMDc3OTIzOX0.Mlc38fkVjdwgr0anEPOA-ZgK04h1_mbkH78eANjbfAU'})
        self.driver.implicitly_wait(10)

    def test_case_login_success(self):
        self.driver.get("http://localhost:3000/s3/buckets")
        self.assertIn("http://localhost:3000/s3/buckets", self.driver.current_url)
        time.sleep(5)

    def tearDown(self):
        # pass
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
    
