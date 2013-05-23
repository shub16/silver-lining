import Tkinter
import ScrolledText
from Tkinter import *
COLOR="blue"
class Gui:
	def __init__(self, master):
		frame = Frame(master)
		frame.config(bg=COLOR,borderwidth=3,relief=SUNKEN)
		frame2=Frame(master)
		frame2.config(borderwidth=3,relief=SUNKEN)
		frame3= Frame(master)
		frame3.config(borderwidth=3,relief=SUNKEN)
		frame2.pack(fill=X)
		frame.pack(fill=X)
		frame3.pack(fill=X)
		frame4=Frame(master)
		frame4.config(borderwidth=3,relief=SUNKEN)
		frame4.pack(fill=X)

		v = IntVar()
		Label(frame2,text="Please Select One",font=("Helvetica", 16),fg=COLOR).pack(side=LEFT,padx=10,pady=13)
      	  	Radiobutton(frame2, text="Software", variable=v, value=1,fg=COLOR).pack(side=LEFT, anchor="w" )
      	  	Radiobutton(frame2, text="Hardware", variable=v, value=2,fg=COLOR).pack(side=LEFT, anchor="w")
        

		Label(frame,text="Choose the GUI Environment ",bg=COLOR,font=("Helvetica", 16),fg="white").pack(side=TOP,padx=5,pady=5)
		l = Button (frame, width =10,  text = "Py-QT",    command=self.dooja)
		m = Button (frame, width =10, text = "Tkinter", command=self.apna)
		n = Button (frame, width =10,  text = "Quit",    command=frame.quit)
		l.pack(side=TOP,padx=5,pady=5)
		m.pack(side=TOP, padx=5,pady=5)
		n.pack(side=TOP, padx=5,pady=5)	
			
		CheckVar1 = IntVar()
		CheckVar2 = IntVar()
		Label(frame3,text="Tick the Required",font=("Helvetica", 16),fg=COLOR).pack(side=LEFT,padx=5,pady=10)
		C1 = Checkbutton(frame3, text = "Music", variable = CheckVar1, \
                onvalue = 1, offvalue = 0, height=1, \
                width = 10,fg=COLOR)
		C2 = Checkbutton(frame3, text = "Video", variable = CheckVar2, \
                onvalue = 1, offvalue = 0, height=1, \
                width = 10,fg=COLOR)
		C1.pack(side=BOTTOM,padx=10,pady=3)
		C2.pack(side=BOTTOM,padx=10,pady=3)

		Label(frame4,text="Scroll The List",font=("Helvetica", 16),fg=COLOR).pack(fill=X,side=TOP,padx=5)
		scrollbar=Scrollbar(frame4)
		scrollbar.pack(side=RIGHT, fill=Y)
		listbox = Listbox(frame4,height=6,width=35)
		listbox.pack(fill=X)
		for item in ["one", "two", "three", "four","five","six","seven","eight","nine","ten"]:
    			listbox.insert(END, item)
			listbox.config(yscrollcommand=scrollbar.set)
			scrollbar.config(command=listbox.yview)

			
	def dooja(self):
		import textAndButton_2
	def apna(self):
		COLOR="blue"
		root =Tk()
		root.config(bg=COLOR)
		w = 400
		h = 200
		x = 60
		y = 150
		root.geometry("%dx%d+%d+%d" % (w, h, x, y))
		root.title('p2010cs1015')
		txt = ScrolledText.ScrolledText(root, background = 'white', width = 30, height = 5, font = ("Times New Roman", 10, "normal"))
		txt.pack(padx=30,pady=30)
		button = Button(root, text="Click Here",width=10)
		button.pack(padx=70,pady=1)
		root.mainloop()

def main():
	root =Tk()
	root.config(bg=COLOR)
	w = 400	
	h = 500
	x = 60
	y = 150
	root.geometry("%dx%d+%d+%d" % (w, h, x, y))
	root.title('p2010cs1015')
	hell=Gui(root)
	root.mainloop()

if __name__ == '__main__':
    main()  
