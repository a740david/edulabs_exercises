from lesson7.lesson7b import bank_account


class Bank:


    def __init__(self, bank_name: str, bank_branch: str):
        self.bank_name: str = bank_name
        self.bank_branch_number: str = bank_branch
        self.bank_account = {int(): bank_account.Bank_account}
        self.available_currencies = ["ILS", "USD"]
        self.usd_rate = 3.43

        # DEPOSIT TO ACCOUNT:

    def deposit(self, account_num: int, amount: int, currency: str):
        currency = currency.upper()
        if account_num not in self.bank_account.keys():
            return f"ERROR: No such account was found ({account_num})."
        if amount <= 0:
            return f"ERROR:  can not be({amount})"
        if currency not in self.available_currencies:
            return f"ERROR: The currency is not in the list of currencies ({currency}) \n" \
                   f"Available currencies: {self.available_currencies}"
        if (currency != "ILS") and \
                (self.bank_account[account_num].is_foreign_currency is False):
            return f"ERROR: Account ID ({account_num}) doesn't support foreign currency ({currency})."
        else:
            if currency == "ILS":
                self.bank_account[account_num].balance['ILS'] += amount
            if currency == "USD":
                self.bank_account[account_num].balance['USD'] += amount
            bank_account.Bank_account.log_transaction(self.bank_account[account_num]['account_details'], 'deposit',
                                                      currency, amount)

    def withdraw(self, account_num: int, amount: int, currency: str):
        currency = currency.upper()
        if account_num not in self.bank_account.keys():
            return f"ERROR: No such account was found ({account_num})."
        if amount <= 0:
            return f"ERROR:  can not be({amount})"
        if currency not in self.available_currencies:
            return f"ERROR: The currency is not in the list of currencies ({currency}) \n" \
                   f"Available currencies: {self.available_currencies}"
        if (currency != "ILS") and \
                (self.bank_account[account_num].is_foreign_currency is False):
            return f"ERROR: Account ID ({account_num}) doesn't support foreign currency ({currency})."
        if amount > self.bank_account[account_num].balance[0] + self.bank_account[account_num].balance[
            1] * self.usd_rate + \
                self.bank_account[account_num].credit_limit:
            return f"ERROR: You tried to withdraw an amount that is too large, it exceeds the credit limit."

        else:
            if currency == "ILS":
                self.bank_account[account_num].balance['ILS'] += amount
            if currency == "USD":
                self.bank_account[account_num].balance['USD'] += amount
            bank_account.Bank_account.log_transaction(self.bank_account[account_num], 'deposit', currency, amount)

    def get_cashflow(self, account_num: int, month: int, year: int):
        if account_num not in self.bank_account.keys():
            return f"ERROR:Account number not found {account_num} "
        else:
            for key in self.bank_account[account_num].transaction_db.keys():
                m = key.split('/')[1]
                y = key.split('/')[2]
                if m == month and y == year:
                    print(m, y)