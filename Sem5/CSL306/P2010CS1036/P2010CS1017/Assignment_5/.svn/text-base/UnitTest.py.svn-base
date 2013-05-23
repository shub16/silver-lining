import assignment5
import unittest

class TestMainFunction(unittest.TestCase):

    # test for success
    def test1(self):
            IsValid = assignment5.validate("abcd123","abcd123")
            if(self.assertEqual(IsValid,True) == None):
	    	print "#Test Case passed"

    # test for failure when password and re-entered password not equal
    def test2(self):
	    IsValid = assignment5.validate("abcdfd123","cgytgh678")
	    if(self.assertEqual(IsValid,False) == None):
	    	print "#Test Case passed"

    # test for failure when paswword length is not more than 6.
    def test3(self):
            IsValid = assignment5.validate("qwe1","qwe1")
            if(self.assertEqual(IsValid,False) == None):
	    	print "#Test Case passed"

    
   # Test for failure when password contains only alphabets
    def test4(self):
            IsValid = assignment5.validate("onlyalpha","onlyalpha")
            if(self.assertEqual(IsValid,False) == None):
	    	print "#Test Case passed"

   # test for failure when password contains only digits
    def test5(self):
            IsValid = assignment5.validate("1234567","1234567")
            if(self.assertEqual(IsValid,False) == None):
	    	print "#Test Case passed"


   # test for failure when password has non-alphanumeric characters
    def test6(self):
            IsValid = assignment5.validate("special@234","special@234")
            if(self.assertEqual(IsValid,False) == None):
	    	print "#Test Case passed"


   # test for failure when one field is empty
    def test7(self):
            IsValid = assignment5.validate("empty123","")
            if(self.assertEqual(IsValid,False) == None):
	    	print "#Test Case passed"


   # test for failure when both fields are empty
    def test8(self):
            IsValid = assignment5.validate("","")
            if(self.assertEqual(IsValid,False) == None):
	    	print "#Test Case passed"


   # test for failure when the two passwords have different cases
    def test9(self):
            IsValid = assignment5.validate("case123","CASE123")
            if(self.assertEqual(IsValid,False) == None):
	    	print "#Test Case passed"

if __name__ == '__main__':
    unittest.main()
