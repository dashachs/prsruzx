class lot:
    def __init__(self, lotID, category, linkToLot, startDate, endDate, purchaseName, customerName, customerDetails,
                 customerContact, customerAddress, deliveryAddress, deliveryTerm, paymentTerm, specialConditions,
                 attachedFile, description, startingPrice):
        self.lotID = lotID
        self.category = category
        self.linkToLot = linkToLot
        self.startDate = startDate
        self.endDate = endDate
        self.purchaseName = purchaseName
        self.customerName = customerName
        self.customerDetails = customerDetails
        self.customerContact = customerContact
        self.customerAddress = customerAddress
        self.deliveryAddress = deliveryAddress
        self.deliveryTerm = deliveryTerm
        self.paymentTerm = paymentTerm
        self.specialConditions = specialConditions
        self.attachedFile = attachedFile
        self.description = description
        self.startingPrice = startingPrice

# Парсер ТЗ:
# -ID лота
# - Категория
# - ссылка на лот
# - дата объявления(когда выставили этот лот)
# - дата окончания
# -Наименование закупки
# -Наименование заказчика
# -Реквизиты заказчика
# -Контакты заказчика (ответственного лица, контактное лицо)
# -Адрес заказчика
# -Адрес поставки
# -Условия поставки
# -Условия оплаты
# -Особые условия (условия участия)
# -Прикреплённый файл(ссылка на скачивание)
# -Описание закупки(товар/услуга). Парсер должен понимать в описании только текст, таблица, текст+таблица, таблица+текст.
# - стартовая цена
# -Парсинг должен быть регулярным с тайм-аутами
# -По дате окончания определять актуальность лота на сегодняшний день
# -БД: PostgreSQL
# -Язык реализации: Python
