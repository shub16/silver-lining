from Tkinter import Tk, BOTH, Entry, TOP, Frame, Button, BOTTOM

# This class inherits from Frame container widget
class ButtonAndTextBox(Frame):
    
    #Constructor
    def __init__(self, parent):
        
        # Constructor of inherited class called, background specified
        Frame.__init__(self, parent, background="grey")
        
        self.parent = parent
        self.initUI()
    
    # Creation of user interface
    def initUI(self):
      
        #Title of the frame
        self.parent.title("Button and TextBox GUI")
        
        # the frame container widget takes whole user space of the root window
        self.pack(fill=BOTH, expand=1)
        
        #The Text Box widget is created with padding and positioning at TOP of frame
        Entry(self, width=10).pack(side=TOP,padx=10,pady=10)
        
        #The Button widget is created with padding and positioning at bottom
        Button(self, text="Button").pack(side=BOTTOM,padx=10,pady=10)

# Main function 
def main():

    # The root window is created, geometry and positioning specified  
    root = Tk()
    root.geometry("275x150+300+300")
    
    # Instance of application class created
    ButtonAndTextBox(root)
    
    # Event handling in the Main Loop of our Application Window
    root.mainloop()  

if __name__ == '__main__':
    main()  