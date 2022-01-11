class Atm:
    def __init__(self, name, money, cardnumber, pin, balance):
        self.name = name
        self.money = money
        self.cardnumber = cardnumber
        self.pin = pin
        self.balance = balance

    def withdraw(self):
        input1 = int(input("please enter the amount you want to withdraw: "))
        if(input1 <= self.balance):
            self.balance = self.balance - input1
            print("You have withdrawn: ", input1, "and your new balance is: ", self.balance)
        else:
            print("You have insufficient funds")



person1 = Atm("boink", 100, 123456789, 1234, 1000000)
person1.withdraw()
