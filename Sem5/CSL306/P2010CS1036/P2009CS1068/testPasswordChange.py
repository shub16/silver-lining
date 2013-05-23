import unittest
import changePasswordApp as app

class testValidate(unittest.TestCase):
	"""Class for the test cases."""
		
	def testValidateA(self):
		self.obj=app.changePassword("ahjgdgf", "dhjdgfh565", "asdfgh2", "asdfgh2")
		self.assertEqual(self.obj.checkPasswordValidity(), True, "The test case A failed!")
	
	def testValidateB(self):
		self.obj=app.changePassword("lkjhggd", "ljhgfsjk575", "abcdefg5678", "abcdefg5678")
		self.assertEqual(self.obj.checkPasswordValidity(), True, "The test case B failed!")
		
	def testValidateC(self):
		self.obj=app.changePassword("akdhjsjgfh", "jdhnb47u8", "abcdefghi", "abcdefghi")
		self.assertEqual(self.obj.checkPasswordValidity(), False, "Only alphabets are not allowed!")
		
	def testValidateD(self):
		self.obj=app.changePassword("hsjdgfdnfv", "dhsf4356", "123456789", "123456789")
		self.assertEqual(self.obj.checkPasswordValidity(), False, "Only digits are not allowed!")
	
	def testValidateE(self):
		self.obj=app.changePassword("oeiyrbbchg", "bndgfd546", "abc123", "abc123")
		self.assertEqual(self.obj.checkPasswordValidity(), False, "Passwords of length equal to 6 are not allowed")
	
	def testValidateF(self):
		self.obj=app.changePassword("wiruhdbcbr", "oweueuy65", "abc123", "def123")
		self.assertEqual(self.obj.checkPasswordValidity(), False, "The two Passwords should match")
		
	def testValidateG(self):
		self.obj=app.changePassword("alskjf466", "eiyu5hdhj", "abcd;1234", "abcd;1234")
		self.assertEqual(self.obj.checkPasswordValidity(), False, "Special characters are not allowed")
		
	def testValidateH(self):
		self.obj=app.changePassword("iejxmn46", "iedjkncm764", "a1b2c", "a1b2c")
		self.assertEqual(self.obj.checkPasswordValidity(), False, "Passwords of length less than 6 are not allowed")
	
	def testValidateI(self):
		self.obj=app.changePassword("askjdskj437", "fghjd7546", "", "")
		self.assertEqual(self.obj.checkPasswordValidity(), False, "Empty Strings are not allowed")
		
def main():
	"""Main function."""
	unittest.main()
	
if __name__=="__main__":
	main()