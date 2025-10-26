from BankAccount import BankAccount

def main() -> None:
    account1 = BankAccount('avi', 50000)
    account2 = BankAccount('beni', 1200)

    print(account1)
    print(account2)

    account1.transfer_funds(account2, 3000)

    print(account1)
    print(account2)


if __name__ == '__main__':
    main()