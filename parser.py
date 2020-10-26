from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
import func

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# start chrome browser
browser = webdriver.Chrome('chromedriver.exe', options=options)
browser.get('http://etender.uzex.uz/lots/1/0')

# print(browser.page_source)

loadButton = func.find_loadButton(browser)
func.press_loadButton(loadButton)
lotIDs = []

res = browser.find_elements_by_xpath("//div[@class ='lot-item__num-cat']/div/span")
for i in res:
    # print(i.text)
    lotIDs.append(i.text)

for lotID in lotIDs:
    link = "http://etender.uzex.uz/lot/" + lotID
    print(lotID, ": ", link)
    func.parseLot(browser, link)

browser.quit()
