class Account:
    def __init__(test, initial_amount):
        test.__balance = initial_amount
    def withdraw(self, amount):
        self.__balance = str(float(self.__balance) - amount)
    def deposit(self, amount):
        self.__balance = str(float(self.__balance) + amount)
    def get_balance(self):
        print("The available balance of the account is: "+str(self.__balance))

ac = Account(1000)
ac.withdraw(500)
ac.deposit(800)
ac.get_balance()