import unittest
import LeapYear

class testLeap(unittest.TestCase):

	def test_leap(self):
		self.assertEqual(LeapYear.leap(2012), 1)

if __name__ == '__main__':
	unittest.main()
