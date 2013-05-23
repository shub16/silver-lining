'''This file demonstrates the unit test suite'''

import unittest
import assignment5 as change_pass 

''' This class is used for test cases'''
class testCases(unittest.TestCase):
	def test_case1(self):
		self.check=change_pass.Pass("nchy13", "sn3Ak3r@nchy13", "nabhqwer", "asdfghj")
		self.assertEqual(self.check.valid(), False, "Only alphabets in password are not acceptable!")		
	
	def test_case2(self):
		self.check=change_pass.Pass("nchy13", "sn3Ak3r@nchy13", "106761444", "44412613")
		self.assertEqual(self.check.valid(), False, "Only digits in password are not acceptable!")		
	
	def test_case3(self):
		self.check=change_pass.Pass("nchy13", "sn3Ak3r@nchy13", "mnb123", "lkj987")
		self.assertEqual(self.check.valid(), False, "Password of length less than 7 not acceptable!")		
	
	def test_case4(self):
		self.check=change_pass.Pass("nchy13", "sn3Ak3r@nchy13", "asdf1234", "abcde342")
		self.assertEqual(self.check.valid(), False, "The password fields should match!")		
	
	def test_case5(self):
		self.check=change_pass.Pass("nchy13", "sn3Ak3r@nchy13", "asd", "poi")
		self.assertEqual(self.check.valid(), False, "Passwords of length less than 6 are not acceptable!")
		
		
	def test_case7(self):
		self.check=change_pass.Pass("nchy13", "sn3Ak3r@nchy13", "", "")
		self.assertEqual(self.check.valid(), False, "password field should nt be empty")
		
		
if __name__=="__main__":
	unittest.main()
	
