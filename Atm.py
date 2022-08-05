class Atm:
    def init(self,atmcardnumber,pinnumber,cashwithrawl,balanceenquiry):
        self.atmcardnumber=atmcardnumber
        self.pinnumber=pinnumber
        self.cashwitdrawl=cashwithrawl
        self.balanceenquiry=balanceenquiry

    
    def atmcardnumber(self):
        print("Enter atmcard number:")
    def pinnumber(self):
        print("Enter pin number:")
    def cashwithdrawl(self):
        print("Withdraw cash")
    def balanceenquiry(self,balanceenquiry):
        print("How can we help You?")