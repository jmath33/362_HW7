import unittest
import FizzBuzz

class testhw7(unittest.TestCase):

	def test_hw7(self):
		self.assertEqual(FizzBuzz.FB(), [1,0,0])

if __name__ == '__main__':
	unittest.main()
