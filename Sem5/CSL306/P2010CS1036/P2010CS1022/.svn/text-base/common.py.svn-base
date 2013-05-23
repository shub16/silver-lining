from Tkinter import *



class CommonAPI:


	global master
	master = Tk()
	global frame
	frame = Frame(master, bg="white")
	
	def __init__(self, Title, Length, Breadth):
        	frame.pack()
		string = str(Length)
		string = string+"x"+str(Breadth)+"+300+300"
		master.geometry(string)
		master.title(Title)

	def CreateButton(self, xPos, yPos, Title):
		self.button = Button(master, text=Title , fg="red")
        	self.button.pack()
		self.button.place(x=xPos,y=yPos)
	
	def CreateTextBox(self, xPos, yPos):
		self.entry=Entry(master, width=20)
		self.entry.pack()
		self.entry.place(x=xPos,y=yPos)
	
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

	def CreateList(self, xPos, yPos,List):
		Lb1 = Listbox(master)
		for l in List:
			Lb1.insert(END,l)
		Lb1.pack()
		Lb1.place(x=xPos,y=yPos)


	def Show(self):
		master.mainloop()

def Main():
	
	app = CommonAPI("hello", 300, 250)
	app.CreateTextBox(20,20)
	app.CreateButton(200, 150, "hey")
	app.CreateCheckBox(180, 60, "Check")
	app.CreateRadioButton(190, 80, "Radio")
	List = ["Algorithm Design", "Software Engineering","Databse Design","Operating Systems"]
	app.CreateList(20,60, List)
	app.Show()
if __name__ == '__main__':
    Main()
