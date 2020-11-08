from selenium import webdriver
from psycopg2 import OperationalError
import psycopg2
import time
import func
import dbUser


def executeParser():
    print("parser started successfully")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # create lot's object
    listOfLots = []

    # start chrome browser
    browser = webdriver.Chrome('chromedriver.exe', options=options)
    print("browser opened successfully")

    # open tenders page
    link = 'http://etender.uzex.uz/lots/2/0'
    func.openAndLoadPage(browser, link)
    print("  tenders page loaded to the end successfully")

    # parse tenders
    func.parseFromPage(browser, listOfLots)

    # reopening browser bc this bitch won't load
    browser.quit()
    print("==========================\n"
          "\nbrowser closed successfully")
    browser = webdriver.Chrome('chromedriver.exe', options=options)
    print("browser reopened successfully\n")

    # open contests page
    link = 'http://etender.uzex.uz/lots/1/0'
    func.openAndLoadPage(browser, link)
    print("  contests page loaded to the end successfully")

    # parse contests
    func.parseFromPage(browser, listOfLots)

    print("Parsed successfully")
    # close browser
    browser.quit()
    print("browser closed successfully")

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

    # adding to DB
    for lot in listOfLots:
        if not dbUser.inTable(con, lot.lotID):
            dbUser.inputToDB(con, lot)
        else:
            print(lot.lotID, "already in DB")

    # find expired lots
    dbUser.findExpiredLots(con)

    # close DB
    con.close()
    print("Database closed successfully")

    # clear list of lots
    listOfLots.clear()

    # setting repeating time
    timerTime = 60
    print("\n~~~~~~~~~~~~~~~~~~~~~\n"
          "Parser will start again in", timerTime, "seconds"
          "\n~~~~~~~~~~~~~~~~~~~~~\n")
    time.sleep(timerTime)


while True:
    executeParser()
