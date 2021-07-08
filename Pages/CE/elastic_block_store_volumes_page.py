from Configs.local import CE_VOLUME_URL
from Pages.CE.volume_page import CEVolumePage
from Locators.CE import CEVolumePageLocators
from Pages.base_page import BasePage
from Configs import CE_BASE_URL


class CEVolumePage(BasePage):
    def __init__(self, driver):
        self.locator = CEVolumePageLocators
        super(CEVolumePage, self).__init__(driver, CE_VOLUME_URL)
