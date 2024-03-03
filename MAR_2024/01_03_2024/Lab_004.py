# using custom exception to create a program to check bal
# this is done by inheriting a class called EXCEPTION
class MyCustomException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)# it means whatever message here is gottn from exception constructor whic is the parent

balance = 1000
withdraw_amount = int(input("Enter the amount you can withdraw \n"))

if withdraw_amount > balance:
    raise MyCustomException("Balance is low!")
else:
    print("Total after withdraw ",balance-withdraw_amount)