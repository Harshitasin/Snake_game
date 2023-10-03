#Encapsulation
from ast import Pass
class Atm:
    def __init__(self):
        self.pin = ""
        self.__balance = 0
        #self.menu()

    def menu(self):
        user_input = input("""How may I help you
    press 1 to create pin
    press 2 to change pin
    press 3 to check balance
    press 4 to withdraw the amount
    press 5 to exit\n""")

        if user_input == "1":
            # create pin
            self.create_pin()
        elif user_input == "2":
            # change pin
            self.change_pin()
        elif user_input == "3":
            # check balance
            self.check_balance()
        elif user_input == "4":
            # withdraw
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter your pin")
        self.pin = user_pin
        user_balance = int(input("Enter balance"))
        self.__balance = user_balance
        print("pin created successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter your old pin")
        if old_pin == self.pin:
            new_pin = input("Enter your new pin")
            self.pin = new_pin
            print("Pin changed successfully")
        else:
            print("Bhaag jao yha se")
        self.menu()

    def check_balance(self):
        user_pin = input("Pin input kar na re")
        if user_pin == self.pin:
            print("Your balance is", self.__balance)
        else:
            print("Bhai garib ho tum")
        self.menu()

    def withdraw(self):
        user_pin = input("Pin input kar na re")
        if user_pin == self.pin:
            self.amount = int(input("How much you want\n"))
            if self.__balance >= self.amount:
                self.balance = self.__balance - self.amount
                print("Succesfully withdraw")
                print("Remainig balance is", self.balance)
            else:
                print("Bhai itte paise nhi rakha h tu")
        else:
            print("chal bhaag")
        self.menu()

obj=Atm()
#obj.create_pin()
obj.balance="hehehe"
obj.create_pin()
obj.withdraw()

