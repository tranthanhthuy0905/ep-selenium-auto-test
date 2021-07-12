from selenium.webdriver.common.by import By

class DEVICE_FARM_ProjectLocators(object):
    # CREATE PROJECT
    CREATE_PROJECT_HOME_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[3]/span')
    PROJECT_CREATE_TITLE = (By.XPATH, "/html/body/div[*]/div/div[2]/div/div[2]/div[1]/div")
    PROJECT_NAME_TEXTBOX = (By.XPATH, "/html/body/div[*]/div/div[2]/div/div[2]/div[2]/div/input")
    PROJECT_CREATE_BUTTON = (By.XPATH, "/html/body/div[*]/div/div[2]/div/div[2]/div[3]/button[2]/span")
    PROJECT_NOTIC_CREATE = (By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[1]")

    # DELETE PROJECT
    PROJECT_SELECT_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/label/span/input')
    PROJECT_ACTION_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[2]/div')
    PROJECT_DELETE_BUTTON = (By.XPATH, "/html/body/div[*]/div/div/ul/li/span")
    PROJECT_CONFIRM_DELETE_BUTTON = (By.XPATH, "/html/body/div[*]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span")
    PROJECT_NAME_TEXT = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]')

    # CREATE SESSION
    PROJECT_SELECTOR_LINK = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/a')
    # PROJECT_SELECTOR_LINK = (By.XPATH, "(//a[contains(text(),'selenium-test-')])[0]")
    SESSION_CREATE_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/a/span')
    # TYPE SESSION
    LG_G5_SE_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/label/span/input')
    LIVE_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/table/tbody/tr[6]/td[1]/label/span/input')
    PIXEL_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/table/tbody/tr[7]/td[1]/label/span/input')
    XPERIA_AQUA = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/table/tbody/tr[3]/td[1]/label/span/input')
    GALAXY_TAB_E = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/table/tbody/tr[4]/td[1]/label')
    PIXEL_3 = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/table/tbody/tr[5]/td[1]/label/span/input')
    
    CONFIRM_START_SESSION_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/button[2]/span')
    SESSION_NAME_TEXT = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/input')
    
    # DELETE SESSION
    SESSION_SELECT_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/label/span/input')
    SESSION_ACTION_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[2]/div')
    SESSION_STOP_ACTION_BUTTON = (By.XPATH, '/html/body/div[*]/div/div/ul/li[1]/span')
    SESSION_STOP_CONFIRM_BUTTON = (By.XPATH, '/html/body/div[*]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span')
    SESSION_STOP_NOTIC = (By.XPATH, '/html/body/div[*]/div/div/div/div/div/div[1]')
    SESSION_STATUS_TEXT = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[7]')
    SESSION_DELETE_ACTION_BUTTON = (By.XPATH, '/html/body/div[*]/div/div/ul/li[2]/span')
    SESSION_DELETE_CONFIRM_BUTTON = (By.XPATH, '/html/body/div[*]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span')
    