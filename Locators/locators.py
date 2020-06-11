class locators():
    # cookieAgreementPage
    agree_button_xpath = "//button[@name='agree']"

    # homePage
    tickerSymbol_textbox_xpath = "//input[@id='yfin-usr-qry']"
    searches_button_xpath = "//button[@id='search-button']"

    # statsPage
    forwardPE_text_cssSelector = ".fi-row:nth-child(4) > .Fw\(500\)"
    marketCap_text_cssSelector = ".fi-row:nth-child(1) > .Fw\(500\)"
    enterpriseValue_text_cssSelector = ".fi-row:nth-child(2) > .Fw\(500\)"
    totalCash_text_cssSelector = ".Pos\(r\):nth-child(5) .Bxz\(bb\):nth-child(1) > .Fw\(500\)"
    totalDebt_text_cssSelector = ".Pos\(r\):nth-child(5) .Bxz\(bb\):nth-child(3) > .Fw\(500\)"
    dividend_text_cssSelector = ".Pstart\(20px\) > .Pos\(r\):nth-child(3) .Bxz\(bb\):nth-child(2) > .Fw\(500\)"
    dividend5Year_text_cssSelector = ".Pos\(r\):nth-child(3) > div > div > .W\(100\%\) .Bxz\(bb\):nth-child(5) > .Fw\(500\)"
    payoutRatio_text_cssSelector = ".Pos\(r\):nth-child(3) > div > div > .W\(100\%\) .Bxz\(bb\):nth-child(6) > .Fw\(500\)"
    quarterlyRevenueGrowth_text_cssSelector = ".Pos\(r\):nth-child(4) .Bxz\(bb\):nth-child(3) > .Fw\(500\)"
    quarterlyEarningsGrowth_text_cssSelector = ".Pos\(r\):nth-child(4) .Bxz\(bb\):nth-child(8) > .Fw\(500\)"

    # stockPage
    stats_link_xpath = "//span[contains(text(),'Statistics')]"
