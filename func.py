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
    res = browser.find_elements_by_xpath("//div[@class='row lot__top-infro-wrapper ']/div/div[@class='card lot__top-info']/p |"
                                         "//div[@class ='mb-4']/div/div/p |"
                                         "//div[@class ='col-md-3 col-lg-2 mb-3']/div[@class ='card lot__top-info']/p |"
                                         "//div[@class ='col-md-3 col-lg-2 mb-3']/div[@class ='card lot__top-info']/p/strong |"
                                         "//div[@class ='col-md-6 col-lg-4 mb-3']/div[@class ='card lot__top-info']/p |"
                                         "//div[@class ='col-md-6 col-lg-4 mb-3']/div[@class ='card lot__top-info']/p/strong")
    for i in res:
        print(i.text)
