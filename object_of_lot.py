class lot:
    def __init__(self, lotID='-', category='-', linkToLot='-', startDate='-', endDate='-', status='relevant',
                 purchaseName='-', customerName='-', customerDetails='-', customerContact='-', customerAddress='-',
                 customerAddressRegion='-', customerAddressArea = '-', deliveryAddress='-', deliveryTerm='-',
                 deposit='-', depositPayment='-', advancePayment='-', paymentMethod='-', paymentPeriod='-',
                 specialConditions='-', attachedFile='-', description='-', startingPrice='-', currency='-'):
        self.lotID = lotID  # -ID лота
        self.category = category  # - Категория +
        self.linkToLot = linkToLot  # - ссылка на лот
        self.startedAt = startDate  # - дата объявления(когда выставили этот лот) +
        self.endedAt = endDate  # - дата окончания +
        self.status = status  # status — (relevant/expired)
        self.purchaseName = purchaseName  # -Наименование закупки
        self.customerName = customerName  # -Наименование заказчика +
        self.customerDetails = customerDetails  # -Реквизиты заказчика
        self.customerContact = customerContact  # -Контакты заказчика (ответственного лица, контактное лицо)
        self.customerAddress = customerAddress  # -Адрес заказчика
        self.customerAddressRegion = customerAddressRegion  # -Адрес заказчика (region)
        self.customerAddressArea = customerAddressArea   # -Адрес заказчика (area)
        self.deliveryAddress = deliveryAddress  # -Адрес поставки +
        self.deliveryTerm = deliveryTerm  # -Условия поставки
        self.deposit = deposit  # -задаток
        self.depositPayment = depositPayment  # - Размер задатка
        self.advancePayment = advancePayment  # -Размер авансового платежа
        self.paymentMethod = paymentMethod  # -Порядок оплаты
        self.paymentPeriod = paymentPeriod  # -Срок расчета (полной оплаты)
        self.specialConditions = specialConditions  # -Особые условия (условия участия)
        self.attachedFile = attachedFile  # -Прикреплённый файл(ссылка на скачивание)
        self.description = description  # -Описание закупки(товар/услуга)
        self.startingPrice = startingPrice  # - стартовая цена
        self.currency = currency  # -валюта

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
# -Описание закупки(товар/услуга). Парсер должен понимать в описании только текст, таблица, текст+таблица, таблица+текст
# - стартовая цена
# -Парсинг должен быть регулярным с тайм-аутами
# -По дате окончания определять актуальность лота на сегодняшний день
# -БД: PostgreSQL
# -Язык реализации: Python
