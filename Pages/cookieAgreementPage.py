from Locators.locators import locators


class cookieAgreementPage:

    def __init__(self, driver):
        self.driver = driver

    def clickAgree(self):
        self.driver.find_element_by_xpath(locators.agree_button_xpath).click()
