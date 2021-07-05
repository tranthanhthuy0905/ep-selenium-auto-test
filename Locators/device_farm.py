from selenium.webdriver.common.by import By

class DEVICE_FARM_ProjectLocators(object):
    CREATE_PROJECT_HOME_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[3]/span')
    PROJECT_CREATE_TITLE = (By.XPATH, "/html/body/div[*]/div/div[2]/div/div[2]/div[1]/div")
    PROJECT_NAME_TEXTBOX = (By.XPATH, "/html/body/div[*]/div/div[2]/div/div[2]/div[2]/div/input")
    PROJECT_CREATE_BUTTON = (By.XPATH, "/html/body/div[*]/div/div[2]/div/div[2]/div[3]/button[2]/span")
    PROJECT_NOTIC_CREATE = (By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[1]")

    PROJECT_SELECT_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/label/span/input')
    PROJECT_ACTION_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[2]/div')
    PROJECT_DELETE_BUTTON = (By.XPATH, "/html/body/div[*]/div/div/ul/li/span")
    PROJECT_CONFIRM_DELETE_BUTTON = (By.XPATH, "/html/body/div[*]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span")
    PROJECT_NAME_TEXT = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]')
