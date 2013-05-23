from AnyGUI.gtkGUI import *

#Functions bind to button events
def SubmitButtonClick(event=None):
    report = "" 
    textarea.clear()
    temp = "Your hobbies are the following:"
	
   
    temp2 = "Your city is "+valuelist.getValue()+"\n"
	
    if(checkbox1.get_state()):
        report = report + "You like Swimming\n"
    
    if(checkbox2.get_state()):
        report = report + "You like reading novels\n"

    if(checkbox3.get_state()):
        report = report + "You like listening to music\n"

    if(checkbox4.get_state()):
        report = report + "You like cycling\n"

    if(checkbox5.get_state()):
        report = report + "You like to write poems\n"

    if(checkbox6.get_state()):
        report = report + "You like dancing\n"

    if(not(checkbox1.get_state()) and not(checkbox2.get_state()) and not(checkbox3.get_state()) and not(checkbox4.get_state()) and not(checkbox5.get_state()) and not(checkbox6.get_state())):
	report = report + "No hobbies? Get a Life :P \n"   

    marks =str( performance.getValue())
    cg = str(Spin.getValue())
    
    textarea.setText("You are "+rb1.get_state()+"\n\n"+temp2+"\n"+temp+"\n\n"+report+"\n\n"+"Marks :"+marks+"\n\n"+"CGPA :"+cg)
    return True 





#Constructor canvas
canvas = Main_Window(1, 'Common API | Gurpreet_Tkinter' ,510,400)

#Spin Box
label_marks = LabelText("CGPA ",55,270,60,50)
Spin =  SpinBox(0.0,10.0,130,275,100,30)
canvas.add_widget(Spin)
canvas.add_widget(label_marks)

#Dropdown valuelist
cities = ['Amritsar', 'Mumbai', 'Ropar', 'Bhatinda', 'Chandigrah' ]
valuelist = ValueList(cities,130,200,220,20,"<Select your city>")
canvas.add_widget(valuelist)

#checkboxs
checkbox1 = CheckBox("Swimming",370,20,215,20)
checkbox2 = CheckBox("Reading Books",370,45,215,20)
checkbox3 = CheckBox("Music",370,70,215,20)
checkbox4 = CheckBox("Cycling",370,95,215,20)
checkbox5 = CheckBox("Poetry",370,120,215,20)
checkbox6 = CheckBox("Dancing",370,145,215,20)


canvas.add_widget(checkbox1)
canvas.add_widget(checkbox2)
canvas.add_widget(checkbox3)
canvas.add_widget(checkbox4)
canvas.add_widget(checkbox5)
canvas.add_widget(checkbox6)


#radioGroup1
rb1 = RadioButtons(90,30)
rb1.add_radiobutton("Male",10,20)
rb1.add_radiobutton("Female",10,45)
canvas.add_widget(rb1)


#TextBox
textarea = TextBox("Please select the appropriate options and then press the evaluate button.You may also enter text here.",120,20,230,150)
canvas.add_widget(textarea)

#Creating Buttons
submitBtn = Button("Evaluate",170,350,120,30)

#Callback methods on buttons click
submitBtn.on_click(SubmitButtonClick)

#Slider
label_marks = LabelText("Marks ",55,225,60,50)
performance=Slider(0,100,130,220,200,50)
canvas.add_widget(performance)
canvas.add_widget(label_marks)
#Adding buttons to canvas

canvas.add_widget(submitBtn)

canvas.show()

