from selenium import webdriver
import func

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

# pars lots
for lotID in lotIDs:
    link = "http://etender.uzex.uz/lot/" + lotID
    print(lotID, ": ", link)
    func.parseLot(browser, link)

# close browser
browser.quit()
