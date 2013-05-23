
choice=int(raw_input("1 for running my code\n 2 for running other`s code:"))
if choice==1:
   import Tkinter
   import ScrolledText
   from Tkinter import *

   root =Tk()

   w = 300
   h = 500
   x = 60
   y = 120

   root.geometry("%dx%d+%d+%d" % (w, h, x, y))  # dimensions of the frame

   txt = ScrolledText.ScrolledText(root, background = 'white', width = 25, height = 4, font = ("Arial", 10, "normal"))
   txt.place(x=100,y=0)
   txt.pack(padx=5,pady=5) # Text Area Definition

   button = Button(root, text="Button",width=10,bg="white",fg="black")  # Button definition
   #button.place(x=30,y=8)
   button.pack(padx=5,pady=5)

   var = IntVar()
   c = Checkbutton(root, text="CheckButton", variable=var)     # check button
   c.pack(anchor=W,padx=5,pady=5)
   
   v=IntVar()
   Radiobutton(root, text="First", variable=v, value=1).pack(anchor=W)      # 1st radio button
   Radiobutton(root, text="Second", variable=v, value=2).pack(anchor=W)      # 2nd radio button with the same variable as 1st
   
   w=Label(root,text="The List")
   w.pack(padx=5)
   
   listbox = Listbox(root)    # List box definition
   listbox.pack(padx=5,pady=5)
   for item in ["one", "two", "three", "four"]:    # elements being added to the list
      listbox.insert(END, item)
  
   root.title('arpit_p2009cs1033')
   root.mainloop()

elif choice==2:
    fil=str(raw_input("enter the filename(the file has to be placed where this file is present): "))
    __import__(fil)

else:
    print "Wrong Choice..."


   
