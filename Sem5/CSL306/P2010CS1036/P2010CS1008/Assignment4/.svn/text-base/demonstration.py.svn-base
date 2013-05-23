from tk_GUI import * 
#xGUI(Environment = "gtk")


if __name__ == '__main__':

    #Functions bind to button events
    def viewClick():
#        report = " Your city is "+valuelist.getValue()+"\
        report = "\n"

        report = report + "Hello!  "+rb1.getButton()+" "+valuelist.getValue()+"  student\n\n"
#        report = report + " Hello!  "+rb2.getButton()+"  student\n"
        
        if( checkbox1.getBox() or checkbox2.getBox() or checkbox3.getBox() or checkbox4.getBox() or checkbox5.getBox() or checkbox6.getBox() or checkbox7.getBox() or checkbox8.getBox() ):
#			print "Yes"
			report= report + "You have selected following elective courses\n"
			i=0
			if(checkbox5.getBox()):
				i=i+1
				report = report +str(i)+ ". Professional Communication\n"
			if(checkbox1.getBox()):
				i=i+1
				report = report +str(i)+ ". Measuring Molecules\n"
			if(checkbox2.getBox()):
				i=i+1
				report = report +str(i)+ ". Phonetics\n"
			if(checkbox3.getBox()):
				i=i+1
				report = report +str(i)+ ". Microeconomics\n"
			if(checkbox4.getBox()):
				i=i+1
				report = report +str(i)+ ". Modern Algebra\n"
			if(checkbox6.getBox()):
				i=i+1
				report = report +str(i)+ ". Quantum Physics\n"
			if(checkbox7.getBox()):
				i=i+1
				report = report +str(i)+ ". Real Analysis\n"
			if(checkbox8.getBox()):
				i=i+1
				report = report +str(i)+ ". Structure Of Molecules\n"
			report=report + "\nPlease submit the form now\n"	
        
        else:
            report = report + "You have not selected any elective course\n"

#		report = report + "Your class for these courses will start from  are "+rb1.getValue()+"\n"
#		report = report + " you need "+rb2.getValue()+"\n"

#        textarea.concatText(report+"\n\n")
        textarea.setText(report+"\n\n")
        return True 

    def submitClick():
        if( checkbox1.getBox() or checkbox2.getBox() or checkbox3.getBox() or checkbox4.getBox() or checkbox5.getBox() or checkbox6.getBox() or checkbox7.getBox() or checkbox8.getBox() ):
			textarea.setText("Thanks for your time!\n")
        else:
			textarea.setText("Please select atleast 1 course")
        return True



    #Constructor Vista
    Vista = Vista(1, 'Course Registration Form' ,600,350)

	#Dropdown valuelist
    department = ['Computer Science','Electrical Engineering','Mechanical Engineering','Information Technology','Chemical Engineering','Civil Engineering']
    valuelist = List(department,17,60,200,20,"Department")
    Vista.addWidget(valuelist)
	
    #checkboxs
    checkbox1 = CheckBox("Measuring Molecules",15,100,215,15)
    checkbox2 = CheckBox("Phonetics",15,120,215,15)
    checkbox3 = CheckBox("Microeconomics",15,140,215,15)
    checkbox4 = CheckBox("Modern Algebra",15,160,215,15)
    checkbox5 = CheckBox("Professinal Communication",15,180,215,15)
    checkbox6 = CheckBox("Quantum Physics",15,200,215,15)
    checkbox7 = CheckBox("Real Analysis",15,220,215,15)
    checkbox8 = CheckBox("Structure of Molecules",15,240,215,15)
	
    checkbox1.setBox(True)
    Vista.addWidget(checkbox1)
    Vista.addWidget(checkbox2)
    Vista.addWidget(checkbox3)
    Vista.addWidget(checkbox4)
    Vista.addWidget(checkbox5)
    Vista.addWidget(checkbox6)
    Vista.addWidget(checkbox7)
    Vista.addWidget(checkbox8)

    #radioGroup1
    rb1 = RadioButton(60,20)
    rb1.addButton("II Year",15,25)
    rb1.addButton("III Year",80,25)
    rb1.addButton("IV Year",150,25)
#    rb1.addButton("Great",160,10)
    rb1.setButton(1)
    Vista.addWidget(rb1)


    #TextArea
#    textarea = TextBuffer("\n Click submit button to see output here!!",250,10,250,200)
    textarea = TextBuffer("",300,10,250,250)
    Vista.addWidget(textarea)

    #Creating Buttons
    viewBtn = Button("View",130,280,120,30)
    submitBtn = Button("Submit",350,280,120,30)

    #Callback methods on buttons click
    viewBtn.clickTrigger(viewClick)
    submitBtn.clickTrigger(submitClick)

    #Adding buttons to Vista
    Vista.addWidget(submitBtn)
    Vista.addWidget(viewBtn)

    Vista.show()

    
 
