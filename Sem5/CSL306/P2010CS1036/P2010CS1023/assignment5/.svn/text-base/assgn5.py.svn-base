from anygui import anywx as g
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
		
	def valid(self,event):
		#if isinstance(new.get_text(), str) and isinstance(repeat.get_text(), str):	
		if(len(self.new.get_text())<=6):
			print 'Password too short. Mininmum 7 characters required:'
			return False
	
		else:	
			if(not isAlphaNumeric(self.new.get_text())):
				print 'Password is not alphanumeric:'
				return False
			
			else:
				if(self.new.get_text()!=self.repeat.get_text()):
					print 
					print 'Passwords do not match:'
					return False
				else:
					print 'Congrats!'
					return True
					
if __name__=='__main__':
	f=g.frame(1,"password checker",510,300)
	
	
	user=g.text_field()
	user.pos=(20,20)
	user.size=(170,30)
	user.label="user name"
	f.append(user)
	
	old=g.text_field2()
	old.pos=(20,60)
	old.size=(170,30)
	old.label="old password"
	f.append(old)
	
	new=g.text_field2()
	new.pos=(20,100)
	new.size=(170,30)
	new.label="new password"
	f.append(new)
	
	confirm=g.text_field2()
	confirm.pos=(20,140)
	confirm.size=(170,30)
	confirm.label="confirm new password"
	f.append(confirm)
	
	check=Pass(user,old,new,confirm)
	
	but=g.button()
	but.pos=(220,100)
	but.label="submit"
	
	#sl=g.Slider(0,10,20,100,50,180)
	#sp=g.SpinBox(0,80,300,160,50,50)
	but.onclick(check.valid)
	f.append(but)
	#f.append(sl)
	#f.append(sp)
	f.show()
	
	
	
	
	
	  
