#import test
from Tkinter import *
import tkMessageBox

vikas = Tk()
#To add the widget.It will make the main window.
var = IntVar()

frame = Frame(vikas)
#to add the frame in the  window

frame.pack(side=TOP)
#to display the frame at the top of the window
def selected():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   
   #tkMessageBox.showinfo( "Hello Python", selection)




# function to import PyQT window from other file
def HI():
 import p2010cs1013 
 p2010cs1013.main()


# function to show TKinter window from original file
def vikas1():
 vikas=Toplevel()
 f = Entry(vikas, bd =6)
#to add the text field in the window and bd is for background
 
 f.pack()
#to display the text field entry


 D=Button(vikas,text="BUTTON",width=7,font="Times 20 bold")
#To add the button in the window named "BUTTON" with width 7 and fonts bold of type "Times"

 D.pack()
 

 R1 = Radiobutton(vikas, text="Option 1", variable=var, value=1,
                command=selected)

                  
 R1.pack( anchor = W )

 R2 = Radiobutton(vikas, text="Option 2", variable=var, value=2, command=selected)
 R2.pack( anchor = W )

 R3 = Radiobutton(vikas, text="Option 3", variable=var, value=3, command=selected)
 R3.pack( anchor = W)
 
 
 CheckVar1 = IntVar()
 CheckVar2 = IntVar()
 C1 = Checkbutton(vikas, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5,  width = 4)
 C2 = Checkbutton(vikas, text = "Video", variable = CheckVar2,  onvalue = 1, offvalue = 0, height=5,  width = 4)
 C1.pack(anchor = W)
 C2.pack(anchor = W)


 scrollbar = Scrollbar(vikas)
 scrollbar.pack( side = RIGHT, fill=Y )
 Lb1 = Listbox(vikas, yscrollcommand = scrollbar.set)
 Lb1.insert(1, "RED")
 Lb1.insert(2, "YELLOW")
 Lb1.insert(3, "GREEN")
 Lb1.insert(4, "BLUE")
 Lb1.insert(5, "PINK")
 Lb1.insert(6, "BLACK")
 Lb1.insert(7, "WHITE")
 Lb1.insert(8, "ORANGE")
 Lb1.insert(9, "PURPLE")
 Lb1.insert(10, "MAGENTA")
 Lb1.insert(11, "BROWN")
 Lb1.insert(12, "NAVY BLUE")
 Lb1.pack( side = LEFT, fill = BOTH )
 scrollbar.config( command = Lb1.yview )








#To display the button
 #vikas.mainloop()



 
b=Button(frame,text="Tkinter",width=7,font="Times 20 bold",command=vikas1)

#To add the button in the window named "Tkinter" with width 7 and fonts bold of type "Times" for displaying the """""Tkinter window"""""..

p=Button(frame,text="PYQT",width=7,font="Times 20 bold",command=HI)

#To add the button in the window named "PYQT" with width 7 and fonts bold of type "Times" for displaying the """""PYQT window"""""..

X=Button(frame,text="EXIT",width=7,font="Times 20 bold",command=exit)
#To add the button in the window named "EXIT" with width 7 and fonts bold of type "Times" for EXIT..


b.pack(side=TOP)
#To display the button

p.pack(side=TOP)
#To display the button

X.pack(side=TOP)
#To display the button

vikas.wm_title("VIKAS")
#Sets the tittle of the window "VIKAS"


 
label = Label(vikas)
label.pack()


vikas.mainloop()
# To execute the main loop and enter the main event loop to take action against each event triggered.
