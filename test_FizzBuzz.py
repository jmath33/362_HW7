import unittest
import FizzBuzz

class testhw7(unittest.TestCase):

	def test_hw7(self):
		self.assertEqual(FizzBuzz.FB(0), 1)

	def test_hw7_1(self):
		self.assertEqual(FizzBuzz.FB(1), 1)

if __name__ == '__main__':
	unittest.main()
