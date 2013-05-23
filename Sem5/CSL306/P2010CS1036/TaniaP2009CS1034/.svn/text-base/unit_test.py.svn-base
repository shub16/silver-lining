import unittest
import gen as mod


class TestValidate(unittest.TestCase):

    def testOne(self):
        self.failUnless(mod.validate("abc345def6","abc345def6"))    #testing a valid string

    def testTwo(self):
        self.failUnless(mod.validate("abcdef6","abcdef6"))      #testing a valid string

    def testThree(self):
        self.failIf(mod.validate("abcdef45","ghijkl45"))        #testing strings that do not match       

    def testFour(self):
        self.failIf(mod.validate("abc34","abc34"))      #testing strings of length 6 or less        

    def testFive(self):
        self.failIf(mod.validate("abcdefg","abcdefg"))  #testing strings consisting of only alphabets               

    def testSix(self):
        self.failIf(mod.validate("1234567","1234567"))  #testing strings consisting of only numerics        

    def testSeven(self):
        self.failIf(mod.validate("abc","abc"))      #testing strings smaller in length and having only alphabets       

    def testEight(self):
        self.failIf(mod.validate("123","123"))      #testing strings smaller in length and having only numbers        

    def testNine(self):
        self.failIf(mod.validate("ab_cde34*","ab_cde34*"))      #testing strings containing special characters with alpha-numeric fields

    def testTen(self):
        self.failIf(mod.validate("abcde34","abcde3*"))      #testing a valid string with a invalid string(do not match)

    def testEleven(self):
        self.failIf(mod.validate("",""))                    #testing empty strings

    def testTwelve(self):
        self.failIf(mod.validate("**_&&","**_&&"))          #testing strings consisting of only special characters


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise
