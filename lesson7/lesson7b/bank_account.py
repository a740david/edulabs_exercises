from datetime import datetime
import pprint
now = datetime.now()
date = now.strftime("%d/%m/%Y")

class Bank_account:


    def __init__(self, account_num:int, bank_name:str,branch:int, account_holder:object,credit_limit:int,is_foreign_currency:bool):
       self.account_num=account_num
       self.bank_name=bank_name
       self.branch=branch
       self.account_holder=account_holder
       self.credit_limit=credit_limit
       self.balance = [{"ILS": 0}, {"USD": 0}]
       self.transaction_db={}
       # transaction
       # '10/12/2022': {
       #       'deposit': {
       #           'USD': [200],
       #           'ILS': [1000]
       #       },
       #       'withdrawal': {
       #           'USD': [200]
       #       },
       #       'transfer_to': {
       #           account_id: [150, ILS]
       #       }
       #       'transfer_in': {
       #           account_id: [200, USD]
       #       },
       #       'conversion': {
       #           'from': [200, ILS],
       #           'to':   [58.25, USD],
       #           'fee':  [4.5, ILS],
       #           'from': [200, ILS],
       #           'to':   [58.25, USD],
       #           'fee':  [4.5, ILS]],
       #         }
       #     }
       # }

       self.is_foreign_currency = is_foreign_currency

    def log_transaction(self, transaction_type: str, currency: str, amount: int):
        if date not in self.transaction_db.keys():
            self.transaction_db[date] = {}
        if transaction_type not in self.transaction_db[date].keys():
            self.transaction_db[date][transaction_type] = []
        self.transaction_db[date][transaction_type].append([currency,amount])

    def show_log(self):
        pprint.pprint(self.transaction_db)
