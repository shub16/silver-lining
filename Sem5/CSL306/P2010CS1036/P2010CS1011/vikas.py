from Tkinter import *

vikas = Tk()
#to add the widget.It will make the main window.
 
frame = Frame(vikas)
#to add the frame in the  window

frame.pack(side=TOP)
#to display the frame at the top of the window

s = Entry(frame, bd =6)
#to add the text field in the window and bd is for background 

s.pack()
#to display the text field entry

b=Button(frame,text="BUTTON",width=7,font="Times 20 bold")
#to add the button in the window named "BUTTON" with width 7 and fonts bold of type "Times"

b.pack(side=TOP)
#To display the button

vikas.wm_title("VIKAS")
#Sets the tittle of the window "VIKAS"

vikas.mainloop()
# to execute the main loop and enter the main event loop to take action against each event triggered.


