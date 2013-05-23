import demo5 as shu5
import unittest

class TestMainFunction(unittest.TestCase):

    # TestCase for success when changing of password is successful
    def testCase1(self):
	print '..........'
	print 'testcase1 :-'
        self.check = shu5.changePassword("Shubham","rvwt345vrr","a1b2c3d4","a1b2c3d4")
        self.assertEqual(self.check.checkPasswordValidity(),True);
	
    # testCase for failure when password and confirm password not equal
    def testCase2(self):
	print '.........'
	print 'testcase2:-'
        self.check = shu5.changePassword("Ahishek", "eot35345vd", "kruhw25c2 ", "kruhw25c1")
        self.assertEqual(self.check.checkPasswordValidity(),False);
	

    # testCase for failure when paswword length is not more than 6.
    def testCase3(self):
	print '.........'
	print 'testcase3'
        self.check = shu5.changePassword("Deepak","abcdefgh123","x233d","x233d")
        self.assertEqual(self.check.checkPasswordValidity(),False);
    
    # Test for failure when password contains only alphabets
    def testCase4(self):
	print '.........'
	print 'testcase4:-'
                
	self.check = shu5.changePassword("Bhupender","htdrgfgghw","xyzabcd","xyzabcd")
        self.assertEqual(self.check.checkPasswordValidity(),False);

    # testCase for failure when password contains only digits 
    def testCase5(self):
	print '.........'
	print 'testcase5:-'
        
        self.check = shu5.changePassword("shubham","abcdefgh123","1234569","1234569")
        self.assertEqual(self.check.checkPasswordValidity(),False);

    # testCase for failure when password has non-alphanumeric characters
    def testCase6(self):
	print '.........'
	print 'testcase6:-'
        
        self.check = shu5.changePassword("rahul","abcdefgh123","fdggr@65757","fdggr@65757")
        self.assertEqual(self.check.checkPasswordValidity(),False);

    # testCase for failure when field is empty   
    def testCase7(self):
	print '.........'
	print 'testcase7:-'
        
        self.check = shu5.changePassword("anirudh","sdfwe34re54","er34crtde","")
        self.assertEqual(self.check.checkPasswordValidity(),False);

    def testCase8(self):
  	print '.........'
	print 'testcase8:-'
        
        self.check = shu5.changePassword("ewctre345v","abcdefgh123","xyz123","xyz123")
        self.assertEqual(self.check.checkPasswordValidity(),False);
if __name__ == '__main__':
    unittest.main()

