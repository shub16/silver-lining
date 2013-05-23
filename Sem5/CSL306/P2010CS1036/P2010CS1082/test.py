import lab5 as out
import unittest

class PasswordTester(unittest.TestCase):	
    # test for success
    def testSuccess(self):
		Values = ['Tanvi116', 'Tanvi116']
		Valid = out.Validate(Values,True)
		self.assertEqual(Valid, None);

    # test for failure when password and re-entered password not equal
    def testFail1(self):
		Values = ['Tanvi116', 'Tanvi11']
		Fail = out.Validate(Values,True)
		self.assertEqual(Fail, None);

	# test for failure when the two passwords have different cases
    def testFail2(self):
	    Values = ['Tanvi116', 'Tanvi116']
	    Fail = out.Validate(Values,True)
	    self.assertEqual(Fail, None);
	    
   # test for failure when paswword contains all alphabets
    def testFail3(self):
		Values = ['Tanvi', 'Tanvi116']
		Fail = out.Validate(Values,True)
		self.assertEqual(Fail, None);

    # test for failure when password contains all digits
    def testFail4(self):
	    Values = ['11692', '11692']
	    Fail = out.Validate(Values,True)
	    self.assertEqual(Fail, None);

    # test for failure when password length is less than equal to 6
    def testFail5(self):
	    Values = ['jas11', 'jas11']
	    Fail = out.Validate(Values,True)
	    self.assertEqual(Fail, None);

    # test for failure when one field is empty
    def testFail6(self):
	    Values = ['Tanvi116', '']
	    Fail = out.Validate(Values,True)
	    self.assertEqual(Fail, None);

    # test for failure when both fields are empty
    def testFail7(self):
	    Values = ['', '']
	    Fail = out.Validate(Values,True)
	    self.assertEqual(Fail, None);

    # test for failure when password has non-alphanumeric characters
    def testFail8(self):
	    Values = ['jas_11*!', 'jas_11*!']
	    Fail = out.Validate(Values,True)
	    self.assertEqual(Fail, None);    

if __name__ == '__main__':
    unittest.main()
