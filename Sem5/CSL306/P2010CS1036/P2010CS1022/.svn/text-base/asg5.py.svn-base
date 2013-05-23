from Tkinter import *
import re

def emptyField(Values):
	for value in Values:
		if not value:
			print "Enter all the fields"
			return
		else:
			continue
	Validate(Values[2], Values[3])

def Validate(pass1,pass2):
	if not pass1 or not pass2:
		print "Fields are Empty"
	elif len(pass1)<6:
		print "length of password should be greater than 6"
	elif pass1 != pass2:
		print "Passwords Do not Match"
	elif ((re.search("[A-Za-z]+", pass1) is None) or (re.search("[0-9]+", pass1) is None)) or not(str(pass1).isalnum()):
		print "Passwords should contain both alpha-numeric characters"
	else:
		print "Password changed successfully"
		frame.quit()

class CommonAPI:
	global master
	master = Tk()
	global frame
	frame = Frame(master, bg="blue")
	
	
	def __init__(self, Title, Length, Breadth):
        	frame.pack()
		string = str(Length)
		string = string+"x"+str(Breadth)+"+300+300"
		master.geometry(string)
		master.title(Title)
		master.configure(background='light blue')

	def CreateButton(self, xPos, yPos, Title):
		self.button = Button(master, text=Title , fg="black")
		self.button.pack()
		self.button.place(x=xPos,y=yPos)
		return self.button

	def GetValue(self, event, TextBoxes):
		Values = []
		for item in TextBoxes:
			Values.append(item.get())
		emptyField(Values)
	
	def CreateTextBox(self, xPos, yPos, passwd=False):
		
		if passwd == False:
			entry=Entry(master, width=20)
		else:
			entry=Entry(master, width=20, show = "*")		
		entry.pack()
		entry.place(x=xPos,y=yPos)
		return entry

	def CreateCheckBox(self, xPos, yPos, Title):
		CheckVar1 = IntVar()
		C1 = Checkbutton(master, text = Title , variable = CheckVar1, onvalue = 1, offvalue = 0, width = 8)
		C1.pack()
		C1.place(x=xPos,y=yPos)
	
	def CreateRadioButton(self, xPos, yPos, Title):
		var = IntVar()
		R1 = Radiobutton(master, text= Title , variable=var, value=1 )
		R1.pack()
		R1.place(x=xPos,y=yPos)

 	def CreateLabel(self, xPos, yPos, Title):
		label=Label (text = Title)
		label.configure(background='light blue')
		label.pack()
		label.place(x=xPos,y=yPos)

	def CreateList(self, xPos, yPos,List):
		Lb1 = Listbox(master)
		for l in List:
			Lb1.insert(END,l)
		Lb1.pack()
		Lb1.place(x=xPos,y=yPos)
		
	def Show(self):
		master.mainloop()
		
def Main():
	app = CommonAPI("hello", 350, 300)
	app.CreateLabel(20,20,"ENTER USERNAME:")
	T1 = app.CreateTextBox(20,40)
    	app.CreateLabel(20,80,"ENTER OLD PASSWORD:")
	T2 = app.CreateTextBox(20,100, 'True')
    	app.CreateLabel(20,140,"ENTER NEW PASSWORD:")
	T3 = app.CreateTextBox(20,160, 'True')
    	app.CreateLabel(20,200,"RE-ENTER NEW PASSWORD:")
	T4 = app.CreateTextBox(20,220, 'True')
	button = app.CreateButton(200, 250, "Submit")
    	button.bind("<ButtonPress-1>",lambda event, arg=[T1,T2,T3,T4] : app.GetValue(event, arg))
	app.Show()
if __name__ == '__main__':
    Main()

