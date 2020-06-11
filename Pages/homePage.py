from Locators.locators import locators


class homePage:

    def __init__(self, driver):
        self.driver = driver

    def typeTickerSymbol(self, tickerSymbol):
        self.driver.find_element_by_xpath(locators.tickerSymbol_textbox_xpath).send_keys(tickerSymbol)

    def clickSearch(self):
        self.driver.find_element_by_xpath(locators.searches_button_xpath).click()
