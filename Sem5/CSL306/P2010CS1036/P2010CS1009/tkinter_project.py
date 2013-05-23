from Tkinter import *
import tkMessageBox

def other():
	import qt_order
	qt_order.main()

class App:

    def __init__(self, master):
    
        frame = Frame(master, bg="red")
        frame.pack()
        
	self.w = Label (frame,text='Enter text below',fg = "blue")    .pack( padx=12, pady=12, side=TOP)
	
	self.e=Entry(frame, width=15)	
	self.e.pack(  padx=17, pady=10,side=TOP)
	self.e.focus_set() 
	
	self.button    = Button(frame,   text="OK",      fg="red",       command= self.btn)           .pack( padx = 4, pady = 4 , side=TOP) 
     	self.hi_there = Button(frame,   text="PyQT",  fg = "purple", command=  other  )		    .pack( padx = 17, pady = 10, side=BOTTOM)
    
    def btn(self):
        tkMessageBox.showinfo( title = 'Textfield', message = "entryfield e  contains:\n " + self.e.get())

class Button_class:

	def __init__(self, master):

		master.config(bg="orange")

    		self.label1 = Label (text='Your hobbies')                .pack(side=LEFT,padx=10,pady=10)
		

		self.CheckVar1 = IntVar()
		self.CheckVar2 = IntVar()
		self.CheckVar3 = IntVar()
	
		self.C1 = Checkbutton(master, text = "reading", variable = self.CheckVar1)  		 .pack(side = LEFT)
		self.C2 = Checkbutton(master, text = "blogging", variable = self.CheckVar2)  		 .pack(side = LEFT)
		self.C3 = Checkbutton(master, text = "cricket", variable = self.CheckVar3)    		 .pack(side = LEFT)

		self.label2 = Label (text='Select gender').pack(side=TOP,padx=10,pady=10)
		
		self.var = StringVar()

		self.R1 = Radiobutton(root, text="Male", variable=self.var, value="Male",command=self.sel)
		self.R1.pack( anchor = W )

		self.R2 = Radiobutton(root, text="Female", variable=self.var, value="Female", command=self.sel)
		self.R2.pack( anchor = W )

		self.label3 = Label (master,text="You havent selected any option",fg="red")						###none type object has no attribute....err	
		self.label3.pack()

		self.label4 = Label (master,text="Select the name of your best players:")								.pack(side =  TOP,pady=20)
		
		self.Lb1 = Listbox(master)
		
		for item in ["Sachin", "Yuvraj", "Sehwag"]:
			self.Lb1.insert(END, item)

		self.Lb1.pack(side = TOP,padx= 20 ,pady=5)
		
		self.button = Button(master, text="Select", bg="blue",fg="yellow" ,command=self.list_box_select)          .pack(padx = 3,pady=4,side=LEFT)
		self.button = Button(master,   text="QUIT",  bg="blue",fg="yellow" ,    command=exit)                          .pack( padx = 30, pady = 40 , side=LEFT)

	def sel(self):
		selection = "You selected the option " + str(self.var.get())
   		self.label3.config(text = selection,fg="dark green")
   		
	def list_box_select(self):
		a=self.Lb1.curselection()
		var="You choosed \n"+"Interests: "
		

		if self.CheckVar1.get()==1 and self.CheckVar2.get()==1 and self.CheckVar3.get()==1:
			var=var+"All the 3 \n"

		elif self.CheckVar1.get()==1 and self.CheckVar2.get()==1:
			var=var+"reading and blogging \n"
		
		elif self.CheckVar1.get()==1 and self.CheckVar3.get()==1:
			var=var+"reading and cricket \n"

		elif self.CheckVar2.get()==1 and self.CheckVar3.get()==1:
			var=var+"blogging and cricket \n"

		elif self.CheckVar1.get()==1:
			var=var+"reading\n"		

		elif self.CheckVar2.get()==1:
			var=var+"blogging\n"

		elif self.CheckVar3.get()==1:
			var=var+"cricket\n"

		else:
			var=var+"None\n"

		var=var+"Gender: "+str(self.var.get())+"\n"
		var=var+"Favourite Player: "

		if(len(a)==0):
			var=var+"None selected: "
		
		elif a[0]=='0':			
			var=var+"Sachin"
		 	tkMessageBox.showinfo("Choice", var)
		elif a[0]=='1':			
			var=var+"Yuvraj"
			tkMessageBox.showinfo("Choice", var)
		elif a[0]=='2':
			var=var+"Sehwag"   
			tkMessageBox.showinfo("Choice", var)						
root = Tk()
root.title('p2010CS1009')
root.geometry("640x640")
app = App(root)
button=Button_class(root)
root.mainloop()
