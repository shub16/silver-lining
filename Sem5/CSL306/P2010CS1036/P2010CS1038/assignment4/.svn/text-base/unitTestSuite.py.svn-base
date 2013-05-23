'''This file demonstrates the unit test suite'''

import unittest
import pwd_change_app as pwd_app 

''' This class is used for test cases'''
class testCases(unittest.TestCase):
	def test_case1(self):
		self.pwd=pwd_app.change_password("qwerty", "456tyhgrd", "zxcvbnb", "zxcvbnb")
		self.assertEqual(self.pwd.check_password_validity(), False, "Only alphabets in password are not acceptable!")		
	
	def test_case2(self):
		self.pwd=pwd_app.change_password("qwerty", "456tyhgrd", "1234567", "1234567")
		self.assertEqual(self.pwd.check_password_validity(), False, "Only digits in password are not acceptable!")		
	
	def test_case3(self):
		self.pwd=pwd_app.change_password("qwerty", "456tyhgrd", "abcde2", "abcde2")
		self.assertEqual(self.pwd.check_password_validity(), False, "Password of length 6 is not acceptable!")		
	
	def test_case4(self):
		self.pwd=pwd_app.change_password("qwerty", "456tyhgrd", "abcde234", "abcde342")
		self.assertEqual(self.pwd.check_password_validity(), False, "The last 2 passwords should match!")		
	
	def test_case5(self):
		self.pwd=pwd_app.change_password("qwerty", "456tyhgrd", "abc", "abc")
		self.assertEqual(self.pwd.check_password_validity(), False, "Passwords of length less than 6 are not acceptable!")
		
	def test_case6(self):
		self.pwd=pwd_app.change_password("qwerty", "456tyhgrd", "sswer@#", "sswer@#")
		self.assertEqual(self.pwd.check_password_validity(), False, "Special character should not be there in passwords!")
		
	def test_case7(self):
		self.pwd=pwd_app.change_password("qwerty", "456tyhgrd", "", "")
		self.assertEqual(self.pwd.check_password_validity(), False, "Empty passwords not accetable!")
		
		
if __name__=="__main__":
	unittest.main()
	
