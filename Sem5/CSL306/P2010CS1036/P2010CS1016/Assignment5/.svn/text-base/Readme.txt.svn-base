__________________________________________________________________________CONTENTS________________________________________________________________________

#assignment5.py
Written in a common API,this python file which brings up an interface where a user can change its password and set it to a new one.The new password and confirm password is validated for the following conditions:

	*The two copies of new passwords must match
	*Both alpha and numeric fields
	*More than 6 characters

#tkGUI.py
This is the my implementation for the common API implemented by our group.This file is imported in assignment5.py

#UnitTest.py
This unit test checks the function validate(string1 ,string2) used in assignment5.py for password validation for the following test cases ie a combination of string1 and string2:
  => test for success
	"abcd123","abcd123"-------------------------- should return true

  => test for failure when password and re-entered password not equal
	"abcdfd123","cgytgh678"---------------------- should return false 

  => test for failure when paswword length is not more than 6.
	"qwe1","qwe1"-------------------------------- should return false

  => Test for failure when password contains only alphabets
	"onlyalpha","onlyalpha"---------------------- should return false

  => test for failure when password contains only digits
	"1234567","1234567"-------------------------- should return false
	
  => test for failure when password has non-alphanumeric characters  	
	"special@234","special@234"------------------ should return false
  
  => test for failure when one field is empty
	"empty123",""-------------------------------- should return false

  => test for failure when both fields are empty
	"",""---------------------------------------- should return false

  => test for failure when the two passwords have different cases
	"case123","CASE123"-------------------------- should return false

______________________________________________________________________RUNNING THE CODE_____________________________________________________________________________

For running the actual change the password application, run the python file assignment5.py
For running the unit test suite to test the validation method , run the python file UnitTest.py

