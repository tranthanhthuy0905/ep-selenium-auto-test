from selenium.webdriver.common.by import By

class S3Locators:
    CREATE_BUCKET_HOME_BUTTON = (By.LINK_TEXT, "Create bucket")

    BUCKET_CREATE_TITLE = (By.XPATH, "//h1[text()='Create bucket']")
    BUCKET_NAME_TEXTBOX = (By.XPATH, "//input[@id='bucket_name']")
    BUCKET_REGION_DROPDOWN = (By.XPATH, "//input[@id='zone']")
    BUCKET_CREATE_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and ./span/text()='Create bucket']")
    BUCKET_RADIO_BUTTON = lambda _name: (By.XPATH, f"//input[@type='radio' and ancestor::td[following-sibling::td/div/a/text()='{_name}']]")
    BUCKET_DATA_ROW = lambda _name: (By.XPATH, f"//input[@type='radio' and ancestor::td[following-sibling::td/div/a/text()='{_name}']]")

    BUCKET_UPLOAD_FILE_BUTTON = (By.LINK_TEXT, "Upload")
    ADD_FILES_BUTTON = (By.XPATH, "//button[./div/text()='Add files']")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")
    UPLOAD_FILE_SUBMIT_BUTTON = (By.XPATH, "//button[@type='button' and ./span/text()='Upload']")
    ACTION_BUTTON = (By.XPATH, "//button[@type='button' and ./div/text()='Actions ']")
    DELETE_BUCKET_OPTION = (By.XPATH, "//li[span[@class='ant-dropdown-menu-title-content' and text()='Delete']]")
    DELETE_CONFIRM_BUTTON = (By.XPATH, "//button[@type='button' and ./span/text()='Delete']")
    DELETE_CANCEL_BUTTON = (By.XPATH, "//button[@type='button' and ./span/text()='Cancel']")

    
    # At left menu bar in homepage
    BUCKET_NAV = (By.XPATH, "//li[span/a[@href='/s3/buckets' and ./span/text()='Buckets']]")
    SERVICE_ACCOUNT_NAV = (By.XPATH, "//li[span/a[@href='/s3/sa' and ./span/text()='Service Account']]")

    # At Service Account home page
    CREATE_SA_BUTTON = (By.XPATH, "//a[@href='/s3/sa/create' and ./span/text()='Create service account']")
    
    # At Service Account create page
    CREATE_SA_TITLE = (By.XPATH, "//h1[text()='Create service account']")
    #TODO: Check if default name is filled in textbox (do it in test)
    SA_NAME_TEXTBOX = (By.XPATH, "//input[@type='text' and @id='serviceAccountName']")

    DELETE_BUCKET_SUCCESSFUL_ALERT = (By.XPATH, "//div[@role='alert' "
                                                "and ./div/text()='Successful!' "
                                                "and ./div/text()='Delete bucket is successful!']")

    DELETE_NON_EMPTY_BUCKET_ALERT = (By.XPATH, "//div[@class='ant-modal-body' "
                                               "and */div/span/text()='Failed to delete bucket' "
                                               "and */div/button/span/text()='Ok']")
