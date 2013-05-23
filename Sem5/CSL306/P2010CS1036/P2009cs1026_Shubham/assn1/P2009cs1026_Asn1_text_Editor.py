"""
    Fltk uses text buffer to store inputed text; using it text-editor & 
    text-display uses the text buffer to show inputed text.
    Thus, this TextEditor program display again the inputed text from text-editor
    to display-box in the same window .
"""

from fltk import *
import sys

class EchoEditor:
    
    def __init__(self):
        self.create_Window()
        self.add_Button()
        self.textbuffer = Fl_Text_Buffer()                   # Create a text buffer, this stores the actual text
        self.textbuffer.text(" write something here ")
        self.add_TextBox()
        self.add_TextDisplay()
        self.window.end()                                    # finishes creation of window 
        self.window.show()

    # Create the main window
    def create_Window(self, width = 400, height = 400, label = " pyFltk sample Application " ) :        
        self.window = Fl_Window(width, height, label)

    # Add a Button to window
    def add_Button(self, left = 150, top = 360, width = 100, height = 20 ) :
    
        label = "Close Window"
        self.button1 = Fl_Button( 150, 360, 100, 20, label )    
        self.button1.callback(self.click)                    # call "click" function when get clicked
        
    # Add a text editor, Showing the text and allows editing also        
    def add_TextBox( self, left = 50, top = 215, width = 300, height = 125 ) :
        label = "Text Input :"
        self.textedit = Fl_Text_Editor(left, top, width, height, label)
        self.textedit.buffer(self.textbuffer)                # use the buffered text to display
        
    # Add a text display, Showing the text only
    def add_TextDisplay( self, left = 50, top = 40, width = 300, height = 125 ) :
        label = "Text Output :"
        self.textdisplay = Fl_Text_Display(50, 40, 300, 125, label)
        self.textdisplay.buffer(self.textbuffer)             # use the buffered text to display
                
    # Function is called, when button1 is clicked
    def click(self, widget):
        sys.exit(0)
    
def main() :
    echo_editor = EchoEditor()                               # Create an object of our TextEditor class
    Fl.run()                                                 # Start the main FLTK loop

if __name__ == "__main__":
    main()