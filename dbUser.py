def inputToDB(con, lot):
    cur = con.cursor()
    cur.execute(
        "INSERT INTO etender_uzex_test(lot_number, type, category_id, source_url, started_at, ended_at, status, country_id, region_id, area_id, price, currency_id, purchase_name, customer_name, customer_details, customer_contact, delivery_address, delivery_term, deposit, deposit_payment, advance_payment, payment_method, payment_period, special_conditions, attached_file, description)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (lot.lotID, lot.type, lot.categoryID, lot.linkToLot, lot.startedAt, lot.endedAt, lot.status,
         lot.customerAddressCountryID, lot.customerAddressRegionID, lot.customerAddressAreaID,
         lot.startingPrice, lot.currencyID, lot.purchaseName, lot.customerName, lot.customerDetails,
         lot.customerContact, lot.deliveryAddress, lot.deliveryTerm, lot.deposit, lot.depositPayment,
         lot.advancePayment, lot.paymentMethod, lot.paymentPeriod, lot.specialConditions, lot.attachedFile,
         lot.description))
    print("{} inserted successfully".format(lot.lotID))
    con.commit()


# def deleteExpiredLots(con):
#     cur = con.cursor()
#     cur.execute("SET TIMEZONE=5")
#     cur.execute("DELETE FROM etender_uzex_test WHERE ended_at < now()")
#     con.commit()
#     print("Expired lots were deleted")

def findExpiredLots(con):
    cur = con.cursor()
    # setting timezone for current session to avoid mistakes
    cur.execute("SET TIMEZONE=5")
    cur.execute("UPDATE etender_uzex_test SET status = %s WHERE ended_at < now()", ('expired'))


# def deleteRow(id, con):
#     cur = con.cursor()
#     cur.execute("DELETE FROM etender_uzex_test WHERE lot_number={}".format(id))
#     print("Deletion successful")
#     con.commit()
#     con.close()
#
#
# def amountOfRow(con):
#     cur = con.cursor()
#     cur.execute("SELECT count(lot_number) FROM etender_uzex_test")
#     res = cur.fetchall()
#     con.commit()
#     con.close()
#     return res[0][0]


def getForEverything(con, listOfLots):  # название временное
    for lot in listOfLots:
        getForThisLot(con, lot)
        printLotIDs(lot)


def getForThisLot(con, currentLot):
    currentLot.categoryID = getCategoryId(con, currentLot.category)
    currentLot.customerAddressRegionID = getRegionId(con, currentLot.customerAddressRegion)
    currentLot.customerAddressAreaID = getAreaId(con, currentLot.customerAddressArea)
    currentLot.currencyID = getCurrencyId(con, currentLot.currency)


def printLotIDs(currentLot):  # temp
    print("Lot №  ", currentLot.lotID,
          "\n  categoryID:  ", currentLot.categoryID,
          "\n  customerAddressRegionID:  ", currentLot.customerAddressRegionID,
          "\n  customerAddressAreaID:  ", currentLot.customerAddressAreaID,
          "\n  currencyID:  ", currentLot.currencyID,
          "\n======================================\n")


def getCategoryId(con, required):
    cur = con.cursor()
    cur.execute("SELECT category_id, name FROM bidding_categories_translations")
    rows = cur.fetchall()
    for row in rows:
        if row[1].lower().replace(' ', '') == required.lower().replace(' ', ''):
            print("getCategoryId done successfully")
            return row[0]
    print("getCategoryId didn't find name:", required)
    rows.clear()
    return -1


def getCurrencyId(con, requierd):
    cur = con.cursor()
    cur.execute("SELECT id, slug FROM finance_currencies")
    rows = cur.fetchall()
    for row in rows:
        if row[1].upper().replace(' ', '') == requierd.upper().replace(' ', ''):
            print("getCurrencyId done successfully", requierd, "ID =", row[0])
            return row[0]
    print("getCurrencyId didn't find name:", requierd)
    rows.clear()
    return -1


def getRegionId(con, requierd):
    cur = con.cursor()
    cur.execute("SELECT region_id, name FROM geo_regions_translations")
    rows = cur.fetchall()
    for row in rows:
        if row[1].lower().replace(' ', '') == requierd.replace('город', '').lower().replace(' ', ''):
            print("getRegionId done successfully")
            return row[0]
    print("getRegionId didn't find name:", requierd)
    rows.clear()
    return -1


def getAreaId(con, required):
    cur = con.cursor()
    cur.execute("SELECT id, area_id, name FROM geo_areas_translations")
    rows = cur.fetchall()
    scrap = required
    scrap = scrap.lower()
    scrap = scrap.replace(' ', '')
    scrap = scrap.replace('район', '')
    scrap = scrap.replace('р-он', '')
    scrap = scrap.replace('г.', '')
    for row in rows:
        if scrap in row[2].lower().replace(' ', ''):
            print("getAreaId done successfully")
            return row[1]
    print("getAreaId didn't find name:", required)
    rows.clear()
    return -1
    # cur.execute("INSERT INTO geo_areas_translations(id, area_id, name, locale) VALUES (%s, %s, %s, %s)",
    #             (rows[-1][0] + 1,
    #              rows[-1][1] + 1,
    #              required,
    #              'rus'))
    # cur.execute("INSERT INTO geo_areas_translations(id, area_id, name, locale) VALUES (%s, %s, %s, %s)",
    #             (rows[-1][0] + 2,
    #              rows[-1][1] + 1,
    #              required,
    #              'uzb'))
    # con.commit()


def inTable(con, lotNumber):
    cur = con.cursor()
    cur.execute("SELECT lot_number FROM etender_uzex_test")
    rows = cur.fetchall()
    for row in rows:
        if int(lotNumber) == row[0]:
            return True
    return False
