import pygtk
pygtk.require('2.0')
import gtk

class assignment1:
    def __init__(self):
    #	setting the window with the title "Hello World!"
        window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Hello World!")

    #	setting the size of window
        window.set_default_size(30,60)

    #	setting the features
        window.set_decorated(True)
        window.set_deletable(True)

    #	Creating a box in the window which would hold the button and the text box
        box=gtk.VBox(False, 10)
        box.show()

    #	Setting the spacing of the objects in the box
        box.set_spacing(10)

    #	Creating a text buffer for the text box
        buf=gtk.TextBuffer()
        buf.set_text("Hello \nWorld!\n")

    #	Creating a text box
        txt=gtk.TextView(buf)

    #	Setting the cursor in the text box    
        txt.set_cursor_visible(True)
        txt.show()

    #	Adding the text box to the box in the window
        box.pack_start(txt, True, False, 10)

    
    #	Creating the button with the label "Press Me!"
        btn=gtk.Button(label="Press Me!")
        btn.show()

    #	Adding the button to the box in the window
        box.pack_start(btn, True, False, 10)

    #	Adding the box to the window
        window.add(box)
        window.show()

def main():
    gtk.main()
    return 0
	
assignment1()
main()
        
