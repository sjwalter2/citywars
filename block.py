import random
import business

from naming.generator import NameGenerator

nameGenerator = NameGenerator('block')

class block(object):
        def __init__(self, e, x, y):
            self.e = e
            self.name = nameGenerator.generate()
            self.owner = 0
            self.business = business.business()
            self.coordinates = str(x) + "," + str(y)
            self.x = x
            self.y = y

        def getOwner(self):
            return self.owner

        def setOwner(self,owner):
            self.owner = owner

        def getBusiness(self):
            return self.business

        def getCoordinates(self):
            return self.coordinates

        def getX(self):
            return self.x

        def getY(self):
            return self.y
