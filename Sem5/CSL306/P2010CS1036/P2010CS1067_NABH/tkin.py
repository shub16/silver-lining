import Tkinter 

from Tkinter import *
root =Tk()
root.title('Hello')



Label (text='Enter Username').pack(side=TOP,padx=15,pady=6)
Entry(root, width=15).pack(side=TOP,padx=15,pady=15)
Button(root, text="submit").pack(side= BOTTOM)

root.mainloop()


