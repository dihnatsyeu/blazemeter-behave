from selenium import webdriver

from web_source.web import Web


def get_web(browser):
    if browser == "chrome":
        return Web(webdriver.Chrome("C:/drivers/chromedriver.exe"))

