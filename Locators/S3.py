
from selenium.webdriver.common.by import By

class S3Locators:
    CREATE_BUCKET_HOME_BUTTON = (By.LINK_TEXT, "Create bucket")

    BUCKET_CREATE_TITLE = (By.XPATH, "//h1[text()='Create bucket']")
    BUCKET_NAME_TEXTBOX = (By.XPATH, "//input[@id='bucket_name']")
    BUCKET_REGION_DROPDOWN = (By.XPATH, "//input[@id='zone']")
    BUCKET_CREATE_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and ./span/text()='Create bucket']")
    BUCKET_RADIO_BUTTON = lambda _name: (By.XPATH, f"//input[@type='radio' and ./../../../../tr/@data-row-key='{_name}']")

    BUCKET_UPLOAD_FILE_BUTTON = (By.LINK_TEXT, "Upload")
    ADD_FILES_BUTTON = (By.XPATH, "//button[./div/text()='Add files']")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")
    UPLOAD_FILE_SUBMIT_BUTTON = (By.XPATH, "//button[@type='button' and ./span/text()='Upload']")
