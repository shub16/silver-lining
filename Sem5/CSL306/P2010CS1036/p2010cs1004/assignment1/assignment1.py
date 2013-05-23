#import Tkinter library
from Tkinter import *



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

#button to call a defined function
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=RIGHT)

#FUNCTION TO PRINT in the console
    def say_hi(self):
        print "hi there, everyone!"

#to create GUI application main window
root = Tk()
app = App(root)


#to enter into Tkinter event loop
root.mainloop()
