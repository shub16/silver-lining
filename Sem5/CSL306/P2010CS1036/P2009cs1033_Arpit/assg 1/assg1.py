import Tkinter
import ScrolledText
from Tkinter import *

root =Tk()
w = 200
h = 175
x = 60
y = 120
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
txt = ScrolledText.ScrolledText(root, background = 'white', width = 30, height = 4, font = ("Arial", 10, "normal"))
txt.pack(padx=30,pady=5)
button = Button(root, text="Button",width=10,bg="white",fg="black")
button.pack(padx=70,pady=35)
root.title('arpit_p2009cs1033')
root.mainloop()
