from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# start chrome browser
browser = webdriver.Chrome('C:\\IT\\Python\\Projects\\uzexparser\\chromedriver.exe', options=options)
browser.get('http://etender.uzex.uz/lots/1/0')
res = browser.find_element_by_class_name('lot-item')
print(browser.page_source)
browser.quit()
