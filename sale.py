class Sale():
    def __init__(self, saleid, customerid, itemid, itemquantity, pricetotal)
        self.saleid=saleid
        self.customerid=customerid
        self.itemid=itemid
        self.itemquantity=itemquantity
        self.pricetotal=pricetotal

    def getSaleId(self):
        return self.saleid

    def getCustomerId(self):
        return self.customerid

    def getItemId(self):
        return self.itemid

    def getItemQuantity(self):
        return self.itemquantity

    def getPriceTotal(self):
        return self.pricetotal

    def setItemId(self, itemid):
        self.itemid=itemid

    def __str__(self):
        return self.itemid + ' ' + self.itemquantity