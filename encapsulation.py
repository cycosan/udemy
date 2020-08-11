class computer:
    def __init__(self):
        self.__maxprice=1000

    def sell(self):
        print("Selling price {}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice=price


c=computer()
c.sell()

c.__maxprice=1100
c.sell()
c.setmaxprice(1100)
c.sell()