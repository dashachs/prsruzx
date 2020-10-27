from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


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

    # waiting for page to load
    try:
        textXPATH = "//div[@class='row lot__top-infro-wrapper ']/div/div[@class='card lot__top-info']/p"
        element = WebDriverWait(browser, 10).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, textXPATH), "Дата начала:")
        )
    finally:
        res = browser.find_elements_by_xpath(
            "//div[@class='row lot__top-infro-wrapper ']/div/div[@class='card lot__top-info']/p |"
            "//div[@class='row lot__top-infro-wrapper ']/div/div[@class='card  lot__top-info']/p |"
            "//div[@class='row lot__top-infro-wrapper ']/div/div[@class='card  lot__top-info ']/p |"
            "//div[@class ='mb-4']/div/div/p |"
            "//div[@class ='col-md-3 col-lg-2 mb-3']/div[@class ='card lot__top-info']/p |"
            "//div[@class ='col-md-6 col-lg-4 mb-3']/div[@class ='card lot__top-info']/p |"
            "//div[@class ='col-md-6 col-lg-4 mb-3']/div[@class ='card lot__top-info']/p/strong")

    for i in res:
        print(i.text)
    res.clear()