import unittest
import LeapYear

class testLeap(unittest.TestCase):

	def test_leap(self):
		self.assertEqual(LeapYear.leap(2012), 1)

	def test_leap_1(self):
		self.assertEqual(LeapYear.leap(1800), 0)

	def test_leap_2(self):
		self.assertEqual(LeapYear.leap(2000), 1)

if __name__ == '__main__':
	unittest.main()
