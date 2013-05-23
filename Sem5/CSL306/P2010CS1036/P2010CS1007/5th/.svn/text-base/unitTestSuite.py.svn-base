'''This file demonstrates the unit test suite'''

import unittest
import unit 

''' This class is used for test cases'''
class testCases(unittest.TestCase):
	def test_case1(self):
		self.pwd=unit.changePassword( "khalsa13raj", "waheguru", "waheguru")
		self.assertEqual(self.pwd.Check_valid(), False, "Only alphabets in password are not acceptable!")		
	
	def test_case2(self):
		self.pwd=unit.changePassword("khalsa13raj", "9876543", "9876543")
		self.assertEqual(self.pwd.Check_valid(), False, "Only digits in password are not acceptable!")		
	
	def test_case3(self):
		self.pwd=unit.changePassword("khalsa13raj", "khals1", "khals1")
		self.assertEqual(self.pwd.Check_valid(), False, "Password of length 6 is not acceptable!")		
	
	def test_case4(self):
		self.pwd=unit.changePassword("khalsa13raj", "waheguru1", "waheguru13")
		self.assertEqual(self.pwd.Check_valid(), False, "The passwords does not match!")		
	
	def test_case5(self):
		self.pwd=unit.changePassword("khalsa13raj", "dhan", "dhan")
		self.assertEqual(self.pwd.Check_valid(), False, "Passwords of length less than 6 are not acceptable!")
		
	def test_case6(self):
		self.pwd=unit.changePassword("khalsa13raj", "prabh@#", "prabh@#")
		self.assertEqual(self.pwd.Check_valid(), False, "Special character should not be there in passwords!")
		
	def test_case7(self):
		self.pwd=unit.changePassword("khalsa13raj", "", "")
		self.assertEqual(self.pwd.Check_valid(), False, "Empty passwords not accetable!")

if __name__=="__main__":
	unittest.main()
	
