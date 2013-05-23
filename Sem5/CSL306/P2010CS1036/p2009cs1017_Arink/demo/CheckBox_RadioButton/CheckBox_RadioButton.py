
from wxGUI import *


def SubmitButtonClick(event):
	report = " Your city is "+valuelist.getValue()+"\n"
	if(checkbox1.getValue()):
		report = report + " you have read the code\n"
	else:
		report = report + " you have not read the code\n"

	if(checkbox2.getValue()):
		report = report + " you have read the documentation\n"
	else:
		report = report + " you have not read the documentation\n"

	report = report + " you are "+rb1.getValue()+"\n"
	report = report + " you need "+rb2.getValue()+"\n"

	textarea.appendText("_______________________\n"+report+"\n\n")
	return True 

def AboutButtonClick(event):
        textarea.setText("Created by wxGUI -v1.0\nAuthor : Arink Verma\n\nhttp://10.1.0.140/trac/wiki/ArinkVerma\n")
        return True




canvas = wxCanvas(1, 'My wxPython' ,510,300)

cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
valuelist = ValueList(cities,10,10,200,"<Select your city>")
canvas.add(valuelist)

checkbox1 = CheckBox("I have read the code.",10,45)
checkbox2 = CheckBox("I have read the documentation.",10,70)
checkbox1.setValue(True)
canvas.add(checkbox1)
canvas.add(checkbox2)

rb1 = RadioGroup()
rb1.addRadioButton("Nice",10,110)
rb1.addRadioButton("Good",70,110)
rb1.addRadioButton("Great",140,110)
rb1.setButtonTrue(2)
canvas.add(rb1)


rb2 = RadioGroup()
rb2.addRadioButton("Option #1",10,160)
rb2.addRadioButton("Option #2",110,160)
canvas.add(rb2)

#TextArea
textarea = TextArea("\n Click submit button to see output here!!",250,10,250,200)
canvas.add(textarea)

#Creating Buttons
submitBtn = Button("Submit",130,230,120,30)
aboutBtn = Button("About",260,230,120,30)

#Callback methods on buttons click
submitBtn.clickListener(SubmitButtonClick)
aboutBtn.clickListener(AboutButtonClick)

#Adding buttons to canvas
canvas.add(aboutBtn)
canvas.add(submitBtn)

canvas.show()