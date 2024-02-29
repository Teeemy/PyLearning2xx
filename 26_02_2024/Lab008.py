class BankAccount:
    def __init__(self):  # construtor
        self.balance = 0
        self.__private_var = 100

    def public_function(self): #public fnc can be used to access the private variable
        print(self.__private_var)
    def deposit(self, amount):
        self.balance += amount # public var

    def _withdraw(self, amount):# protected var
        self.balance -= amount

    def __show_balance(self): #private
        print("Your Bal ", self.balance)

    def if_you_are_authenticated(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")

    def do_withdraw_by_bank_manager(self, amount):# Can call the func bcus its within d  class
        self._withdraw(amount=amount)


Access_bank = BankAccount()
Access_bank.deposit(11000)# public func
Access_bank.balance
Access_bank.do_withdraw_by_bank_manager(3500) # prtoected fn called by method
Access_bank.if_you_are_authenticated(True)
Access_bank.public_function()