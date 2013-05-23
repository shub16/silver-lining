import Assignment5b
import unittest
class TestMainFunction(unittest.TestCase):

    # test for success
    def test1(self):
            IsValid = Assignment5b.Validate("abcd123","abcd123")
            self.assertEqual(IsValid,True);

    # test for failure when password and re-entered password not equal
    def test2(self):
		    IsValid = Assignment5b.Validate("abcdfd123","cgytgh678")
		    self.assertEqual(IsValid,False);

    # test for failure when paswword length is not more than 6.
    def test3(self):
            IsValid = Assignment5b.Validate("qwe1","qwe1")
            self.assertEqual(IsValid,False);
    
   # Test for failure when password contains only alphabets
    def test4(self):
            IsValid = Assignment5b.Validate("onlyalpha","onlyalpha")
            self.assertEqual(IsValid,False);

   # test for failure when password contains only digits
    def test5(self):
            IsValid = Assignment5b.Validate("1234567","1234567")
            self.assertEqual(IsValid,False);

   # test for failure when password has non-alphanumeric characters
    def test6(self):
            IsValid = Assignment5b.Validate("special@234","special@234")
            self.assertEqual(IsValid,False);

   # test for failure when one field is empty
    def test7(self):
            IsValid = Assignment5b.Validate("empty123","")
            self.assertEqual(IsValid,False);

   # test for failure when both fields are empty
    def test8(self):
            IsValid = Assignment5b.Validate("","")
            self.assertEqual(IsValid,False);

   # test for failure when the two passwords have different cases
    def test9(self):
            IsValid = Assignment5b.Validate("case123","CASE123")
            self.assertEqual(IsValid,False);
if __name__ == '__main__':
    unittest.main()
