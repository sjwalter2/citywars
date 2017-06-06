import random
import os.path
import pkg_resources

class NameGenerator:

	PREFIX_FIRSTWORDS = 'firstwords'
	PREFIX_LASTWORDS = 'lastwords'
	SUFFIX_MEMBER = 'member'

	def __init__ (self, type=''):
		self.__type = type
		self.__firstwords = self.readWords(NameGenerator.PREFIX_FIRSTWORDS)
		self.__lastwords = self.readWords(NameGenerator.PREFIX_LASTWORDS)

	def readWords(self, preffix):
		words = []
		filename = preffix
		if self.__type == '' or not pkg_resources.resource_exists('generator.resources', preffix + self.__type):
			filename += NameGenerator.SUFFIX_MEMBER
		else:
			filename += self.__type

		wordsFile = pkg_resources.resource_string('generator.resources', filename)
		for word in wordsFile.decode().split('\n'):
			words.append(word.rstrip())
		return words

	def generate(self):
		return '{} {}'.format(self.generateFirstName(), self.generateLastName())

	def generateFirstName(self):
		return self.randomWord(self.__firstwords)

	def generateLastName(self):
		return self.randomWord(self.__lastwords)
	
	def randomWord(self, words=[]):
		return words[random.randint(0, len(words) - 1)]
