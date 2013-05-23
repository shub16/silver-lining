import pyFLTK_API as gui
#import pyTK_API as gui

if __name__== '__main__':
    frame = gui.Xwindow(1, 'assignment 4', 510, 500)

    text = gui.TextView('Text', 300, 30,200,300)
    frame.add(text)


    button =gui.Button('submit', 200, 450, 90,30)
    frame.add(button)

    checkbox1 = gui.CheckBox('check box 1', 30, 90, 20,20)
    frame.add(checkbox1)
    checkbox2 = gui.CheckBox('check box 2', 30, 130, 20,20)
    frame.add(checkbox2)

    rb = gui.Radio(150, 30)
    rb1 = rb.addRadioButton('rb1', 30, 160)
    rb2 = rb.addRadioButton('rb2', 30, 190)
    rb3 = rb.addRadioButton('rb3', 30, 220)
    frame.add(rb)
    
    frame.show()
