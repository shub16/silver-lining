#! usr/bin/python

from fltk import *
import sys


class Create_Box(Fl_Widget):

    #constructor
    def __init__(self):
        Fl_Widget.__init__(self, 0, 0, 400, 400, "Assignmetn1")
        self.createWindow()
        self.create_Textbox()
        self.create_button()
        
        self.window.end()
        self.window.show(sys.argv)

    #creates window
    def createWindow(self):
        self.window = Fl_Window(400,400)
        self.center_screen()

    #creates Text Box
    def create_Textbox(self):
        Fl_Multiline_Input(40,40,320, 280, "");

    #creates Button
    def create_button(self):
        button = Fl_Button(150, 340, 100, 40, "Button");

    #adjust window to center
    def center_screen(self):
        self.window.position((Fl.w() - self.window.w())/2, (Fl.h() - self.window.h())/2);
                
def main():
        ex = Create_Box()   
        Fl.run()
