#Test-suite for the TkinterAPI function
import TkinterAPI
import unittest

class TestTkinterAPI(unittest.TestCase):
	#...........Test for failure...............
	def testNotSame(self):		#Test for different passwords	
		result = TkinterAPI.validate("password1","password2")
		self.assertEqual(result[0],False)
		
	def testLength(self):		#Test for password length
		result = TkinterAPI.validate("new123","new123")
		self.assertEqual(result[0],False)
		
	def testAllAlpha(self):		#Test for all alphabetical characters in password
		result = TkinterAPI.validate("password","password")
		self.assertEqual(result[0],False)
		
	def testAllNumber(self):	#Test for all numbers in password
		result = TkinterAPI.validate("1234567","1234567")
		self.assertEqual(result[0],False)
		
	def testNotAlnum(self):		#Test for password containing special characters
		result = TkinterAPI.validate("123$#abc","123$#abc")
		self.assertEqual(result[0],False)
		
	def testEmpty(self):		#Test for empty pasword
		result = TkinterAPI.validate("","")
		self.assertEqual(result[0],False)
		
	def testCapital(self):		#Test for passwords having characters in different cases 
		result = TkinterAPI.validate("abcdef123","ABCDEF123")
		self.assertEqual(result[0],False)
		
	#...........Test for Success...................
	def testValid(self):		#Test for valid password
		result = TkinterAPI.validate("passwd123","passwd123")
		self.assertEqual(result[0],True)
		
	#...........Test for Sanity....................
	def testNotSameCond(self):	#Test for number of conditions for different passwords
		result = TkinterAPI.validate("password1","password2")
		self.assertEqual(result[1],1)
		
	def testLengthCond(self):	#Test for number of conditions for equal passwords but invalid length
		result = TkinterAPI.validate("new123","new123")
		self.assertEqual(result[1],3)
		
	def testAllAlphaCond(self):	#Test for number of conditions for all alphabetical characters in password
		result = TkinterAPI.validate("password","password")
		self.assertEqual(result[1],2)
		
	def testAllNumCond(self):	#Test for number of conditions for all numbers in password
		result = TkinterAPI.validate("1234567","1234567")
		self.assertEqual(result[1],2)
		
	def testNotAlnumCond(self):		#Test for number of conditions for password containing special characters
		result = TkinterAPI.validate("123$#abc","123$#abc")
		self.assertEqual(result[1],2)
		
	def testEmptyCond(self):	#Test for number of conditions for empty pasword
		result = TkinterAPI.validate("","")
		self.assertEqual(result[1],2)
		
	def testCapitalCond(self):	#Test for number of conditions for passwords having characters in different cases 
		result = TkinterAPI.validate("abcdef123","ABCDEF123")
		self.assertEqual(result[1],1)

if __name__=='__main__':
	unittest.main()
