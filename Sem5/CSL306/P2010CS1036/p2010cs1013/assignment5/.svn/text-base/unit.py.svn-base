import assignment5
import unittest

class TestMainFunction(unittest.TestCase):

    # testCase for success
    def testCase1(self):
	
	print 'testcase1'
        self.check = assignment5.changePassword("Gaurav ","qwertygh123","qwz123456","qwz123456")
        self.assertEqual(self.check.checkPasswordValidity(),True,' working');
	
    # testCase for failure when password and re-entered password not equal
    def testCase2(self):
	
	print 'testcase2'
        self.check = assignment5.changePassword("lkjhggd", "ljhgfsjk575", "qwertyg5678", "qwertyg56")
        self.assertEqual(self.check.checkPasswordValidity(),False);
	

    # testCase for failure when paswword length is not more than 6.
    def testCase3(self):
	
	print 'testcase3'
        self.check = assignment5.changePassword("Gaurav ","qwertygh123","qw12","qw12")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Passwords of length less than 6 are not allowed.");
    
    # Test for failure when password contains only alphabets
    def testCase4(self):
    	print 'testcase4'
        self.check = assignment5.changePassword("Gaurav ","qwertygh123","qwzabcd","qwzabcd")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Only alphabets are not allowed!");

    # testCase for failure when password contains only digits 
    def testCase5(self):
    	print 'testcase5'
        self.check = assignment5.changePassword("Gaurav ","qwertygh123","1234569","1234569")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Only digits are not allowed!");

    # testCase for failure when password has non-alphanumeric characters
    def testCase6(self):
    	print 'testcase6'
        self.check = assignment5.changePassword("Gaurav ","qwertygh123","qwz1234$","qwz1234$")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Special characters are not allowed!");

    # testCase for failure when field is empty   
    def testCase7(self):
    	print 'testcase7'
        self.check = assignment5.changePassword("Gaurav ","qwertygh123","qwz123456","")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Empty Strings are not allowed!");

    def testCase8(self):
    	print 'testcase8'
        self.check = assignment5.changePassword("Gaurav ","qwertygh123","qwz123","qwz123")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Password length must be greater than 6.");
if __name__ == '__main__':
    unittest.main()

