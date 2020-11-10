class lot:
    def __init__(self, lotID=None, type=None, category=None, categoryID=None, linkToLot=None, startDate=None,
                 endDate=None, status='relevant', purchaseName=None, customerName=None, customerDetails=None,
                 customerContact=None, customerAddress=None, customerAddressCountryID=220, customerAddressRegion=None,
                 customerAddressRegionID=None, customerAddressArea=None, customerAddressAreaID=None, deliveryAddress=None,
                 deliveryTerm=None, deposit=None, depositPayment=None, advancePayment=None, paymentMethod=None,
                 paymentPeriod=None, specialConditions=None, attachedFile=None, description=None, startingPrice=None,
                 currency=None, currencyID=None):
        self.lotID = lotID  # -ID лота
        self.type = type  # -конкурс/тендер
        self.category = category  # - Категория +
        self.categoryID = categoryID  # - ID категории +
        self.linkToLot = linkToLot  # - ссылка на лот
        self.startedAt = startDate  # - дата объявления(когда выставили этот лот) +
        self.endedAt = endDate  # - дата окончания +
        self.status = status  # status — (relevant/expired)
        self.purchaseName = purchaseName  # -Наименование закупки
        self.customerName = customerName  # -Наименование заказчика +
        self.customerDetails = customerDetails  # -Реквизиты заказчика
        self.customerContact = customerContact  # -Контакты заказчика (ответственного лица, контактное лицо)
        self.customerAddress = customerAddress  # -Адрес заказчика
        self.customerAddressCountryID = customerAddressCountryID  # -ID адрес заказчика (country ID)
        self.customerAddressRegion = customerAddressRegion  # -Адрес заказчика (region)
        self.customerAddressRegionID = customerAddressRegionID  # -ID адрес заказчика (region ID)
        self.customerAddressArea = customerAddressArea   # -Адрес заказчика (area)
        self.customerAddressAreaID = customerAddressAreaID  # -ID адрес заказчика (area ID)
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
        self.currencyID = currencyID  # -ID валюты
