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


def parseLot(browser, link, currentLot):
    browser.get(link)

    # +lotID, +category, +linkToLot, +startDate, +endDate, +purchaseName, +customerName, +customerDetails,
    #                  +customerContact, -customerAddress, +deliveryAddress, -deliveryTerm, -paymentTerm, -specialConditions,
    #                  -attachedFile, -description, +startingPrice

    # waiting for page to load
    try:
        textXPATH = "//div[@class='row lot__top-infro-wrapper ']/div/div[@class='card lot__top-info']/p"
        element = WebDriverWait(browser, 10).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, textXPATH), "Дата начала:")
        )
    finally:
        temp_startDate = browser.find_element_by_xpath("//div[@class='card lot__top-info']/p/strong[@class='text-success mt-3 ']").text  # startDate - дата начала
        temp_endDate = browser.find_element_by_xpath("//div[@class='card  lot__top-info']/p/strong[@class='text-danger mt-3 ']").text  # endDate - дата окончания
        temp_startingPrice = browser.find_element_by_xpath("//div[@class='card  lot__top-info ']/p/strong[@class='text-success mt-3 ']").text  # paymentTerm - Итого стартовая стоимость
        temp_category = browser.find_element_by_xpath("//table[@class='table custom-table-dark--2']/tbody/tr/td[3]").text  # category - категория
        temp_customerName = browser.find_element_by_xpath("//div[@class='mb-4']/div[2]/div[@class='col-md-7 ']/p/strong"). text  # customerName - Наименование заказчика
        temp_customerDetails = browser.find_element_by_xpath("//div[@class='mb-4']/div[1]/div[@class='col-md-7 ']/p/strong").text  # customerDetails - реквизиты заказчика
        temp_deliveryAddress = browser.find_element_by_xpath("//div[@class='mb-4']/div[13]/div[@class='col-md-7 ']/p/strong").text  # deliveryAddress - Адрес поставки
        temp_customerContact = browser.find_element_by_xpath("//table[@class='table custom-table-dark--2 ']/tbody/tr/th").text  # customerContact
        temp_paymentTerm = browser.find_element_by_xpath("//div[@class='mb-4']/div[6]/div[@class='col-md-5 text-md-right']/p").text + \
                           browser.find_element_by_xpath("//div[@class='mb-4']/div[6]/div[@class='col-md-7 ']/p/strong").text + ";\n  " + \
                           browser.find_element_by_xpath("//div[@class='mb-4']/div[7]/div[@class='col-md-5 text-md-right']/p").text + \
                           browser.find_element_by_xpath("//div[@class='mb-4']/div[7]/div[@class='col-md-7 ']/p/strong").text + ";\n  " + \
                           browser.find_element_by_xpath("//div[@class='mb-4']/div[8]/div[@class='col-md-5 text-md-right']/p").text + \
                           browser.find_element_by_xpath("//div[@class='mb-4']/div[8]/div[@class='col-md-7 ']/p/strong").text + ";\n  " + \
                           browser.find_element_by_xpath("//div[@class='mb-4']/div[9]/div[@class='col-md-5 text-md-right']/p").text + \
                           browser.find_element_by_xpath("//div[@class='mb-4']/div[9]/div[@class='col-md-7 ']/p/strong").text + ";\n  " + \
                           browser.find_element_by_xpath("//div[@class='mb-4']/div[12]/div[@class='col-md-5 text-md-right']/p").text + \
                           browser.find_element_by_xpath("//div[@class='mb-4']/div[12]/div[@class='col-md-7 ']/p/strong").text

    currentLot.linkToLot = link
    currentLot.startDate = temp_startDate
    currentLot.endDate = temp_endDate
    currentLot.startingPrice = temp_startingPrice
    currentLot.category = temp_category
    currentLot.customerName = temp_customerName
    currentLot.customerDetails = temp_customerDetails
    currentLot.deliveryAddress = temp_deliveryAddress
    currentLot.customerContact = temp_customerContact
    currentLot.paymentTerm = temp_paymentTerm

    print("lotID\n  ", currentLot.lotID,
          "\nlinkToLOt\n  ", currentLot.linkToLot,
          "\ncategory\n  ", currentLot.category,
          "\nstartDate\n  ", currentLot.startDate,
          "\nendDate\n  ", currentLot.endDate,
          "\npurchaseName\n  ", currentLot.purchaseName,
          "\ncustomerName\n  ", currentLot.customerName,
          "\ncustomerDetails\n  ", currentLot.customerDetails,
          "\ncustomerContact\n  ", currentLot.customerContact,
          "\ncustomerAddress\n  ",
          "\ndeliveryAddress\n  ", currentLot.deliveryAddress,
          "\ndeliveryTerm\n  ",
          "\npaymentTerm\n ", currentLot.paymentTerm,
          "\nspecialConditions\n  ",
          "\nattachedFile\n  ",
          "\ndescription\n  ",
          "\nstartingPrice\n  ", currentLot.startingPrice)
