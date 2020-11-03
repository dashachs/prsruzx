from selenium import webdriver
import psycopg2
import func
import object_of_lot
import dbUser

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# start chrome browser
browser = webdriver.Chrome('chromedriver.exe', options=options)
browser.get('http://etender.uzex.uz/lots/1/0')

# press button for add new lots
loadButton = func.find_loadButton(browser)
func.press_loadButton(loadButton)

# search lot's ID and purchase names
lotIDs = []
lotNames = []
lotAdresses = []
listForIDs = browser.find_elements_by_xpath("//div[@class ='lot-item__num-cat']/div/span")
listForNames = browser.find_elements_by_xpath("//div[@class='lot-item__title']")
listOfAdresses = browser.find_elements_by_xpath("//div[@class='lot-item__address']")
for i, j, k in zip(listForIDs, listForNames, listOfAdresses):
    lotIDs.append(i.text)
    lotNames.append(j.text)
    lotAdresses.append(k.text)

# clear lists
listForIDs.clear()
listForNames.clear()
listOfAdresses.clear()

# create lot's object
listOfLots = []

# parse lots
for i in range(len(lotNames)):
    link = "http://etender.uzex.uz/lot/" + lotIDs[i]
    # adding new lot to list of lots (adding ID and purchase name)
    listOfLots.append(object_of_lot.lot())
    listOfLots[i].lotID = lotIDs[i]
    listOfLots[i].type = "конкурс"
    listOfLots[i].purchaseName = lotNames[i]
    listOfLots[i].customerAddress = lotAdresses[i]
    print("\n==========================")
    func.parseLot(browser, link, listOfLots[i])

# close browser
browser.quit()

# database input
con = psycopg2.connect(
        database="postgres",
        user="anwar",
        password="etender.uz",
        host="database-rds.cbs8omqsohea.eu-west-3.rds.amazonaws.com",
        port="5432"
    )
print("Database opened successfully")
dbUser.getForEverything(con, listOfLots)

#close DB
con.close()
