import random
import os.path

class NameGenerator:

	PREFIX_FIRSTWORDS = 'firstwords'
	PREFIX_LASTWORDS = 'lastwords'
	SUFFIX_MEMBER = 'member'

	def __init__ (self, type):
		self.type = type
		self.__firstwords = self.readWords(PREFIX_FIRSTWORDS)
		self.__lastwords = self.readWords(PREFIX_LASTWORDS)

	def readWords(self, preffix):
		words = []
		filename = preffix
		if not os.path.isfile(preffix + self.type):
			filename += SUFFIX_MEMBER
		else:
			filename += self.type

		with open(filename) as wordsFile:
			for word in wordsFile:
				words.append(word.rstrip())
		return words

	def generate(self):
		return self.randomWord(self.__firstwords) + " " + self.randomWord(self.__lastwords)
	
	def randomWord(self, words=[]):
		return words[random.randint(0, len(words) - 1)]
