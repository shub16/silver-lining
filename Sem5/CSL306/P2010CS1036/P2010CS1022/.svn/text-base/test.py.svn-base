import asg5 as test
import unittest

class PasswordTester(unittest.TestCase):	
    # test for success
    def testSuccess(self):
		Valid = test.Validate('yeah123', 'yeah123')
		self.assertEqual(Valid, None);

    # test for failure when password and re-entered password not equal
    def testFail1(self):
		Fail = test.Validate('yeah123', 'yeah12')
		self.assertEqual(Fail, None);

	# test for failure when the two passwords have different cases
    def testFail2(self):
	    Fail = test.Validate('Yeah123', 'yeah123')
	    self.assertEqual(Fail, None);
	    
   # test for failure when paswword contains all alphabets
    def testFail3(self):
		Fail = test.Validate('yeahyeah', 'yeahyeah')
		self.assertEqual(Fail, None);

    # test for failure when password contains all digits
    def testFail4(self):
	    Fail = test.Validate('1234567', '1234567')
	    self.assertEqual(Fail, None);

    # test for failure when password length is less than equal to 6
    def testFail5(self):
	    Fail = test.Validate('yeah', 'yeah')
	    self.assertEqual(Fail, None);

    # test for failure when one field is empty
    def testFail6(self):
	    Fail = test.Validate('yeah123', '')
	    self.assertEqual(Fail, None);

    # test for failure when both fields are empty
    def testFail7(self):
	    Fail = test.Validate('', '')
	    self.assertEqual(Fail, None);

    # test for failure when password has non-alphanumeric characters
    def testFail8(self):
	    Fail = test.Validate('yeah123*!', 'yeah123*!')
	    self.assertEqual(Fail, None);    

if __name__ == '__main__':
    unittest.main()
