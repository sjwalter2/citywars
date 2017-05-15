import random
from naming.generator import NameGenerator

nameGenerator = NameGenerator('member')

def name():
    return firstname()

class business(object):
        def __init__(self):
            self.type = random.choice(["Taxis","Laundry","Barbers","Shipping","Bonds","Delivery","Pizza Parlor","Taco Shack","Real Estate","Printing Company","Tourist Trap","Ice Cream Plaza"])
            self.income = random.randint(1,8)
            self.name = nameGenerator.generateFirstName() + " " + self.type

        def getIncome(self):
            return self.income

        def getName(self):
            return self.name
