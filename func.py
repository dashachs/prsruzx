from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import object_of_lot


def openAndLoadPage(browser, link):
    browser.get(link)
    print("connection to the site was successful")

    # press button for add new lots
    loadButton = find_loadButton(browser)
    if loadButton != -1:
        press_loadButton(loadButton)


def find_loadButton(browser):
    buttons = browser.find_elements_by_css_selector('button.btn-outline-primary')
    for i in buttons:
        if 'Загрузить ещё' in i.text:
            return i
    return -1


def press_loadButton(button):
    try:
        while True:
            button.click()
    except StaleElementReferenceException:
        pass


def parseFromPage(browser, listOfLots):
    # search lot's ID and purchase names
    lotIDs = []
    lotNames = []
    lotAddresses = []
    listForIDs = browser.find_elements_by_xpath("//div[@class ='lot-item__num-cat']/div/span")
    listForNames = browser.find_elements_by_xpath("//div[@class='lot-item__title']")
    listOfAddresses = browser.find_elements_by_xpath("//div[@class='lot-item__address']")
    for i, j, k in zip(listForIDs, listForNames, listOfAddresses):
        lotIDs.append(i.text)
        lotNames.append(j.text)
        lotAddresses.append(k.text)

    # clear lists
    listForIDs.clear()
    listForNames.clear()
    listOfAddresses.clear()

    # parse lots
    for i in range(len(lotNames)):
        size = len(listOfLots)  # чтобы не было наслойки
        link = "http://etender.uzex.uz/lot/" + lotIDs[i]
        # adding new lot to list of lots (adding ID and purchase name)
        listOfLots.append(object_of_lot.lot())
        listOfLots[size].lotID = lotIDs[i]
        listOfLots[size].purchaseName = lotNames[i]
        listOfLots[size].customerAddress = lotAddresses[i]
        print("==========================")
        print("#", size + 1)  # to count lots
        parseLot(browser, link, listOfLots[size])

    # clear lists
    lotIDs.clear()
    lotNames.clear()
    lotAddresses.clear()


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
        print("TimeoutException in parsing ig (idk)")
        return 0
    finally:
        fillInLot(browser, link, currentLot)


def fillInLot(browser, link, currentLot):
    currentLot.type = browser.find_element_by_xpath(
        "//div[@class='mb-4']/div[3]/div[@class='col-md-7 ']/p/strong").text  # type - конкурс/тендер
    currentLot.category = browser.find_element_by_xpath(
        "//table[@class='table custom-table-dark--2']/tbody/tr/td[3]").text  # category - категория
    currentLot.startedAt = browser.find_element_by_xpath(
        "//div[@class='card lot__top-info']/p/strong[@class='text-success mt-3 ']").text  # startedAt - дата начала
    currentLot.startedAt = reformatDate(currentLot.startedAt)  # замена dd-mm-yyyy hh:mm на yyyy-mm-dd hh:mm
    currentLot.endedAt = browser.find_element_by_xpath(
        "//div[@class='card  lot__top-info']/p/strong[@class='text-danger mt-3 ']").text  # endedAt - дата окончания
    currentLot.endedAt = reformatDate(currentLot.endedAt)  # замена dd-mm-yyyy hh:mm на yyyy-mm-dd hh:mm
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
    if currentLot.specialConditions == "-":
        currentLot.specialConditions = None  # if no special conditions
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
    currentLot.startingPrice = int(
        (tempForPrice.replace(currentLot.currency, '')).replace(' ', ''))  # -Стартовая стоимость
    currentLot.linkToLot = link

    tempForAddress = currentLot.customerAddress.split(",")
    currentLot.customerAddressRegion = tempForAddress[0]
    currentLot.customerAddressArea = tempForAddress[1]
    tempForAddress.clear()

    # printing lot information (temp)
    printLotInfo(currentLot)


def reformatDate(date):
    dateAndTime = date.split(' ')
    dayMonthYear = dateAndTime[0].split('-')
    date = (((((dayMonthYear[2] + '-') + dayMonthYear[1]) + '-') + dayMonthYear[0]) + ' ') + dateAndTime[1]
    dateAndTime.clear()
    dayMonthYear.clear()
    return date


def printLotInfo(currentLot):  # temp
    print("lotID:  ", currentLot.lotID)
    # output is temporarily commented
    # print("lotID\n  ", currentLot.lotID,
    # "\ntype\n  ", currentLot.type,
    # "\nlinkToLot\n  ", currentLot.linkToLot,
    # "\ncategory\n  ", currentLot.category,
    # "\nstartedAt\n  ", currentLot.startedAt,
    # "\nendedAt\n  ", currentLot.endedAt,
    # "\nstatus\n  ", currentLot.status,
    # "\npurchaseName\n  ", currentLot.purchaseName,
    # "\ncustomerName\n  ", currentLot.customerName,
    # "\ncustomerDetails\n  ", currentLot.customerDetails,
    # "\ncustomerContact\n  ", currentLot.customerContact,
    # "\ncustomerAddressRegion\n  ", currentLot.customerAddressRegion,
    # "\ncustomerAddressArea\n  ", currentLot.customerAddressArea,
    # "\ndeliveryAddress\n  ", currentLot.deliveryAddress,
    # "\ndeliveryTerm\n  ", currentLot.deliveryTerm,
    # "\ndeposit\n  ", currentLot.deposit,
    # "\ndepositPayment\n  ", currentLot.depositPayment,
    # "\nadvancePayment\n  ", currentLot.advancePayment,
    # "\npaymentMethod\n  ", currentLot.paymentMethod,
    # "\npaymentPeriod\n  ", currentLot.paymentPeriod,
    # "\nspecialConditions\n  ", currentLot.specialConditions,
    # "\nattachedFile\n  ", currentLot.attachedFile,
    # "\ndescription\n  ", currentLot.description,
    # "\nstartingPrice\n  ", currentLot.startingPrice,
    # "\ncurrency\n  ", currentLot.currency)


# def checkIfPageIsLoaded(browser, link):
#     browser.get(link)
#     # waiting for page to load
#     loadingStatus = 1
#     try:
#         textXPATH = "/main"
#         # setting waiting time
#         wait = WebDriverWait(browser, 10)
#         element = wait.until(
#             expected_conditions.text_to_be_present_in_element((By.XPATH, textXPATH), "№ лота:")
#         )
#     except TimeoutException:  # https://qna.habr.com/q/641216 - храни их господь
#         print("TimeoutException or an empty page")
#         loadingStatus = 0
#     finally:
#         return loadingStatus
