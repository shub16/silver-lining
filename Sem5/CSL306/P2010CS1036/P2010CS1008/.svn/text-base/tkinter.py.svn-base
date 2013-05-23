import Tkinter
import ScrolledText
from Tkinter import *
COLOR = "light grey"

class example:
	def __init__(self,master):
		frame=Frame(master)
		frame.config(bg=COLOR)
		frame2=Frame(master)
		frame2.config(bg="SlateGray")
		frame3=Frame(master)
		frame4=Frame(master)
		frame4.config(bg="grey")
		frame3.config(bg="SlateGray")
		frame3.pack(pady=15,fill=X)		
		frame.pack()
		frame2.pack(pady=15)
		frame4.pack(pady=20)
		
		Label(frame,text='Select anything from the given options:',fg="black",font=("Arial",13),borderwidth = 1, relief = SUNKEN).pack(pady=10)
		w = Button (frame, width =5,height=1,  text = "pyqt", fg="black", command=self.other)
		w.pack(padx=17,pady=20,side=LEFT)
		i = Button (frame, width =5,height=1 , text = "tkinter", fg="black", command=self.mera)
		i.pack(padx=17,pady=20,side=LEFT)
		j = Button (frame, width =5,height=1,  text = "quit", fg="black",    command=frame.quit)
		j.pack(padx=17,pady=20,side=LEFT)
 	        v = IntVar()
		Label(frame2,text='Select any radiobutton:',fg="black",font=("Arial",13),borderwidth = 1, relief = SUNKEN).pack(pady=15)
	        Radiobutton(frame2, text="Radiobutton1", variable=v, value=1, fg="black",width = 10, height =1).pack(side=LEFT, padx=10,pady=20,anchor="w") 
	        Radiobutton(frame2, text="Radiobutton2", variable=v, value=2, fg="black",width = 10, height =1).pack(side=LEFT,padx=10,pady=20, anchor="w")
	        CheckVar1 = IntVar()
	        CheckVar2 = IntVar()
		Label(frame3,text='Select any check button:',fg="black",font=("Arial",13),borderwidth = 1, relief = SUNKEN).pack(side=LEFT,pady=10)
		C1 = Checkbutton(frame3, text = "check2", variable = CheckVar1,onvalue = 1, offvalue = 0, height=1, width = 10)
		C2 = Checkbutton(frame3, text = "check1", variable = CheckVar2, onvalue = 1, offvalue = 0, height=1,width =10)
		C1.pack(padx=5,pady=5,side=BOTTOM)
		C2.pack(padx=5,pady=5,side=BOTTOM)
		Label(frame4,text='Here is the list of names of students:',fg="black",font=("Arial",13),borderwidth = 1, relief = SUNKEN).pack(side=TOP,pady=12)
		scrollbar=Scrollbar(frame4)
		scrollbar.pack(side=RIGHT, fill=Y)		
		listbox = Listbox(frame4,height=4,width=35)
		listbox.pack()
		
		for item in ["Abhisaar", "Jag Ustit", "Kshitij", "Gurpreet","Harmandeep","Anubhav","Aditya","Akshat"]:
    			listbox.insert(END, item)
			listbox.config(yscrollcommand=scrollbar.set)
			scrollbar.config(command=listbox.yview)

	
	def other(self):	
		import textAndButton
	def mera(self):

		COLOR = "grey"
		root=Tk()
		root.config(bg=COLOR)
		w = 300
		h = 250
		x = 60
		y = 150
		root.geometry("%dx%d+%d+%d" % (w, h, x, y))
		root.title('Pytinker')
		button = Button(root, text="Button",width=14, bg="red", fg="blue")
		button.pack(padx=70,pady=35)
		Label(root,text='Enter your text:').pack(pady=5)
		txt = ScrolledText.ScrolledText(root, background = 'white', width = 30, height = 4, font = ("Arial", 10, "normal"))
		txt.pack(padx=30,pady=5)

def main():
	root=Tk()
	
	root.config(bg=COLOR)	
	w = 400
	h = 510
	x = 600
	y = 100
	root.geometry("%dx%d+%d+%d" % (w, h, x, y))
	root.title('p2010cs008')
	yup=example(root)
	root.mainloop()
if  __name__=='__main__':
	main()
