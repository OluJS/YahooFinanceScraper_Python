from behave import *
from selenium import webdriver
from Pages.cookieAgreementPage import cookieAgreementPage
from Pages.homePage import homePage
from Pages.statsPage import statsPage
from Pages.stockPage import stockPage
import time

PATH = "C:\\webdrivers\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)


@given('I go to Yahoo Finance "{webUrl}"')
def step_impl(context, webUrl):
    driver.get(webUrl)
    driver.maximize_window()
    pass


@when('I search for a stock {stockName}')
def step_impl(context, stockName):
    cookie = cookieAgreementPage(driver)
    cookie.clickAgree()
    home = homePage(driver)
    home.typeTickerSymbol(stockName)
    time.sleep(2)
    home.clickSearch()
    pass


@when('I go to the statistics tab')
def step_impl(context):
    time.sleep(2)
    stock = stockPage(driver)
    stock.clickStats()
    pass


@then('I get the enterprise value')
def step_impl(context):
    stats = statsPage(driver)
    time.sleep(3)
    stats.getValuationMeasures()
    pass


@then('I close the browser')
def step_impl(context):
    driver.quit()
    pass


'''
driver = webdriver.Chrome(executable_path=PATH)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(webUrl)

time.sleep(2)

cookie = cookieAgreementPage(driver)
cookie.clickAgree()

time.sleep(2)

home = homePage(driver)
home.typeTickerSymbol("MSFT")
time.sleep(1)
home.clickSearch()

time.sleep(2)

stock = stockPage(driver)
stock.clickStats()

time.sleep(2)

stats = statsPage(driver)
stats.getValuationMeasures()

driver.close()
driver.quit()
print("\nStats col
'''
