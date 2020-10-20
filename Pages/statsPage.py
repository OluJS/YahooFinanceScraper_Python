from Locators.locators import locators


class statsPage:

    def __init__(self, driver):
        self.driver = driver

    def getValuationMeasures(self):
        stockName = self.driver.find_element_by_css_selector(locators.stockName_text_cssSelector).text
        marketCap = self.driver.find_element_by_css_selector(locators.marketCap_text_cssSelector).text
        enterpriseValue = self.driver.find_element_by_css_selector(locators.enterpriseValue_text_cssSelector).text
        fPE = self.driver.find_element_by_css_selector(locators.forwardPE_text_cssSelector).text
        totalCash = self.driver.find_element_by_css_selector(locators.totalCash_text_cssSelector).text
        totalDebt = self.driver.find_element_by_css_selector(locators.totalDebt_text_cssSelector).text
        dividend = self.driver.find_element_by_css_selector(locators.dividend_text_cssSelector).text
        dividend5Year = self.driver.find_element_by_css_selector(locators.dividend5Year_text_cssSelector).text
        payoutRatio = self.driver.find_element_by_css_selector(locators.payoutRatio_text_cssSelector).text
        quarterlyRevenueGrowth = self.driver.find_element_by_css_selector(
            locators.quarterlyRevenueGrowth_text_cssSelector).text
        quarterlyEarningsGrowth = self.driver.find_element_by_css_selector(
            locators.quarterlyEarningsGrowth_text_cssSelector).text

        print("\n=========================================================================")
        print(f"{stockName}: Valuation Measures")
        print("************************************************")
        print(f"Market Cap: {marketCap}")
        print(f"Enterprise Value: {enterpriseValue}")
        print(f"Forward PE Ratio: {fPE}")

        print(f"\n\n{stockName}: Balance Sheet")
        print("************************************************")
        print(f"Total Cash: {totalCash}")
        print(f"Total Debt: {totalDebt}")

        print(f"\n\n{stockName}: Income Statement")
        print("************************************************")
        print(f"Quarterly Revenue Growth: {quarterlyRevenueGrowth}")
        print(f"Quarterly Earnings Growth: {quarterlyEarningsGrowth}")

        print(f"\n\n{stockName}: Dividends & Splits")
        print("************************************************")
        print(f"Dividend: {dividend}")
        print(f"5 Year Dividend Avg.: {dividend5Year}%")
        print(f"Payout Ratio: {payoutRatio}")
        print("=========================================================================")
