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

# search lot's ID
lotIDs = []
res = browser.find_elements_by_xpath("//div[@class ='lot-item__num-cat']/div/span")
for i in res:
    # print(i.text)
    lotIDs.append(i.text)

# parse lots
for lotID in lotIDs:
    link = "http://etender.uzex.uz/lot/" + lotID
    print(lotID, ": ", link)
    func.parseLot(browser, link)

#create lot's object
listOfLots = []
for i in range(len(lotIDs)):
    listOfLots.append(i)
    listOfLots[i] = object_of_lot.lot(lotIDs[i], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    # нужно добавть заполнить все поля в объекте, или указать значения по умолчанию
    # это просто пример и он запоминает пока лишь ID лота

# close browser
browser.quit()
