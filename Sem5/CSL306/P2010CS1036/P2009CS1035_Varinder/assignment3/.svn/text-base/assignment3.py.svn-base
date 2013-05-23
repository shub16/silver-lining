from fltk import *

window = Fl_Window(1000,100,500,800)
window.label("assignment 1")

textbox = Fl_Multiline_Input(40,40,400,300)

button = Fl_Button(180,350, 180,50)
button.label("Button")

radio1 = Fl_Round_Button(40, 400, 20, 20)
radio1.type(102)
radio1.pyChildren=[]
radio1.selection_color(1)
radio1.align(8)
radio1.label('radio')

radio2 = Fl_Round_Button(40, 425, 20, 20, "radio")
radio2.type(102)
radio2.pyChildren=[]
radio2.selection_color(1)
radio2.align(8)
radio2.label('radio')

chk = Fl_Check_Button(40,475,20,20,"check_box")

menuitems = (( "&Menu_Bar",              0, 0, 0, FL_SUBMENU ),
    ( "&New File",        0 ),
    ( "&Open File...",    FL_CTRL + ord('o') ),
    ( "&Insert File...",  FL_CTRL + ord('i'), 0, FL_MENU_DIVIDER ),
    ( "&Save File",       FL_CTRL + ord('s') ),
    ( "Save File &As...", FL_CTRL + FL_SHIFT + ord('s'), 0, FL_MENU_DIVIDER ),
    ( "New &View", FL_ALT + ord('v'), 0 ),
    ( "&Close View", FL_CTRL + ord('w'), 0, FL_MENU_DIVIDER ),
    ( "E&xit", FL_CTRL + ord('q'), 0 ),
    ( None, 0 ),

  ( None, 0 )
)

m = Fl_Menu_Bar(40, 520, 100, 30);
m.copy(menuitems)

window.show()
Fl.run()
