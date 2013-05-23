"""
This pyfltk Program contains widgets like : radio-buttons, checkboxes, list of values; 
Also, action listeners will be added later.
"""

from fltk import *

xpos = 40
ypos = 40

class Form():                                                   
                                                                                
    def __init__(self, width = 500, height = 500):             
       
        main_Win = Fl_Window( width, height, " Registration Form ")

        # input box        
        name_text_Box = Fl_Box( xpos, ypos + 20, 40, 30, " Name : ")
        name_Input = Fl_Input(xpos + 60 , ypos + 20 , 250, 30)
        
        # radio buttons
        gender_text_Box = Fl_Box( xpos, ypos + 70, 60, 20, " Gender :    ")
        male_Button = Fl_Round_Button( xpos + 100 , ypos + 70, 100, 20, " Male ")
        male_Button.type(102)
        female_Button = Fl_Round_Button( xpos + 220 , ypos + 70, 100, 20, " Female ")
        female_Button.type(102)
        
        # List of value widgets        
        branch_text_Box = Fl_Box( xpos , ypos + 120, 50, 30, " Branch :  ")
        choices = ( ("select", ), ("CSE", ), ("EE", ) ,("Others", ), (None, ) ) 
        ch = Fl_Choice ( xpos + 150, ypos + 120,120,25)
        ch.copy(choices)

        # added 3 check boxes         
        q_Text_Box = Fl_Box( xpos + 60, ypos + 200, 180, 30, " What are you upto after B.tech., choose some :")
        checkbox1 = Fl_Check_Button(xpos + 60, ypos + 275, 80, 15, " Research ")
        checkbox1.down_box(FL_DOWN_BOX)
        checkbox2 = Fl_Check_Button(xpos + 60, ypos + 305, 80, 15, " Job ")
        checkbox2.down_box(FL_DOWN_BOX)
        checkbox3 = Fl_Check_Button(xpos + 60, ypos + 335, 70, 15, " others:")
        checkbox3.down_box(FL_DOWN_BOX)
        name_Input = Fl_Input(xpos + 150 , ypos + 335 , 150, 20)

        # some buttons at bottom
        submit_Button = Fl_Button(xpos + 40, ypos + 400, 80, 40, "Submit")
        submit_Button.box(FL_PLASTIC_UP_BOX)
        submit_Button.color(FL_CYAN)
        submit_Button.selection_color(FL_BLUE)

        quit_Button = Fl_Button(xpos + 320, ypos + 400, 80, 40, "Quit")
        quit_Button.box(FL_PLASTIC_UP_BOX)
        quit_Button.color(fl_rgb_color(255, 0, 0))
        quit_Button.callback(quit_action)
        
        # end of window creation
        main_Win.end()
        main_Win.show()
        Fl.run()                # run Fltk event loop

def quit_action(widget):     
    import sys
    sys.exit(0)    

def main():
    form = Form()                                                             

if __name__ == '__main__':
    main()   
