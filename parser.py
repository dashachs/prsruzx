from selenium import webdriver
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# start chrome browser
browser = webdriver.Chrome('C:\\IT\\Python\\Projects\\uzexparser\\chromedriver.exe', options=options)
browser.get('http://etender.uzex.uz/lots/1/0')

# print(browser.page_source)

buttons = browser.find_elements_by_css_selector('button.btn-outline-primary')
for i in buttons:
    print(i, type(i))

for i in range(100):
    buttons[1].click()

res = browser.find_elements_by_class_name('lot-item')
for i in range(len(res)):
    print(i)
    # print(res[i].text)
    # print('\n\n')
browser.quit()
