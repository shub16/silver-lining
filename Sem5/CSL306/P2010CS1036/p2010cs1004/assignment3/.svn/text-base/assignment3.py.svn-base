#import Tkinter library
from Tkinter import *
import tkMessageBox

#function to use class of secondary file
def open_pyqt_tab():
	import lab1
	lab1.main()

#class to add widgets to main window
class App:
#constructor for App class
    def __init__(self, master):
#create frame
        frame = Frame(master)
        frame.pack()
#create a Label to show some text
        self.w = Label (frame,text='Enter some text')
	self.w.pack(side=TOP,padx=10,pady=10)

#entry field to take input from user 
        self.e=Entry(frame, width=10)
	self.e.pack(side=TOP,padx=10,pady=10)

#button to close the frame	
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
	self.hi_there = Button(frame, text="PyQT TAB", command=open_pyqt_tab)
        self.hi_there.pack(side=RIGHT)
#button to call a defined function
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=RIGHT)
#FUNCTION TO PRINT in the console
    def say_hi(self):
        print "hi there, everyone!"
        
class Button_class:
	def __init__(self, master):
		self.label1 = Label (text='Your interests')
		self.label1.pack(side=TOP,padx=10,pady=10)
		self.CheckVar1 = IntVar()
		self.CheckVar2 = IntVar()
		self.C1 = Checkbutton(master, text = "Music", variable = self.CheckVar1)
		self.C2 = Checkbutton(master, text = "Video", variable = self.CheckVar2)
		self.C1.pack()
		self.C2.pack()		

		self.label2 = Label (text='Select Gender')
		self.label2.pack(side=TOP,padx=10,pady=10)
		self.var = StringVar()
		self.R1 = Radiobutton(root, text="Male", variable=self.var, value="Male",
                  command=self.sel)
		self.R1.pack( anchor = W )
		self.R2 = Radiobutton(root, text="Female", variable=self.var, value="Female",
                  command=self.sel)
		self.R2.pack( anchor = W )
		self.label3 = Label (master,text="You havent selected any option",fg="red")
		self.label3.pack()
		self.label4 = Label (master,text="Select your preffered language:")
		self.label4.pack()
		self.Lb1 = Listbox(master)
		self.Lb1.insert(1, "C++")
		self.Lb1.insert(2, "Python")
		self.Lb1.insert(3, "Java")
		self.Lb1.pack()
		self.button = Button(master, text="Select", fg="red", command=self.list_box_select)
        	self.button.pack(side=LEFT)
	def sel(self):
		selection = "You selected the option " + str(self.var.get())
   		self.label3.config(text = selection,fg="blue")
	def list_box_select(self):
		a=self.Lb1.curselection()
		var="You choosed \n"+"Interests: "
		if self.CheckVar1.get()==1 and self.CheckVar2.get()==1:
			var=var+"Music and Video Both\n"
		elif self.CheckVar1.get()==1:
			var=var+"Music\n"
		elif self.CheckVar2.get()==1:
			var=var+"Video\n"
		else:
			var=var+"None\n"
		var=var+"Gender: "+str(self.var.get())+"\n"
		var=var+"Language: "
		if(len(a)==0):
			var=var+"None selected: "		
		elif a[0]=='0':
			var=var+"C++"
		elif a[0]=='1':
			var=var+"Python"
		elif a[0]=='2':
			var=var+"Java"
   		tkMessageBox.showinfo("Choice", var)
root = Tk()
app = App(root)
button=Button_class(root)
#to enter into Tkinter event loop
root.mainloop()
