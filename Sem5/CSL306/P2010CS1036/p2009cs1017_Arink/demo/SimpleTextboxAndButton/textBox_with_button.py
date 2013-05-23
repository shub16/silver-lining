#demo.py 
#This demo code for WX_Canvas class
from wxGUI import *

def SubmitButtonClick(event):
	textArea.appendText("Button has been click\n")
	return True 

#canvas construtor
canvas = wxCanvas(1, 'wxPython1' ,200,400)

#Adding textarea
textArea = TextArea("This is a demo text\n",0,0,200,200)
canvas.add(textArea)

#Adding button
btn = Button("MyButton",0,210,200,20)
btn.clickListener(SubmitButtonClick)
canvas.add(btn)
canvas.show()