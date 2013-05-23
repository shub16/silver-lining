from Tkinter import *
from PIL import ImageTk, Image
import re
import tryclock
import time
import ttk
import tkMessageBox

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

def CreateImage(path):
	return path


class CommonAPI:
	global master
	master = Tk()
	global frame
	frame = Frame(master)
	
	def __init__(self, Title, Length, Breadth):
        	frame.pack()
		string = str(Length)
		string = string+"x"+str(Breadth)+"+300+300"
		master.geometry(string)
		master.title(Title)
		master.configure(background='light blue')

	def CreateButton(self, xPos, yPos, Title):
		self.button = Button(master, text=Title , fg="blue")
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

	def CreateTextArea(self, xPos, yPos):
		text1 = Text()
		text1.config(width=23, height=5)
		text1.pack()
		text1.place(x=xPos,y=yPos)

 	def CreateLabel(self, xPos, yPos, Title):
		label=Label (text = Title)
		label.pack()
		label.place(x=xPos,y=yPos)
		label.configure(background='light blue')

	def CreateList(self, xPos, yPos,List):
		Lb1 = Listbox(master, width=20, height=10)
		for l in List:
			Lb1.insert(END,l)
		Lb1.pack()
		Lb1.place(x=xPos,y=yPos)
		
		

	def AddImage(self, xPos, yPos, path):
		photo = PhotoImage(file=path)
		w = Label(master, image=photo)
		w.photo = photo
		w.pack()
		w.place(x=xPos,y=yPos)

	def CreateSlider(self, xPos, yPos):
		w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
		w.pack()
		w.place(x=xPos,y=yPos)

	def CreateSpinButton(self,xPos,yPos):
		spin = Spinbox(master, from_ = 0, to = 100)
    		spin.pack()
		spin.place(x=xPos,y=yPos)

	def CreateToggleButton(self,xPos,yPos,Title):
		def toggle_text():
			if button["text"] == "Toggle me!":
				button["text"] = "Untoggle me!"
			else:
				button["text"] = "Toggle me!"
		button = Button( text="Toggle me!", width=12, command=toggle_text)
		button.pack(padx=100, pady=10)
		button.place(x=xPos,y=yPos)
	
	def CreateClock(self, xPos, yPos):
    		clock = Label(master, font=('times', 20, 'bold'), bg='grey')
    		clock.pack()
		def tick(time_old, clock):
    			time_now = time.strftime('%H:%M:%S')
			if time_now != time_old:
	        		time_old = time_now
	        		clock.config(text = time_now)
	    		clock.after(200, tick, time_old, clock)
    		tick("", clock)
		clock.place(x=xPos,y=yPos)

	
	def CreateProgressBar(self, xPos, yPos):
		progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200, mode='determinate')
		progressbar.pack(side="bottom")
		progressbar.step(40)
		progressbar.place(x=xPos,y=yPos)
	
	def CreateDialogBox(self,Text):
		tkMessageBox.showinfo("Say Hello", Text)
		
	def Show(self):
		master.mainloop()

def Main():
	app = CommonAPI("hello", 600, 600)
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
	CreateImage("smilingpython.gif")
	app.AddImage(20,300,"smilingpython.gif")
	app.CreateSlider(400,20)
	app.CreateSpinButton(400,300)
	app.CreateToggleButton(400,250,"Toggle")
	app.CreateClock(400,80)
	app.CreateProgressBar(400,360)
	app.CreateTextArea(400,150)
	List = ["Algorithm Design", "Software Engineering","Databse Design","Operating Systems"]
	app.CreateList(400,410, List)
	
	app.Show()

if __name__ == '__main__':
    Main()		
