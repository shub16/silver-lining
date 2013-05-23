import Tkinter
import ScrolledText
from Tkinter import *
COLOR="blue"
root = Tk()
root.config(bg=COLOR)
w = 300
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
