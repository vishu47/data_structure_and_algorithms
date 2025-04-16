class Banking:
    def __init__(self, account_no, branch, name, account_Type, balance=0):
        self.account_no = account_no
        self.branch = branch
        self.name = name
        self.account_Type = account_Type
        self.balance = balance

    def displayAccountDetails(self):
        print(f"account_no : {self.account_no}")
        print(f"branch : {self.branch}")
        print(f"name : {self.name}")
        print(f"account_Type : {self.account_Type}")
        print(f"balance : {self.balance}\n\n")

    def getBalance(self):
        return self.balance

    def depositBalance(self, balance):
        self.balance = self.balance + balance
        return self.balance

    def withdrawn(self, balance):
        if self.balance >= balance:
            self.balance = self.balance - balance
            return self.balance
        else:
            print(f"Are you begger?")


accounts = []
while True:
    print(f"1. Add account details")
    print(f"2. Display Account Details")
    print(f"3. Get Balance detailes of account")
    print(f"4. Diposit amount to account")
    print(f"5. withdrawn from account :")
    print(f"6. Exit")
    print(f"7. Transfer money :")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        name = input("Enter your name : ")
        number = int(input("Enter your account number : "))
        branch = input("Enter your account branch : ")
        account_Type = input("Enter your account account_Type : ")
        if account_Type != "savings" or account_Type != "current":
            print(f"only allowed savings or current")
            account_Type = input("Enter your account account_Type : ")

        x = Banking(number, branch, name, account_Type)
        accounts.append(x)
        print(accounts)
    elif choice == 2:
        for acc in accounts:
            acc.displayAccountDetails()
    elif choice == 3:
        pass
    elif choice == 4:
        number = int(input("Enter account number: "))
        print(number)
        for acc in accounts:
            if number == acc.account_no:
                x = int(input("enter amount to be diposited : "))
                print(acc.depositBalance(x))
                break

    elif choice == 5:
        number = int(input("Enter account number: "))
        for acc in accounts:
            if number == acc.account_no:
                x = int(input("enter amount to be debited : "))
                acc.withdrawn(x)
                break
    elif choice == 6:
        break
