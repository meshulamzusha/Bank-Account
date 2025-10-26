class BankAccount:

    def __init__(self, account_holder: str, initial_balance: float) -> None:
        self.account_holder = account_holder
        self.balance = initial_balance


    def transfer_funds(self, other_account: "BankAccount", amount: float) -> None:
        if self.balance >= other_account.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f'Successfully transferred {amount} shekels to {other_account.account_holder}')
        else:
            print(f'Transfer failed. You have less than {amount} shekels in your balance.')


    def __str__(self) -> str:
        return f'account holder name: {self.account_holder} current balance: {self.balance}'