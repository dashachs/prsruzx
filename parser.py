from selenium import webdriver
from psycopg2 import OperationalError
import psycopg2
import func
import object_of_lot
import dbUser


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
    size = len(listOfLots)  # чтобы не было наслойки
    for i in range(len(lotNames)):
        link = "http://etender.uzex.uz/lot/" + lotIDs[i]
        # adding new lot to list of lots (adding ID and purchase name)
        listOfLots.append(object_of_lot.lot())
        listOfLots[size + i].lotID = lotIDs[i]
        listOfLots[size + i].purchaseName = lotNames[i]
        listOfLots[size + i].customerAddress = lotAddresses[i]
        print("\n==========================")
        func.parseLot(browser, link, listOfLots[size + i])
    pass

print("parser started successful")

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# create lot's object
listOfLots = []

# start chrome browser
browser = webdriver.Chrome('chromedriver.exe', options=options)
print("browser opened successfully")
browser.get('http://etender.uzex.uz/lots/2/0')
print("connection to the site was successfully")

# press button for add new lots
loadButton = func.find_loadButton(browser)
if loadButton != -1:
    func.press_loadButton(loadButton)
print("tenders page loaded to the end successfully")

# parse tenders
parseFromPage(browser, listOfLots)

browser.get('http://etender.uzex.uz/lots/1/0')
print("connection to the site was successful")

# press button for add new lots
loadButton = func.find_loadButton(browser)
if loadButton != -1:
    func.press_loadButton(loadButton)
print("contests page loaded to the end successfully")

# parse contests
parseFromPage(browser, listOfLots)

# close browser
browser.quit()
print("Parsed and closed the browser successfully")


# database input

while True:
    try:
        con = psycopg2.connect(
            database="postgres",
            user="anwar",
            password="etender.uz",
            host="database-rds.cbs8omqsohea.eu-west-3.rds.amazonaws.com",
            port="5432"
        )
    except OperationalError:
        print("Failed to connect to the server. connection...")
    else:
        print("Database opened successfully")
        break

dbUser.getForEverything(con, listOfLots)
# dbUser.addEverything(con, listOfLots)

# testing
dbUser.inputToDB(con, listOfLots[0])

# close DB
con.close()
