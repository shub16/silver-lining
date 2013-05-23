import Assignment5
import unittest

class TestMainFunction(unittest.TestCase):

    # test for success
    def test1(self):
            IsValid = Assignment5.IsValidPswd("shanu123","shanu123")
            self.assertEqual(IsValid,True);

    # test for failure when password and re-entered password not equal
    def test2(self):
		    IsValid = Assignment5.IsValidPswd("shanu1234","shanu123")
		    self.assertEqual(IsValid,False);

    # test for failure when paswword length is not more than 6.
    def test3(self):
            IsValid = Assignment5.IsValidPswd("shanu1","shanu1")
            self.assertEqual(IsValid,False);# test for failure when password contains all digits
    
   # Test for failure when password contains only alphabets
    def test4(self):
            IsValid = Assignment5.IsValidPswd("shanushanu","shanushanu")
            self.assertEqual(IsValid,False);

 # test for failure when password contains only digits
 
    def test5(self):
            IsValid = Assignment5.IsValidPswd("1234567","1234567")
            self.assertEqual(IsValid,False);

     # test for failure when password has non-alphanumeric characters
    def test6(self):
            IsValid = Assignment5.IsValidPswd("shanu$123","shanu$123")
            self.assertEqual(IsValid,False);

	# test for failure when one field is empty
   
    def test7(self):
            IsValid = Assignment5.IsValidPswd("shanu123","")
            self.assertEqual(IsValid,False);

	 # test for failure when both fields are empty
   
    def test8(self):
            IsValid = Assignment5.IsValidPswd("","")
            self.assertEqual(IsValid,False);

    # test for failure when the two passwords have different cases
    def test9(self):
            IsValid = Assignment5.IsValidPswd("shanu123","SHANU123")
            self.assertEqual(IsValid,False);
if __name__ == '__main__':
    unittest.main()
