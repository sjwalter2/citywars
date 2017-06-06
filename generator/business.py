import random
from generator.naming import NameGenerator
from model.business import Business

class BusinessGenerator:

	MIN_INCOME = 1
	MAX_INCOME = 8

	def __init__(self):
		self.__nameGenerator = NameGenerator()

	def generate(self):
		return Business(self.getRandomType(), self.__nameGenerator.generateFirstName(), self.getRandomIncome())

	def getRandomType(self):
		return Business.TYPES[random.randint(0, len(Business.TYPES) - 1)]

	def getRandomIncome(self):
		return random.randint(BusinessGenerator.MIN_INCOME, BusinessGenerator.MAX_INCOME)
