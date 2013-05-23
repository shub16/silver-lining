import assignment5Main as UserPassApp
import unittest, sys

class UnitTestSuite(unittest.TestCase):

#test case for valid passwords which are alphanumeric and greater than 6 in length and match
    def testCaseA(self):
        self.result = UserPassApp.checkValidity("Praneeth","default_pass","newpass123","newpass123")
        self.assertEqual(self.result,True,"Valid Password Combination failed!");
    
#test case for password less then 6 characters
    def testCaseB(self):
        self.result = UserPassApp.checkValidity("Praneeth","default_pass","pass","pass")
        self.assertEqual(self.result,False,"Passwords of length less then or equal to 6 are allowed!");
    
#test case for passwords which contain only alphabets
    def testCaseC(self):
        self.result = UserPassApp.checkValidity("Praneeth","default_pass","passxyz","passxyz")
        self.assertEqual(self.result,True,"Password containing only alphabets not allowed!");

#test case for passwords which contain only digits
    def testCaseD(self):
        self.result = UserPassApp.checkValidity("Praneeth","default_pass","01234569","01234569")
        self.assertEqual(self.result,True,"Password containing only digits not allowed!");

#test case for passwords which have special characters(not alphanumeric)
    def testCaseE(self):
        self.result = UserPassApp.checkValidity("Praneeth","default_pass","pass123$","pass123$")
        self.assertEqual(self.result,False,"Password which are not alphanumeric are allowed!");

#test case for passwords which are empty
    def testCaseF(self):
        self.result = UserPassApp.checkValidity("Praneeth","default_pass","newpass123","")
        self.assertEqual(self.result,False,"Empty Passwords are allowed!");

class devnull():
    def write(self, data):
        pass

if __name__ == '__main__':

#removing internal IO redirection so that garbage is not printed onto terminal while testing
    f = devnull()
    orig_stdout = sys.stdout
    sys.stdout = f

    unittest.main()

