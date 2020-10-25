from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# start chrome browser
browser = webdriver.Chrome('C:\\IT\\Python\\Projects\\uzexparser\\chromedriver.exe', options=options)
browser.get('http://etender.uzex.uz/lots/1/0')
res = browser.find_elements_by_class_name('lot-item')
for i in range(len(res)):
    print(i)
    print(res[i].text)
    print('\n\n')
browser.quit()
