import Tkinter 
from Tkinter import *
root =Tk()
root.title('waheguru')

def qt_code():
	import textAndButton

def mine_code():

	root=Tk()
	var = IntVar()
	root.title('tkinter GUI')
	Label (root,text='Enter your name').pack(side=TOP,padx=10,pady=10)
	Entry(root, width=30).pack(side=TOP,padx=10,pady=10)
	Button(root, text='ENTER',width=10).pack(side= LEFT)
	Checkbutton(root, text="Expand", variable=var).pack(side=LEFT)
	Button(root, text='close', command=exit).pack(side= RIGHT)
	
	root.mainloop()
Checkbutton(root, text="Expand", variable=var).pack(side=TOP)
Button(root, text='QT_code', width=10, height=2, command =qt_code).pack(pady=20,side= LEFT)
Button(root, text='TK_inter', width=10, height=2, command= mine_code).pack(padx=20,pady=20,side= LEFT)	
Button(root, text='close',width=10, height=2, command =exit).pack(pady=20,side= LEFT)

root.mainloop()
