import unit4
from Tkinter import *
import re

def isAlphaNumeric(str1):
	str1_alnum=re.findall('[a-zA-Z0-9]', str1)
	str1_matchNum=re.findall('[0-9]', str1)
	str1_matchAlpha=re.findall('[a-zA-Z]', str1)
	if len(str1_alnum)==len(str1) and len(str1_matchAlpha)>0 and len(str1_matchNum)>0:
		return True
	else:
		return False

class changePassword():
	def __init__(self,oldPassword, NewPassword, confirmBox):
		self.old_pwd=oldPassword
		self.new_pwd=NewPassword
		self.confirm_pwd=confirmBox

	def Check_valid(self):
		if len(self.new_pwd)<=6:
			print("Password can not have less than 6 or equal to characters")
			print("Re Enter the newpassword")
			return False

		if isAlphaNumeric(self.new_pwd)==0:
			print("Password must have minimum 1 alphabet,1 digit and no special characters")
			print("Re Enter the newpassword")
			return False

		if self.new_pwd!=self.confirm_pwd:
			print("Password confirmation failed")
			print("Re Enter the newpassword")
			return False
		else:
			return True

class onclick():

	def __init__(self,oldPassword, NewPassword, confirmBox):
		self.oldPassword=oldPassword
		self.NewPassword=NewPassword
		self.confirmBox=confirmBox
		self.old_pwd=oldPassword
		self.new_pwd=NewPassword
		self.confirm_pwd=confirmBox

	def on_click(self):
		print 'new='	,self.new_pwd.get_text()
		print 'confirmation='	,self.confirm_pwd.get_text()
		change_pwd=changePassword(self.old_pwd.get_text(),self.new_pwd.get_text(), self.confirm_pwd.get_text())

		if change_pwd.Check_valid():
			print("Password successfully changed")
			return True

		else:
			self.oldPassword.set_text("")
			self.NewPassword.set_text("")
			self.confirmBox.set_text("")
			return False


if __name__=='__main__':
	win=unit4.Windows('None',300,300,500,200)
	win.show_window(None)
	v=unit4.Valignment(win)

	lb1=unit4.Statictext(win)
	lb1.set_text("User Name")
	v.add(lb1,0,0,1)
	lb2=unit4.Statictext(win)
	lb2.set_text("Old password")
	v.add(lb2,1,0,1)
	lb3=unit4.Statictext(win)
	lb3.set_text("New password")
	v.add(lb3,2,0,1)
	lb4=unit4.Statictext(win)
	lb4.set_text("confirm New password")
	v.add(lb4,3,0,1)

	box=unit4.SingleTextBox(win,1)
	v.add(box,0,1,1)
	box1=unit4.SingleTextBox(win,0)
	v.add(box1,1,1,1)
	box2=unit4.SingleTextBox(win,0)
	v.add(box2,2,1,1)
	box3=unit4.SingleTextBox(win,0)
	v.add(box3,3,1,1)
	click=onclick(box1,box2,box3)

	but=unit4.button(win,'Login',click.on_click)
	v.add(but,4,0,1)
mainloop()
