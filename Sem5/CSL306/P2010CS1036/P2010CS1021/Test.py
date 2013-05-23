import A5
import unittest
ex = A5.CommonAPI("A5", 400, 300)

class PwdTest(unittest.TestCase):
    def testSuccess(self):                                     # Test for success
		Valid = ex.PwdValidate('New1212', 'New1212')
		self.assertEqual(Valid, None)

    def testFail1(self):                                       # field is empty
	    Fail = ex.PwdValidate('New1212', '')
	    self.assertEqual(Fail, None)

    def testFail2(self):                                       # both fields are empty
	    Fail = ex.PwdValidate('', '')
	    self.assertEqual(Fail, None)         

    def testFail3(self):                                       # password length is less than equal to 6
	    Fail = ex.PwdValidate('New12', 'New12')
	    self.assertEqual(Fail, None)
  
    def testFail4(self):                                       # new password and re-entered password not equal
	    Fail = ex.PwdValidate('New1212', 'New121')
	    self.assertEqual(Fail, None)

    def testFail5(self):                                       # password has non-alphanumeric characters
	    Fail = ex.PwdValidate('new_12*#', 'new_12*#')
	    self.assertEqual(Fail, None)

    def testFail6(self):                                       # Passwords have different cases
	    Fail = ex.PwdValidate('New1212', 'new1212')
	    self.assertEqual(Fail, None)
	    
    def testFail7(self):                                       # password contains all alphabets
		Fail = ex.PwdValidate('Newold', 'Newold')
		self.assertEqual(Fail, None)

    def testFail8(self):                                       # password contains all digits
	    Fail = ex.PwdValidate('121212', '121212')
	    self.assertEqual(Fail, None)

if __name__ == '__main__':
    unittest.main()
