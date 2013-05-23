import Tkinter #this will import toolkit files from python
from Tkinter import *
root =Tk()
root.title('tkinter GUI') #the title of the new window is created by this
Label (text='Enter your name').pack(side=TOP,padx=10,pady=10) #this create the some lable inside that window
Entry(root, width=30).pack(side=TOP,padx=10,pady=10) # this create the box for writing text
Button(root, text='ENTER').pack(side= LEFT) # this create button
Button(root, text='close').pack(side= RIGHT) # this create button
root.geometry('+%d+%d' % (435,500))
root.mainloop()
