import Tkinter

#Create an instance top of Class Tkinter which create main window.
top = Tkinter.Tk() 

#Create a TextBox in main window by calling Entry() function
E1 = Tkinter.Entry(top)

E1.pack()

#Create a Button in main window with text "Button" by calling Button() function
B = Tkinter.Button(top, text ="Button")
B.pack()

#Event loop that waits for an event to occur and handle it accordingly.
top.mainloop()
