import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.players import ATTR_TYPE, Attribute, Member

class TestMember(unittest.TestCase):

	def test_attribute(self):
		honor = 25
		attr = Attribute(honor)
		self.assertEquals(honor, attr.getValue())
		self.assertEquals(honor + 10, attr.increase(10))
		self.assertEquals(honor, attr.decrease(10))

	def test_member_basic_getters(self):
		honor = 25
		inertia = 20
		heat = 10
		notoriety = 15
		attributes = {
			ATTR_TYPE.HONOR: Attribute(honor),
			ATTR_TYPE.INERTIA: Attribute(inertia),
			ATTR_TYPE.HEAT: Attribute(heat),
			ATTR_TYPE.NOTORIETY: Attribute(notoriety)
		}
		name = 'Kermit'
		gang = 'The Muppets'
		member = Member(None, name, gang, attributes)
		self.assertEquals(name, member.getName())
		self.assertEquals(gang, member.getGroup())
		self.assertEquals(honor, member.getAttributes()[ATTR_TYPE.HONOR].getValue())
		self.assertEquals(inertia, member.getAttributes()[ATTR_TYPE.INERTIA].getValue())
		self.assertEquals(notoriety, member.getAttributes()[ATTR_TYPE.NOTORIETY].getValue())
		self.assertEquals(heat, member.getAttributes()[ATTR_TYPE.HEAT].getValue())

	def test_member_step_moved(self):
		inertia = 20
		heat = 5
		attributes = {
			ATTR_TYPE.INERTIA: Attribute(inertia),
			ATTR_TYPE.HEAT: Attribute(heat),
		}
		member = Member(None, None, None, attributes)

		hasMoved = member.step()
		self.assertEquals(1, hasMoved)
		self.assertEquals(heat + 10 - 1, member.getAttributes()[ATTR_TYPE.HEAT].getValue())

	def test_member_step_not_moved(self):
		inertia = 0
		heat = 10
		attributes = {
			ATTR_TYPE.INERTIA: Attribute(inertia),
			ATTR_TYPE.HEAT: Attribute(heat),
		}
		member = Member(None, None, None, attributes)

		hasMoved = member.step()
		self.assertEquals(0, hasMoved)
		self.assertEquals(heat - 1, member.getAttributes()[ATTR_TYPE.HEAT].getValue())

	def test_member_step_no_heat(self):
		inertia = 0
		heat = 0
		attributes = {
			ATTR_TYPE.INERTIA: Attribute(inertia),
			ATTR_TYPE.HEAT: Attribute(heat),
		}
		member = Member(None, None, None, attributes)

		hasMoved = member.step()
		self.assertEquals(0, hasMoved)
		self.assertEquals(heat, member.getAttributes()[ATTR_TYPE.HEAT].getValue())
		
if __name__ == '__main__':
	unittest.main()