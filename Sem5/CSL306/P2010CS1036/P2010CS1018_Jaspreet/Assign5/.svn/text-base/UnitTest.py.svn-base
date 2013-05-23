import OutputWindow as out
import unittest

class PasswordTester(unittest.TestCase):	
    # test for success
    def testSuccess(self):
		Valid = out.PasswdValid('Jaspreet252', 'Jaspreet252')
		self.assertEqual(Valid, None);

    # test for failure when password and re-entered password not equal
    def testFail1(self):
		Fail = out.PasswdValid('Jaspreet252', 'Jaspreet25')
		self.assertEqual(Fail, None);

	# test for failure when the two passwords have different cases
    def testFail2(self):
	    Fail = out.PasswdValid('Jaspreet252', 'jaspreet252')
	    self.assertEqual(Fail, None);
	    
   # test for failure when paswword contains all alphabets
    def testFail3(self):
		Fail = out.PasswdValid('Jaspreet', 'Jaspreet')
		self.assertEqual(Fail, None);

    # test for failure when password contains all digits
    def testFail4(self):
	    Fail = out.PasswdValid('25292', '25292')
	    self.assertEqual(Fail, None);

    # test for failure when password length is less than equal to 6
    def testFail5(self):
	    Fail = out.PasswdValid('jas25', 'jas25')
	    self.assertEqual(Fail, None);

    # test for failure when one field is empty
    def testFail6(self):
	    Fail = out.PasswdValid('Jaspreet252', '')
	    self.assertEqual(Fail, None);

    # test for failure when both fields are empty
    def testFail7(self):
	    Fail = out.PasswdValid('', '')
	    self.assertEqual(Fail, None);

    # test for failure when password has non-alphanumeric characters
    def testFail8(self):
	    Fail = out.PasswdValid('jas_25*!', 'jas_25*!')
	    self.assertEqual(Fail, None);    

if __name__ == '__main__':
    unittest.main()
