from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


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


def parseLot(browser, link, currentLot):
    browser.get(link)

    # waiting for page to load
    try:
        textXPATH = "//div[@class='row lot__top-infro-wrapper ']/div/div[@class='card lot__top-info']/p"
        # setting waiting time
        wait = WebDriverWait(browser, 10)
        element = wait.until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, textXPATH), "Дата начала:")
        )
    except TimeoutException:  # https://qna.habr.com/q/641216 - храни их господь
        print("TimeoutException ig (idk)")
        return 0
    finally:
        fillInLot(browser, link, currentLot)


def fillInLot(browser, link, currentLot):
    currentLot.category = browser.find_element_by_xpath(
        # "//div[@class='mb-4']/div[3]/div[@class='col-md-7 ']/p/strong").text  # category - категория
        "//table[@class='table custom-table-dark--2']/tbody/tr/td[3]").text  # category - категория
    currentLot.startDate = browser.find_element_by_xpath(
        "//div[@class='card lot__top-info']/p/strong[@class='text-success mt-3 ']").text  # startDate - дата начала
    currentLot.endDate = browser.find_element_by_xpath(
        "//div[@class='card  lot__top-info']/p/strong[@class='text-danger mt-3 ']").text  # endDate - дата окончания
    currentLot.customerName = browser.find_element_by_xpath(
        "//div[@class='mb-4']/div[2]/div[@class='col-md-7 ']/p/strong").text  # customerName - Наименование заказчика
    currentLot.customerDetails = "ИНН: " + browser.find_element_by_xpath(
        "//div[@class='mb-4']/div[1]/div[@class='col-md-7 ']/p/strong").text  # customerDetails - реквизиты заказчика
    currentLot.customerContact = browser.find_element_by_xpath(
        "//table[@class='table custom-table-dark--2 ']/tbody/tr/th").text + ", " + \
                                 browser.find_element_by_xpath(
                                     "//table[@class='table custom-table-dark--2 ']/tbody/tr/td").text  # customerContact - Контакты заказчика
    currentLot.deliveryAddress = browser.find_element_by_xpath(
        "//div[@class='mb-4']/div[13]/div[@class='col-md-7 ']/p/strong").text  # deliveryAddress - Адрес поставки
    currentLot.deliveryTerm = browser.find_element_by_xpath(
        "//table[@class='table custom-table-dark--2']/tbody/tr/td[7]").text  # deliveryTerm
    currentLot.deposit = browser.find_element_by_xpath(
        "//div[@class='mb-4']/div[6]/div[@class='col-md-7 ']/p/strong").text  # -задаток
    currentLot.depositPayment = browser.find_element_by_xpath(
        "//div[@class='mb-4']/div[7]/div[@class='col-md-7 ']/p/strong").text  # - Размер задатка
    currentLot.advancePayment = browser.find_element_by_xpath(
        "//div[@class='mb-4']/div[8]/div[@class='col-md-7 ']/p/strong").text  # -Размер авансового платежа
    currentLot.paymentMethod = browser.find_element_by_xpath(
        "//div[@class='mb-4']/div[9]/div[@class='col-md-7 ']/p/strong").text  # -Порядок оплаты
    currentLot.paymentPeriod = browser.find_element_by_xpath(
        "//div[@class='mb-4']/div[12]/div[@class='col-md-7 ']/p/strong").text  # -Срок расчета (полной оплаты)
    currentLot.specialConditions = browser.find_element_by_xpath(
        "//*[@id='lot-details-tab-content-1']/div/div[@class='mb-4']/p").text  # specialConditions
    currentLot.description = browser.find_element_by_xpath(
        "//div[@class='lot__products__item']/h5[@class='text-primary mb-3']").text.replace('1 - ', '')  # description
    tempForPrice = browser.find_element_by_xpath(
        "//div[@class='card  lot__top-info ']/p/strong[@class='text-success mt-3 ']").text
    for i in range(len(tempForPrice)):
        num = len(tempForPrice) - i - 1
        if tempForPrice[num] == ' ':
            break
        currentLot.currency = tempForPrice[num] + currentLot.currency
    currentLot.currency = currentLot.currency.replace('-', '')  # -валюта
    currentLot.startingPrice = int((tempForPrice.replace(' ', '')).replace(currentLot.currency, ''))  # -Стартовая стоимость

    currentLot.linkToLot = link

    # printing lot information (temp)
    printLotInfo(currentLot)

def printLotInfo(currentLot):  # temp
    print("lotID\n  ", currentLot.lotID,
          "\nlinkToLOt\n  ", currentLot.linkToLot,
          "\ncategory\n  ", currentLot.category,
          "\nstartDate\n  ", currentLot.startDate,
          "\nendDate\n  ", currentLot.endDate,
          "\nstatus\n  ", currentLot.status,
          "\npurchaseName\n  ", currentLot.purchaseName,
          "\ncustomerName\n  ", currentLot.customerName,
          "\ncustomerDetails\n  ", currentLot.customerDetails,
          "\ncustomerContact\n  ", currentLot.customerContact,
          "\ncustomerAddress\n  ", currentLot.customerAddress,
          "\ndeliveryAddress\n  ", currentLot.deliveryAddress,
          "\ndeliveryTerm\n  ", currentLot.deliveryTerm,
          "\ndeposit\n  ", currentLot.deposit,
          "\ndepositPayment\n  ", currentLot.depositPayment,
          "\nadvancePayment\n  ", currentLot.advancePayment,
          "\npaymentMethod\n  ", currentLot.paymentMethod,
          "\npaymentPeriod\n  ", currentLot.paymentPeriod,
          "\nspecialConditions\n  ", currentLot.specialConditions,
          "\nattachedFile\n  ", currentLot.attachedFile,
          "\ndescription\n  ", currentLot.description,
          "\nstartingPrice\n  ", currentLot.startingPrice,
          "\ncurrency\n  ", currentLot.currency)
