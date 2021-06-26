
from selenium.webdriver.common.by import By

class S3Locators:
    CREATE_BUCKET_HOME_BUTTON = (By.LINK_TEXT, "Create bucket")

    BUCKET_CREATE_TITLE = (By.XPATH, "//h1[text()='Create bucket']")
    BUCKET_NAME_TEXTBOX = (By.XPATH, "//input[@id='bucket_name']")
    BUCKET_REGION_DROPDOWN = (By.XPATH, "//input[@id='zone']")
    # BUCKET_CREATE_SUBMIT_BUTTON = (By.XPATH, "//span[text()='Create bucket']")
    BUCKET_CREATE_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and ./span/text()='Create bucket']")
