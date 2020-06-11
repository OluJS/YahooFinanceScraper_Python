from Locators.locators import locators


class stockPage:

    def __init__(self, driver):
        self.driver = driver

    def clickStats(self):
        self.driver.find_element_by_xpath(locators.stats_link_xpath).click()
