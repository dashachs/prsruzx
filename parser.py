from selenium import webdriver
import func
import object_of_lot

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
listForIDs = browser.find_elements_by_xpath("//div[@class ='lot-item__num-cat']/div/span")
listForNames = browser.find_elements_by_xpath("//div[@class='lot-item__title']")
for i, j in zip(listForIDs, listForNames):
    lotIDs.append(i.text)
    lotNames.append(j.text)

# clear lists
listForIDs.clear()
listForNames.clear()

# create lot's object
listOfLots = []

# parse lots
for i in range(len(lotNames)):
    link = "http://etender.uzex.uz/lot/" + lotIDs[i]
    # adding new lot to list of lots (adding ID and purchase name)
    listOfLots.append(object_of_lot.lot(lotIDs[i], 1, 1, 1, 1, lotNames[i], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
    print(listOfLots[i].lotID, ": ", link)
    print(listOfLots[i].purchaseName)
    func.parseLot(browser, link, listOfLots[i])

# close browser
browser.quit()
