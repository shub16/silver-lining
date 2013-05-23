from wx_GUI import * 

if __name__ == '__main__':

    #Functions bind to button events
    def viewClick(self):
        report = "\t COURSE REGISTRATION RECORD\n\n"
        report =report+"Name\t:\t"+name.getText() +"\nEntry Number\t:\t"+entr.getText()+"\nYear\t:\t"+str(rb1.getButton())+"\nSemester\t:\t"+str(Spin.getValue())+"\nDepartment\t:\t"+str(valuelist.getValue())
            
        if(  checkbox4.getBox() or checkbox5.getBox() or checkbox6.getBox() or checkbox7.getBox() or checkbox8.getBox() ):
			report= report + "\n\n\nSelected Elective courses\n"
			i=0
			if(checkbox5.getBox()):
				i=i+1
				report = report +str(i)+ ". Professional Communication\n"
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
			report=report+"\n\nCourse Advisor\t:\t"+str(valuelist1.getValue())+"\n"
			report=report + "\n\nPlease submit the form now!\n"	
        
        else:
            report = report + "\n\nYou have not selected any elective course\n"
		
        textarea.setText(report+"\n\n")
        return True 

    def submitClick(event):
        if( checkbox4.getBox() or checkbox5.getBox() or checkbox6.getBox() or checkbox7.getBox() or checkbox8.getBox() ):
			textarea.setText("Thanks for your time!\n")
        else:
			textarea.setText("Please select atleast 1 course")
        return True

    #Constructor Vista
    Vista = Vista(1, 'Course Registration Form' ,750,500)

    #TextArea
    textarea = TextBuffer("",400,10,310,400)
    Vista.addWidget(textarea)

#name
    label = ShowText("Name",15,13,100,20)
    name=TextArea("",170,15,150,20)	
    Vista.addWidget(name)
    Vista.addWidget(label)

    label1 = ShowText("Entry Number",15,40,100,20)
    entr=TextArea("",170,40,150,20)	
    Vista.addWidget(label1)
    Vista.addWidget(entr)

    #year
    rb1 = RadioButton(80,20)
    rb1.addButton("I Year",15,70)
    rb1.addButton("II Year",100,70)
    rb1.addButton("III Year",185,70)
    rb1.addButton("IV Year",270,70)
    rb1.setButton(1)
    Vista.addWidget(rb1)



# semester 
    vol = ShowText("Semester",15,100,100,15)
    Spin = SpinBox(1,2,180,100,100,20)
    Vista.addWidget(Spin)
    Vista.addWidget(vol)
    


	#Dropdown valuelist
    department = ['Computer Science','Electrical Engineering','Mechanical Engineering','Information Technology','Chemical Engineering','Civil Engineering']
    valuelist = List(department,17,130,150,20,"Department")
    Vista.addWidget(valuelist)


    #checkboxs
    #vol23 = ShowText("Select Elective Courses",15,160,200,50)
    checkbox4 = CheckBox("Modern Algebra",15,180,215,15)
    checkbox5 = CheckBox("Professinal Communication",15,200,215,15)
    checkbox6 = CheckBox("Quantum Physics",15,220,215,15)
    checkbox7 = CheckBox("Real Analysis",15,240,215,15)
    checkbox8 = CheckBox("Structure of Molecules",15,260,215,15)
	
#    checkbox5.setBox(True)
    #Vista.addWidget(vol23)
    Vista.addWidget(checkbox4)
    Vista.addWidget(checkbox5)
    Vista.addWidget(checkbox6)
    Vista.addWidget(checkbox7)
    Vista.addWidget(checkbox8)

	#course advisor
    advisor = ['Dr Anil Seth','Dr Apurva Mudgal','Dr Daya Gaur', 'Dr Nitin Auluck','Dr Iyenger' ]
    valuelist1 = List(advisor,17,290,150,20,"Course Advisor")
    Vista.addWidget(valuelist1)

#Slider
    label65 = ShowText("Rate Our Application",15,320,150,20)
    Vista.addWidget(label65)

    vol = ShowText("Bad",15,350,50,50)
    vol1 = ShowText("Excellent",240,350,80,50)
    cgpa=Slider(0,10,60,335,150,50)
    Vista.addWidget(cgpa)
    Vista.addWidget(vol)
    Vista.addWidget(vol1)


    #Creating Buttons
    viewBtn = Button("View",20,400,80,30)
    submitBtn = Button("Submit",120,400,80,30)

    #Callback methods on buttons click
    viewBtn.clickTrigger(viewClick)
    submitBtn.clickTrigger(submitClick)

    #Adding buttons to Vista
    Vista.addWidget(submitBtn)
    Vista.addWidget(viewBtn)

    Vista.show()

   
