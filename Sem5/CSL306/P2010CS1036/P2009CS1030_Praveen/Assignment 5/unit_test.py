import unittest
import Assign5_P2009CS1030 as my_app

class TestPasswordValidity(unittest.TestCase):

    def setUp(self):
        self.function = my_app.if_valid_pwd  
    def teardown(self):
        pass

# testing for success 
    def test_pwd_case1_t(self):
        self.assertTrue(self.function("P2009cs1026", "P2009cs1026").value)
    def test_pwd_case2_t(self):
        self.assertTrue(self.function("ABCde,1", "ABCde,1").value)
    def test_pwd_case3_t(self):
        self.assertTrue(self.function("123456z", "123456z").value)
    def test_pwd_case4_t(self):
        self.assertTrue(self.function("abcde1%", "abcde1%").value)
    def test_pwd_case5_t(self):
        self.assertTrue(self.function("axyz&0%", "axyz&0%").value)
        
# testing for failure 
    def test_pwd_case6_f(self):
        self.assertFalse(self.function("abcde1%", "ABCDE1%").value)
    def test_pwd_case7_f(self):
        self.assertFalse(self.function("zx123%", "zx123%").value)
    def test_pwd_case8_f(self):
        self.assertFalse(self.function("123456", "123456").value)
    def test_pwd_case9_f(self):
        self.assertFalse(self.function("abcedf%", "abcedf%").value)
    def test_pwd_case10_f(self):
        self.assertFalse(self.function("P2009c%", "P2009c").value)

# testing for sanity
    def test_pwd_case11_s(self):
        with self.assertRaises(TypeError):
            self.function(123, 123)
   
    def test_pwd_case12_s(self):
        with self.assertRaises(TypeError):
            self.function(1234567, "1234567")
            
    def test_pwd_case13_s(self):
        with self.assertRaises(TypeError):
            self.function(1234567, "xyze1256")

            
if __name__ == '__main__':
    unittest.main()