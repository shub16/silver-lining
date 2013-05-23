import Assignment5 as pwd	#Name of file having password validation method
import unittest

class Unit_test_for_validation(unittest.TestCase):
	def testcase1(self):																						#Case when password length is < 6.
		self.check1 = pwd.CheckPassword("ABCDEF","1234qwert","123qw","123qw")
		self.assertEqual(self.check1,False);
	
	def testcase2(self):																						#Case when password length is = 6.
		self.check2 = pwd.CheckPassword("ABCDEF","1234qwert","123qwe","123qwe")
		self.assertEqual(self.check2,False);
	
	def testcase3(self):																						#Case when password is purely numeric.
		self.check3 = pwd.CheckPassword("ABCDEF","1234qwert","12345678","1235678")
		self.assertEqual(self.check3,False);
	
	def testcase4(self):																						#Case when password is purely alphabatic.
		self.check4 = pwd.CheckPassword("ABCDEF","1234qwert","qwertyui","qwertyui")
		self.assertEqual(self.check4,False);
	
	def testcase5(self):																						#Case when password contains special characters.
		self.check5 = pwd.CheckPassword("ABCDEF","1234qwert","1234qwer$#@!","1234qwer$#@!")
		self.assertEqual(self.check5,False);
	
	def testcase6(self):																						#Case when password field is left empty.
		self.check6 = pwd.CheckPassword("ABCDEF","1234qwert","1234qwer","")
		self.assertEqual(self.check6,False);
	
	def testcase7(self):																						#Case when passwords do not match.
		self.check7 = pwd.CheckPassword("ABCDEF","1234qwert","1234qwer","qwer1234")
		self.assertEqual(self.check7,False);
		
	def testcase8(self):																						#Case when password matched and changed.
		self.check8 = pwd.CheckPassword("ABCDEF","1234qwert","1234qwer","1234qwer")
		self.assertEqual(self.check8,True);

if __name__=='__main__':
	unittest.main()
