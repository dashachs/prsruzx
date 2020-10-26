from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

def find_loadButton(browser):
    buttons = browser.find_elements_by_css_selector('button.btn-outline-primary')
    for i in buttons:
        if 'Загрузить ещё' in i.text:
            return i


def press_loadButton(button):
    try:
        while True:
            button.click()
    except StaleElementReferenceException:
        pass


def parseLot(browser, link):
    browser.get(link)
    print(" parseLot")
    res = browser.find_elements_by_xpath("//div[@class ='mb-4']/div/div/p")
    for i in res:
        print(i.text)
