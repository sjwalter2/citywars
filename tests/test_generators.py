import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.business import Business
from generator.business import BusinessGenerator
from generator.naming import NameGenerator

class TestBusinessGenerator(unittest.TestCase):

	def setUp(self):
		self.generator = BusinessGenerator()

	def test_getRandomIncome(self):
		self.assertIsNotNone(self.generator.getRandomIncome())
		self.assertGreaterEqual(self.generator.getRandomIncome(), BusinessGenerator.MIN_INCOME)
		self.assertLessEqual(self.generator.getRandomIncome(), BusinessGenerator.MAX_INCOME)

if __name__ == '__main__':
	unittest.main()