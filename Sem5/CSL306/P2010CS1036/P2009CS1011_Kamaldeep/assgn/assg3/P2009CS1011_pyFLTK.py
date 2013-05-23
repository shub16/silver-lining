#! usr/bin/python

from fltk import *
import sys

x   =    0
y   =    0
width  = 500
height = 500

class Widgets(Fl_Widget):

    #constructor
    def __init__(self):
        Fl_Widget.__init__(self, 0, 0, 700, 600, "Assignmetn1")
        
    #creates window
    def createWindow(self,x,y,widht,height,text):
        self.window = Fl_Window(x,y,widht,height,text)
        self.center_screen()

    #creates Text Box
    def create_Textbox(self, x, y, widht, height, text):
        textbox = Fl_Input(x, y, widht, height, text);
        textbox.color(FL_WHITE);

    #creats radio_button
    def round_button(self,x,y,widht,height, text):
        rbutton = Fl_Round_Button(x,y,widht,height, text);
        rbutton.type(FL_RADIO_BUTTON);
        rbutton.color(FL_WHITE);

    #creates pulldown list
    def pulldown(self,x,y,widht,height,data, text):
        choice = Fl_Choice (x,y,widht,height,text)
        choice.copy(data)
        choice.color(FL_WHITE);

    #creates toggle button
    def toggle_button(self, x, y, widht, height, text):
        cbutton1 = Fl_Check_Button(x, y, widht, height, text);
        cbutton1.type(FL_TOGGLE_BUTTON);

    #creates Button
    def create_button(self, x, y, widht, height, text):
        button1 = Fl_Button(x, y, widht, height, text);
        

    #adjust window to center
    def center_screen(self):
        self.window.position((Fl.w() - self.window.w())/2, (Fl.h() - self.window.h())/2);

    #closes the window
    def window_end(self):
        self.window.end()
        self.window.show(sys.argv)

def main():
        window_fltk = Widgets()
        window = window_fltk.createWindow(0, 0, 560, 600, "Registration Form")                  #creating window

        window_fltk.create_Textbox(120,40,400,25,"First Name: ")                                #adding textbox to window
        window_fltk.create_Textbox(120,80,400,25,"Last Name: ")
        window_fltk.create_Textbox(120,120,400,25,"Email Address: ")

        window_fltk.round_button(120, 160, 100 ,30, "Male")                                     #adding radio button widget to window
        window_fltk.round_button(220, 160, 100 ,30, "Female")
        

        date = (("1",),("2",),("3",),("4",),("5",),("6",),("8",),("9",),("10",),                #creating list of dates for date of birth field
                ("11",),("12",),("13",),("14",),("15",),("16",),("17",),("18",),("19",),("20",),
                )#("21",),("22",),("23",),("24",),("25",),("26",),("27",),("28",),("29",),("30",),
                #("31",))

        month = (("January",),("February",),("March",),("April",),("May",),("June",),
                 ("July",),("August",),("September",),("Octobar",),("November",),("December",))
        
        year = (("2000",),("1999",),("1998",),("1997",),("1996",),("1995",),("1994",),
                ("1993",),("1992",),("1991",),("1990",),("1989",),("1988",),("1987",),
                ("1986",),("1985",),("before 1985",))

        window_fltk.pulldown(120,200,80,25, date, "Date of Birth:")                             #adding drop down list to window
        window_fltk.pulldown(220,200,80,25, month, "")
        window_fltk.pulldown(320,200,80,25, year, "")

        window_fltk.create_Textbox(120, 260,400,25,"Postal Address: ")  

        window_fltk.toggle_button(50, 380, 100, 25, "Agree Terms And Conditions")               #adding toggle button to window

        window_fltk.create_button(120, 460, 100, 25, "Register")                                #adding normal button to window
        window_fltk.create_button(260, 460, 100, 25, "Cancel")

        box = Fl_Box(100,560,300,40,"WARNING: PLease don't try to register on this page.")      #adding text to window

        window_fltk.window_end()                                                                #closing window

        Fl.run()

if __name__ == '__main__':
    main()
