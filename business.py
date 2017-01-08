import random
import generator

firstwordsbusiness = generator.wordlist("firstwordsmember")
#lastwordsbusiness = generator.wordlist("lastwordsbusiness")

def firstname():
    return firstwordsbusiness[random.randint(0,len(firstwordsbusiness)-1)]

#def lastname():
#    return lastwordsbusiness[random.randint(0,len(lastwordsbusiness)-1)]


def name():
    return firstname()

class business(object):
        def __init__(self):
            self.type = random.choice(["Taxis","Laundry","Barbers","Shipping","Bonds","Delivery","Pizza Parlor","Taco Shack","Real Estate","Printing Company","Tourist Trap","Ice Cream Plaza"])
            self.income = random.randint(1,8)
            self.name = name() + " " + self.type

        def getIncome(self):
            return self.income

        def getName(self):
            return self.name
