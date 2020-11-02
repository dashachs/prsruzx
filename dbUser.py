# def inputToDB(con):
#     cur = con.cursor()
#     cur.execute(
#         "INSERT INTO etender_uzex_test (lot_number, description, name, TIN, start_date, end_date, telephone, email, file_link)"
#         "VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(a, b, c, d, e, f, g, h, i))
#     print("Date inserted successfully")
#     con.commit()
#     con.close()
#
#
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

def getCategoryId(con, requierd):
    cur = con.cursor()
    cur.execute("SELECT category_id, name FROM bidding_categories_translations")
    rows = cur.fetchall()
    for row in rows:
        if row[1].lower().replace(' ', '') == requierd.lower().replace(' ', ''):
            print("getCategoryId done successfully")
            return row[0]
    print("getCategoryId didn't find name")
    return -1

def getCurrencyId(con, requierd):
    cur = con.cursor()
    cur.execute("SELECT id, slug FROM finance_currencies")
    rows = cur.fetchall()
    for row in rows:
        if row[1].upper().replace(' ', '') == requierd.upper().replace(' ', ''):
            print("getCurrencyId done successfully", requierd, "ID =", row[0])
            return row[0]
    print("getCurrencyId didn't find name")
    return -1

def getRegionId(con, requierd):
    cur = con.cursor()
    cur.execute("SELECT region_id, name FROM geo_regions_translations")
    rows = cur.fetchall()
    for row in rows:
        if row[1].lower().replace(' ', '') == requierd.lower().replace(' ', ''):
            print("getRegionId done successfully")
            return row[0]
    print("getRegionId didn't find name")
    return -1

def getAreaId(con, requierd):
    cur = con.cursor()
    cur.execute("SELECT area_id, name FROM geo_areas_translations")
    rows = cur.fetchall()
    for row in rows:
        if row[1].lower().replace(' ', '') == requierd.lower().replace(' ', ''):
            print("getAreaId done successfully")
            return row[0]
    print("getAreaId didn't find name")
    return -1
