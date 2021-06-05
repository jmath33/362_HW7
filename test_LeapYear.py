import unittest

class testLeap(unittest.TestCase):

	def test_leap(self):
		self.assertEqual(LeapYear.leap(2012)), "Leap Year")

if __name__ == '__main__':
	unittest.main()
