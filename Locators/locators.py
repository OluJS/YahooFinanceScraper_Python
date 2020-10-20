class locators:
    # cookieAgreementPage
    agree_button_xpath = "//button[@name='agree']"

    # homePage
    tickerSymbol_textbox_xpath = "//input[@id='yfin-usr-qry']"
    searches_button_xpath = "//button[@id='header-desktop-search-button']"

    # statsPage
    stockName_text_cssSelector = ".Fz\(18px\)"
    forwardPE_text_cssSelector = ".Bxz\(bb\):nth-child(4) > .Ta\(c\):nth-child(2)"
    marketCap_text_cssSelector = ".BdY > .Ta\(c\):nth-child(2)"
    enterpriseValue_text_cssSelector = ".Bxz\(bb\):nth-child(2) > .Ta\(c\):nth-child(2)"
    totalCash_text_cssSelector = ".Pos\(r\):nth-child(5) .Bxz\(bb\):nth-child(1) > .Fw\(500\)"
    totalDebt_text_cssSelector = ".Pos\(r\):nth-child(5) .Bxz\(bb\):nth-child(3) > .Fw\(500\)"
    dividend_text_cssSelector = ".Pstart\(20px\) > .Pos\(r\):nth-child(3) .Bxz\(bb\):nth-child(2) > .Fw\(500\)"
    dividend5Year_text_cssSelector = ".Pos\(r\):nth-child(3) > div > div > .W\(100\%\) .Bxz\(bb\):nth-child(5) > .Fw\(500\)"
    payoutRatio_text_cssSelector = ".Pos\(r\):nth-child(3) > div > div > .W\(100\%\) .Bxz\(bb\):nth-child(6) > .Fw\(500\)"
    quarterlyRevenueGrowth_text_cssSelector = ".Pos\(r\):nth-child(4) .Bxz\(bb\):nth-child(3) > .Fw\(500\)"
    quarterlyEarningsGrowth_text_cssSelector = ".Pos\(r\):nth-child(4) .Bxz\(bb\):nth-child(8) > .Fw\(500\)"

    # stockPage
    stats_link_xpath = "//span[contains(text(),'Statistics')]"
