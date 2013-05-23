import unit as unit
import unittest

class PasswordTester(unittest.TestCase):	
    # test for success
    def testSuccess(self):
		Valid = unit.PasswdValid('Bonani252', 'Bonani252')
		self.assertEqual(Valid, None);

    # test for failure when password and re-entered password not equal
    def testFail1(self):
		Fail = unit.PasswdValid('Bonani252', 'Bonani25')
		self.assertEqual(Fail, None);

	# test for failure when the two passwords have different cases
    def testFail2(self):
	    Fail = unit.PasswdValid('Bonani252', 'bonani252')
	    self.assertEqual(Fail, None);
	    
   # test for failure when paswword contains all alphabets
    def testFail3(self):
		Fail = unit.PasswdValid('Bonani', 'Bonani')
		self.assertEqual(Fail, None);

    # test for failure when password contains all digits
    def testFail4(self):
	    Fail = unit.PasswdValid('28692', '28692')
	    self.assertEqual(Fail, None);

    # test for failure when password length is less than equal to 6
    def testFail5(self):
	    Fail = unit.PasswdValid('bon25', 'bon25')
	    self.assertEqual(Fail, None);

    # test for failure when one field is empty
    def testFail6(self):
	    Fail = unit.PasswdValid('Bonani252', '')
	    self.assertEqual(Fail, None);

    # test for failure when both fields are empty
    def testFail7(self):
	    Fail = unit.PasswdValid('', '')
	    self.assertEqual(Fail, None);

    # test for failure when password has non-alphanumeric characters
    def testFail8(self):
	    Fail = unit.PasswdValid('bon_25*!', 'bon_25*!')
	    self.assertEqual(Fail, None);    

if __name__ == '__main__':
    unittest.main()
