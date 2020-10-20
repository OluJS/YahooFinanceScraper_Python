from selenium import webdriver
from Resources.listOfStocks import stocksToSearch
from Pages.cookieAgreementPage import cookieAgreementPage
from Pages.homePage import homePage
from Pages.statsPage import statsPage
from Pages.stockPage import stockPage
import time

PATH = "/Users/olu/PycharmProjects/YahooFinanceScraper/Driver/chromedriver"
webUrl = "https://finance.yahoo.com/"
driver = webdriver.Chrome(executable_path=PATH)


def open_browser():
    driver.maximize_window()
    driver.get(webUrl)
    time.sleep(2)
    cookie = cookieAgreementPage(driver)
    cookie.clickAgree()
    get_stock()


def get_stock():
    for stock in stocksToSearch:
        time.sleep(2)

        home = homePage(driver)
        home.typeTickerSymbol(stock)
        time.sleep(1)
        home.clickSearch()

        time.sleep(2)

        stock = stockPage(driver)
        stock.clickStats()

        time.sleep(2)

        stats = statsPage(driver)
        stats.getValuationMeasures()

    print("\nStats have been collected")
    close_browser()


def close_browser():
    driver.quit()


open_browser()
