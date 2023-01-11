
class RavKav():
    def __init__(self,holder_id:int,holder_name:str):
        self.holder_id=holder_id
        self.holder_name=holder_name
        self.balance = 0

    def topup(self,amont):
        if amont<=0:
            print( f'ERROR It is not possible to enter a missing amount{amont}')
        else:
            self.balance+=amont

    def get_current_balance(self):
        return f'current balance {self.balance}'