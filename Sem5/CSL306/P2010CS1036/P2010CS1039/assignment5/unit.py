import assignment5
import unittest

class TestMainFunction(unittest.TestCase):

    # testCase for success
    def testCase1(self):
	print '..........'
	print 'testcase1'
        self.check = assignment5.changePassword("Vikas","abcdefgh123","xyz123456","xyz123456")
        self.assertEqual(self.check.checkPasswordValidity(),True,' working');
	
    # testCase for failure when password and re-entered password not equal
    def testCase2(self):
	print '.........'
	print 'testcase2'
        self.check = assignment5.changePassword("lkjhggd", "ljhgfsjk575", "abcdefg5678", "abcdefg56")
        self.assertEqual(self.check.checkPasswordValidity(),False);
	

    # testCase for failure when paswword length is not more than 6.
    def testCase3(self):
	print '.........'
	print 'testcase3'
        self.check = assignment5.changePassword("Vikas","abcdefgh123","xy12","xy12")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Passwords of length equal to 6 are not allowed.");
    
    # Test for failure when password contains only alphabets
    def testCase4(self):
        self.check = assignment5.changePassword("Vikas","abcdefgh123","xyzabcd","xyzabcd")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Only alphabets are not allowed!");

    # testCase for failure when password contains only digits 
    def testCase5(self):
        self.check = assignment5.changePassword("Vikas","abcdefgh123","1234569","1234569")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Only digits are not allowed!");

    # testCase for failure when password has non-alphanumeric characters
    def testCase6(self):
        self.check = assignment5.changePassword("Vikas","abcdefgh123","xyz1234$","xyz1234$")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Special characters are not allowed!");

    # testCase for failure when field is empty   
    def testCase7(self):
        self.check = assignment5.changePassword("Vikas","abcdefgh123","xyz123456","")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Empty Strings are not allowed!");

    def testCase8(self):
        self.check = assignment5.changePassword("Vikas","abcdefgh123","xyz123","xyz123")
        self.assertEqual(self.check.checkPasswordValidity(),False,"Password length must be greater than 6.");
if __name__ == '__main__':
    unittest.main()

