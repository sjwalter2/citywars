class Business:

    TYPES = ['Taxis','Laundry','Barbers','Shipping','Bonds','Delivery','Pizza Parlor','Taco Shack','Real Estate','Printing Company','Tourist Trap','Ice Cream Plaza']

    def __init__(self, type, name, income):
        self.__type = type
        self.__name = name
        self.__income = income

    def getIncome(self):
        return self.__income

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def toJSON(self):
        return {
            'business': {
                'type': self.__type,
                'name': self.__name,
                'income': self.__income
            }
        }