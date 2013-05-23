from P2010CS1067_WxPython import *
import re
def isAlphaNumeric(str1):											#this checks a string whether alphanumeric or not 
	str1_alnum=re.findall('[a-zA-Z0-9]', str1)
	str1_matchNum=re.findall('[0-9]', str1)
	str1_matchAlpha=re.findall('[a-zA-Z]', str1)
	if len(str1_alnum)==len(str1) and len(str1_matchAlpha)>0 and len(str1_matchNum)>0:
		return True
	else:
		return False



class Pass:
	def __init__(self,usr,old,new,repeat):
		self.usr=usr
		self.new=new
		self.old=old
		self.repeat=repeat
		
	def valid(self,*args):
		#if isinstance(new.get_text(), str) and isinstance(repeat.get_text(), str):	
		if(len(self.new)<=6):
			print 'Password too short. Mininmum 7 characters required:'
			return False
			
		else:	
			if(not isAlphaNumeric(self.new)):
				print 'Password is not alphanumeric:'
				return False
				
			else:
				if(self.new!=self.repeat):
					print 
					print 'Passwords do not match:'
					return False
				else:
					
					print 'Congrats!,password changed'
					return True
	


if __name__ == '__main__':
	app =App()
	frame= Windows('What\'s up buddy!!!',250,250,300,300)
	frame.move_to_centre()
	
	usr=SingleTextBox(frame,0)
	user=Statictext(frame,"")
	user.set_text("User Name")
	
	old=SingleTextBox(frame,0)
	older=Statictext(frame,"")
	older.set_text("Old Password")
	
	new=SingleTextBox(frame,0)
	newer=Statictext(frame,"")
	newer.set_text("New Password")
	
	repeat=SingleTextBox(frame,0)
	rep=Statictext(frame,"")
	rep.set_text("Confirm New Password")
	
	
	
	but=button(frame,'Submit')
	
	but1=button(frame,'Close')
	
	def closin(event):
		frame.close_window()
	
	but1.bind(closin)
	
	def validity(event):
		u=usr.get_text()
		o=old.get_text()
		n=new.get_text()
		r=repeat.get_text()
		check=Pass(u,o,n,r)
		
		if(check.valid()):
			
			frame.close_window()
			
		else:
			new.set_text("")
			repeat.set_text("")
	
	
	but.bind(validity)
	
	
	
	v=Alignment(frame)	
	v.add(user,1,1,1)
	v.add(usr,2,1,2)
	v.add(older,3,1,1)
	v.add(old,4,1,2)
	v.add(newer,5,1,1)
	v.add(new,6,1,2)
	v.add(rep,7,1,1)
	v.add(repeat,8,1,2)
	v.add(but,9,1,1)
	v.add(but1,9,2,3)
	frame.show_window(v)
	
	app.loop()
	
	
