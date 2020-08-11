class account:
    balance=0
    def __init__(self):
        self.balance=0
    # def __init__(self,bal):
    #     self.balance=bal
    def  getBalance(self):
         return self.balance
    def setBalance(self,bal):
        if (bal>0):
            self.balance=bal
        elif (bal!=int):
            print("Please insert interger value")

    def transfer(self,amt,transferAcc):
        if (self.balance<amt):
            return False
        elif(amt<0):
            return False
        else:
            self.balance=self.balance-amt
            temp=transferAcc.getBalance()+amt
            transferAcc.setBalance(temp)
            return True

myaccount=account()
youraccount=account()
myaccount.setBalance(1000)
youraccount.setBalance(2000)
myaccount.transfer(100,youraccount)
print(myaccount.getBalance())
print(youraccount.getBalance())



