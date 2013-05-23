from AnyGUI.qtGUI import *


def Evaluate(event=None):
    display = "" 
    textarea.clear()
    temp = "Your hobbies are the following:"
	
   	
    if(checkbox1.get_state()):
        display = display + "You like Swimming\n"
    
    if(checkbox2.get_state()):
        display = display + "You like reading novels\n"

    if(checkbox3.get_state()):
        display = display + "You like listening to music\n"

    if(checkbox4.get_state()):
        display = display + "You like cycling\n"

    if(checkbox5.get_state()):
        display = display + "You like to write poems\n"

    if(checkbox6.get_state()):
        display = display + "You like dancing\n"

    if(not(checkbox1.get_state()) and not(checkbox2.get_state()) and not(checkbox3.get_state()) and not(checkbox4.get_state()) and not(checkbox5.get_state()) and not(checkbox6.get_state())):
	display = display + "No hobbies? Get a Life :P \n"   


    
    textarea.setText("You are "+rb1.get_state()+"\n\n"+temp+"\n\n"+display+"\n\n")
    return True 


#Constructor canvas
canvas = Main_Window(1, 'Common API | Kshitij_PyQt' ,510,300)

#Creating checkboxes for displaying hobbies
checkbox1 = CheckBox("Swimming",370,20,215,20)
checkbox2 = CheckBox("Reading Books",370,45,215,20)
checkbox3 = CheckBox("Music",370,70,215,20)
checkbox4 = CheckBox("Cycling",370,95,215,20)
checkbox5 = CheckBox("Poetry",370,120,215,20)
checkbox6 = CheckBox("Dancing",370,145,215,20)

#Adding checkboxes 
canvas.add_widget(checkbox1)
canvas.add_widget(checkbox2)
canvas.add_widget(checkbox3)
canvas.add_widget(checkbox4)
canvas.add_widget(checkbox5)
canvas.add_widget(checkbox6)


#Radio buttons for gender
rb1 = RadioButtons(90,30)
rb1.add_radiobutton("Male",10,20)
rb1.add_radiobutton("Female",10,45)
canvas.add_widget(rb1)


#Adding the text area
textarea = TextBox("Please select the appropriate options and then press the evaluate button.You may also enter text here.",120,20,230,150)
canvas.add_widget(textarea)

#Creating Buttons
submitBtn = Button("Evaluate",170,210,120,30)

#Callback methods on button click
submitBtn.on_click(Evaluate)


#Adding button to canvas
canvas.add_widget(submitBtn)

canvas.show()

