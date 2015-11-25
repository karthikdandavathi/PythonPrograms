import unittest
import find_duplicate

class TestFindDuplicate(unittest.TestCase):
	
	def test_for_null_input(self):
		#test = Test()
		self.assertEqual(find_duplicate(inp=[]))
		return True


if __name__=="__main__":
	unittest.main()	