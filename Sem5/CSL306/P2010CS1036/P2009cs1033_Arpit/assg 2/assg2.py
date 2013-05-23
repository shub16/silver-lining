choice=int(raw_input("1 for running my code\n 2 for running other`s code:"))
if choice==1:
   import Tkinter
   import ScrolledText
   from Tkinter import *
   root =Tk()

   w = 300
   h = 200
   x = 400
   y = 200

   root.geometry("%dx%d+%d+%d" % (w, h, x, y))
   
   txt = ScrolledText.ScrolledText(root, background = 'white', width = 30, height = 4, font = ("Arial", 10, "normal"))
   txt.pack(padx=10,pady=5)

   button = Button(root, text="Button",width=10,bg="white",fg="black")
   button.pack(padx=70,pady=35)

   root.title('arpit_p2009cs1033')
   root.mainloop()

elif choice==2:
    fil=str(raw_input("enter the filename(it should be at the same position as this program): "))
    __import__(fil)

else:
    print "Wrong Choice..."
