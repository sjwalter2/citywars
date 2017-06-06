from generator.naming import NameGenerator
from model.players import Member

class MemberGenerator:

	def __init__(self, eventHandler, gang):
		self.__gang = gang
		self.__nameGenerator = NameGenerator(self.getType(gang.getType()))
		self.__eventHandler = eventHandler

	def generate(self):
		return Member(self.__eventHandler, self.__nameGenerator.generate(), self.__gang)

	def generateLeader(self):
		return Member(self.__eventHandler, self.__nameGenerator.generate(), self.__gang, True)

	def getType(self, gangType = ''):
		if gangType == 'gang':
			return 'member'
		elif gangType == 'force':
			return 'officer'
		elif gangType == 'league':
			return 'hero'
		else:
			return ''

