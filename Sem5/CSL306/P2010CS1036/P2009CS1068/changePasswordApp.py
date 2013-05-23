#!/usr/bin/python 

import pygtk
pygtk.require('2.0')
import gtk
import gtk_gui as gui

def close():
	"""This function closes the window and exists from the program."""
	gtk.main_quit()

def is_alphanumeric(str):
	"""This function checks if the given string is alphanumeric."""
	
	import re
	strMatchAlnum=re.findall('[a-zA-Z0-9]', str)
	strMatchNum=re.findall('[0-9]', str)
	strMatchAlpha=re.findall('[a-zA-Z]', str)
	if len(strMatchAlnum)==len(str) and len(strMatchAlpha)>0 and len(strMatchNum)>0:
		return 1
	else:
		return 0

class changePassword:
	"""This class is the application for changing the password."""
	
	def __init__(self, username, old_password, new_password, confirm_password):
		"""Constructor."""
		self.userName=username
		self.oldPassword=old_password
		self.newPassword=new_password
		self.confirmPassword=confirm_password
		
	def checkPasswordValidity(self):
		"""This function checks the validity of the new password."""
		
		if len(self.newPassword)<=6:
			print("The Password must have more than 6 characters. Try Again!")
			return False
		
		elif is_alphanumeric(self.newPassword)==0:
			print("The Password must have atleast 1 alphabet, 1 digit and no special characters. Try Again!")
			return False
		
		elif self.newPassword!=self.confirmPassword:
			print("The passwords entered in the fields New Password and Confirm Passowrd do not match. Try Again!")
			return False
		
		else:
			return True
			
def submitData(button, userName, oldPassword, newPassword, confirmPassword):
	"""This function is called when the button in the application is pressed and creates an object of the application class and checks for the validity of the password."""
	
	uName=userName.getValue()
	oldPwd=oldPassword.getValue()
	newPwd=newPassword.getValue()
	new2Pwd=confirmPassword.getValue()
	
	obj=changePassword(uName, oldPwd, newPwd, new2Pwd)

	if obj.checkPasswordValidity():
		print("The password has been changed successfully")
		close()
		return True

	else:
		oldPassword.setValue("")
		newPassword.setValue("")
		confirmPassword.setValue("")
		return False

def createWidgets():		
	"""This function creates and return the list of widgets in the application window."""

#	All the widgets would be added to this list and this list of widgets is then returned
	lstWidgets=[]
		
	userName="Username:"
	userLabel=gui.LabelWidget("",userName)
	lstWidgets.append(userLabel.getWidget())
	
	userText=gui.TextBoxWidget("")
	lstWidgets.append(userText.getWidget())
	
	oldPwdName="Old Password:"
	oldPwdLabel=gui.LabelWidget("",oldPwdName)
	lstWidgets.append(oldPwdLabel.getWidget())
	
	oldPwdText=gui.PasswordFieldWidget("")
	lstWidgets.append(oldPwdText.getWidget())

	newPwdName="New Password:"
	newPwdLabel=gui.LabelWidget("",newPwdName)
	lstWidgets.append(newPwdLabel.getWidget())
	
	newPwdText=gui.PasswordFieldWidget("")
	lstWidgets.append(newPwdText.getWidget())
	
	new2PwdName="Retype Password:"
	new2PwdLabel=gui.LabelWidget("",new2PwdName)
	lstWidgets.append(new2PwdLabel.getWidget())
	
	new2PwdText=gui.PasswordFieldWidget("")
	lstWidgets.append(new2PwdText.getWidget())
	
	btnName="Change Password"
	btn=gui.ButtonWidget("",btnName, submitData, userText, oldPwdText, newPwdText, new2PwdText)
	lstWidgets.append(btn.getWidget())
	
	return lstWidgets
		
def main():
	"""This is the main function of the program."""

#	the parameters for the window
	title="Change Password"
	width=300
	height=200

#	create an object of the class i.e. create the window
	obj=gui.WindowLayout("", width, height)

#	create the list of widgets to be present in the window
	wgt=createWidgets()

#	place the widgets
	obj.createLayout(wgt)
	
	gtk.main()
	return 0

if __name__=="__main__":
        main()
