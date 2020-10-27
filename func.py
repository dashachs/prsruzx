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
            "/html/body/app-root/main/app-lot-item/div/div[1]/section/div[2]/div[2]/div/p[2]/strong |" # дата начала
            "/html/body/app-root/main/app-lot-item/div/div[1]/section/div[2]/div[3]/div/p[2]/strong |" # дата окончания
            "/html/body/app-root/main/app-lot-item/div/div[1]/section/div[2]/div[4]/div/p[2]/strong") # Итого стартовая стоимость

    for i in res:
        print(i.text)
    res.clear()