import Tkinter_Test1
import unittest

class TestMainFunction(unittest.TestCase):

    #Test for success
    def test1(self):
            IsValid = apiTest1.Is_valid_pass("UnitTest123","UnitTest123")
            self.assertEqual(IsValid,True);

    #Test for failure-->One field is empty
    def test2(self):
            IsValid = apiTest1.Is_valid_pass("UnitTest123","")
            self.assertEqual(IsValid,False);

    #Test for failure-->Both fields are empty   
    def test3(self):
            IsValid = apiTest1.Is_valid_pass("","")
            self.assertEqual(IsValid,False);

    #Test for failure--> Password and re-typed password are not equal
    def test4(self):
		    IsValid = apiTest1.Is_valid_pass("UnitTest1234","UnitTest12")
		    self.assertEqual(IsValid,False);

    #Test for failure--> Password length is not more than 6.
    def test5(self):
            IsValid = apiTest1.Is_valid_pass("Unit1","Unit1")
            self.assertEqual(IsValid,False);
    
   # Test for failure--> Password contains only alphabets
    def test6(self):
            IsValid = apiTest1.Is_valid_pass("UnitTesting","UnitTesting")
            self.assertEqual(IsValid,False);

   # Test for failure--> Password contains only digits
    def test7(self):
            IsValid = apiTest1.Is_valid_pass("1234567890","1234567890")
            self.assertEqual(IsValid,False);

    #Test for failure--> Password has non-alphanumeric characters
    def test8(self):
            IsValid = apiTest1.Is_valid_pass("Unit@Test123","Unit@Test123")
            self.assertEqual(IsValid,False);


    #Test for failure--> The two passwords have different cases
    def test9(self):
            IsValid = apiTest1.Is_valid_pass("UnitTest123","unittest123")
            self.assertEqual(IsValid,False);

if __name__ == '__main__':
    unittest.main()
