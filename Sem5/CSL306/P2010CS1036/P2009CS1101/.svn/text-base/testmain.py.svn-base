import main
import unittest

class TestMainFunction(unittest.TestCase):

    # test for success
    def testValidate(self):
	self.assertEqual(main.validate('qwerty12', 'qwerty12'), 0)

    # test for failure when password and re-entered password not equal
    def testValidateFail1(self):
	with self.assertRaises(ValueError):
	    main.validate('qwerty', 'qwert')

    # test for failure when paswword contains all alphabets
    def testValidateFail2(self):
	with self.assertRaises(TypeError):
	    main.validate('qwerty', 'qwerty')

    # test for failure when password contains all digits
    def testValidateFail3(self):
	with self.assertRaises(TypeError):
	    main.validate('123456', '123456')

    # test for failure when password length is less than equal to 6
    def testValidateFail4(self):
	with self.assertRaises(Exception):
	    main.validate('12qw', '12qw')

    # test for failure when one field is empty
    def testValidateFail5(self):
	with self.assertRaises(ValueError):
	    main.validate('qwerty', '')

    # test for failure when both fields are empty
    def testValidateFail6(self):
	with self.assertRaises(TypeError):
	    main.validate('', '')

    # test for failure when password has non-alphanumeric characters
    def testValidateFail7(self):
	with self.assertRaises(TypeError):
	    main.validate('qwerty12_$', 'qwerty12_$')

    # test for failure when the two passwords have different cases
    def testValidateFail8(self):
	with self.assertRaises(ValueError):
	    main.validate('qwerty12', 'QWERTY12')

if __name__ == '__main__':
    unittest.main()
