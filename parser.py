from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# start chrome browser
browser = webdriver.Chrome('chromedriver.exe', options=options)
browser.get('http://etender.uzex.uz/lots/1/0')

# print(browser.page_source)

buttons = browser.find_elements_by_css_selector('button.btn-outline-primary')
for i in buttons:
    print(i, type(i))

try:
    while True:
        buttons[1].click()
except StaleElementReferenceException:
    print('кнопки больше нет')

res = browser.find_elements_by_class_name('lot-item')
for i in range(len(res)):
    print(i)
    # print(res[i].text)
    # print('\n\n')
browser.quit()
