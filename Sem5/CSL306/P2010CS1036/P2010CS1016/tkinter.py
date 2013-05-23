import Tkinter
import ScrolledText
from Tkinter import *
COLOR = "grey"
root=Tk()
root.config(bg=COLOR)
w = 300
h = 250
x = 60
y = 150
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
root.title('Pytinker')
button = Button(root, text="Button",width=14, bg="red", fg="blue")
button.pack(padx=70,pady=35)
Label(root,text='Enter your text:').pack(pady=5)
txt = ScrolledText.ScrolledText(root, background = 'white', width = 30, height = 4, font = ("Arial", 10, "normal"))
txt.pack(padx=30,pady=5)
root.mainloop()
