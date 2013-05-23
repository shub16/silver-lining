import Assignment5 as As
import unittest

class PasswordTester(unittest.TestCase):	
    # test for success
    def testSuccess(self):
		Valid = As.Validate([1,2,'Tribune19t', 'Tribune19t'])
		self.assertEqual(Valid, None);

    # test for failure when password and re-entered password not equal
    def testFail1(self):
		Fail = As.Validate([1,2,'Tribune19t', 'Tribune19'])
		self.assertEqual(Fail, None);

	# test for failure when the two passwords have different cases
    def testFail2(self):
	    Fail = As.Validate([1,2,'Tribune19t', 'TRIBUNE19t'])
	    self.assertEqual(Fail, None);
	    
   # test for failure when paswword contains all alphabets
    def testFail3(self):
		Fail = As.Validate([1,2,'Tribunet', 'Tribunet'])
		self.assertEqual(Fail, None);

    # test for failure when password contains all digits
    def testFail4(self):
	    Fail = As.Validate([1,2,'123', '123'])
	    self.assertEqual(Fail, None);

    # test for failure when password length is less than 6
    def testFail5(self):
	    Fail = As.Validate([1,2,'Tr19t', 'Tr19t'])
	    self.assertEqual(Fail, None);

    # test for failure when one field is empty
    def testFail6(self):
	    Fail = As.Validate([1,2,'Tribune19t', ''])
	    self.assertEqual(Fail, None);

    # test for failure when both fields are empty
    def testFail7(self):
	    Fail = As.Validate([1,2,'', ''])
	    self.assertEqual(Fail, None);

    # test for failure when password has non-alphanumeric characters
    def testFail8(self):
	    Fail = As.Validate([1,2,'Tribu.ne_19t*!', 'Tribu.ne_19t*!'])
	    self.assertEqual(Fail, None);    

if __name__ == '__main__':
    unittest.main()
