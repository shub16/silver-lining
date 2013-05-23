'''
	Python GUI Project:
	Software Engineering Course
	Author:
		Abhimanyu Niroola   - 2010CS1087 
		Abhishek Arora      - 2010CS1004
		Shubham Chaudhary   - 2010CS1011
		Deepak Garg	    - 2010CS1012
	IIT Ropar
	Mentor: Dr. Anil Seth
	Library Used: 
		1) WX Python
		2) TKinter
		3) PyQT
		4) PyGTK		
'''

if __name__ == '__main__':
    	print "--------Please select a Toolkit to run your code: ----------" 		# Provide user with all the GUI options available
	print "\tPress 1 for TKInter"
	print "\tPress 2 for GTK"
	print "\tPress 3 for Wx"
	print "\tPress 4 for PyQT"
	x = input("Please give your choice: ")			# Asking user to select a GUI
	b=False
	while(b==False):					# Prompt user until he doesnt provide us with 
		if x==1:					
			print "You have choosed Tkinter"	
			import API_tk as API			# Import Tkinter API file
		elif x==2:
			print "You have choosed GTK"
			import API_gtk as API			# Import GTK API file
		elif x==3:
			print "You have choosed WX"
			import API_wx as API			# Import WX API file
		elif x==4:
			print "You have choosed PyQT"		# Import PyQT API file
			import API_qt as API
		else:						# If user entered a invalid choice then ask user for a valid choice 
			print "\n---You have choosed a invalid option"		
			x = input("Please provide a valid choice: ")
			continue
		b=True
		

    	def SubmitButtonClick(event=None):			# Function to call when user clicks on Submit Button
		report=" You are a "+rb2.getValue()+"\n"		# Gender of user
        	report = report+" Your city is "+DropDownList.getValue()+"\n"	# Date of Birth of user
		report = report+" Your Date Of Birth is "+str(int(dd.getValue()))+"/"+str(int(mm.getValue()))+"/"+str(int(yy.getValue()))+"\n"		# Date of Bith of user
		report = report+" Your income is "+str(sli.getValue())+" Lakhs\n"			# Income of user
		
		
		s1=password.getText()
		s2=passwordcon.getText()
		if len(s1)<6:
			if len(s1)==0:
				report=report+" Please Provide a Password.\n"
			else:	
				report=report+" Your Password is very short.\n"
		elif s1!=s2:
			report=report+" Your Password doesnt match.\n"				
        	if(checkbox1.getValue()):			# Check whether checkbox is selected or not
            		report = report + " You understand risks in mutual funds and investments.\n"
        	else:
            		report = report + " You do not understand risks in mutual funds and investments.\n"
			
		    		
		
        	if(checkbox2.getValue()):			# Check whether checkbox is selected or not
            		report = report + " You agree to terms and conditions \n"
        	else:
            		report = report + " You do not agree to terms and conditions\n"
            	textarea.clear()
		textarea.appendText(report+"\n")
        	return True 

	
    	def AboutButtonClick(event=None):			# Function to call when a user clicks on About Button 
        	textarea.setText("Created by  : IIT Ropar Students\n")
        	return True


		
    	Frame = API.WindowFrame(1, 'Login ' ,400,600)		# Creating a Main window.All widgets will be added to this window.
    	
    	labelfirst=API.Label(' First Name',10,10,100,20)	# Creating a Label field for First Name. 
    	Frame.add(labelfirst)					# Adding Label to Main window.
    	
    	first=API.TextLine(160,10,150,20)			# Entry field where user enters his First Name
    	Frame.add(first)					# Adding TextLine widget to Main window.
    	
    	labellast=API.Label(' Last Name',10,40,100,20)		# Creating a Label for Last Name.
    	Frame.add(labellast)					# Adding Label to Main window.
    	
    	last=API.TextLine(160,40,150,20)			# Entry field where user enters his Last Name
    	Frame.add(last)						# Adding TextLine widget to Main window.
    	
    	labeluser=API.Label(' User Name',10,70,100,20)		# Creating a Label field for UserName.
    	Frame.add(labeluser)					# Adding Label to Main window.
    	
    	user=API.TextLine(160,70,150,20)			# Entry field where user enters a username
    	Frame.add(user)						# Adding TextLine widget to Main window.
    	
    	labelpas=API.Label(' Password',10,100,100,20)		# Label for Password.
    	Frame.add(labelpas)					# Adding Label to Main window.
    	
    	password=API.Password(160,100,150,20)			# Entry field where user enters his password
    	Frame.add(password)
    	
    	labelpass=API.Label(' Confirm Password',10,130,130,20)		# Label for Confirming Password.
    	Frame.add(labelpass)						# Adding Label to Main window.
    	
    	passwordcon=API.Password(160,130,150,20)		# Entry field where user enters his password again
    	Frame.add(passwordcon)
    	
    	labelcity=API.Label('City',10,160,100,20)		# Label for Cities
    	Frame.add(labelcity)					# Adding Label to Main window.
    	
    	cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigarh', 'Wasseypur', 'Jaipur' ]	# Cities value List
    	DropDownList = API.DropDownList(cities,160,160,150,20,"<Select your city>")				# Creating a Dropdown DropDownList
    	Frame.add(DropDownList)										# Add DropDownList to Main window
    	
    	labelsex=API.Label('Sex',10,190,100,20)			# Label for sex
    	Frame.add(labelsex)					# Adding label to Main window
  
    	rb2 = API.RadioGroup(100,20)				# Adding a RadioGroup 
    
    
# Adding individual RadioButtons to RadioGroup	
    	rb2.addRadioButton("Male",130,190)			
    	rb2.addRadioButton("Female",220,190)
    	rb2.setButtonTrue(0)
    	Frame.add(rb2)						# Adding RadioGroup to Main window
    	
    	labeldob=API.Label('Date of Birth',10,220,130,20)	# Label for Date Of Birth
    	Frame.add(labeldob)					
    	labelfo=API.Label('(DD/MM/YYYY)',10,240,130,10)
    	Frame.add(labelfo)
    	
    	
    	dd=API.SpinBox(1,31,160,220,50,20) 			# SpinBox for Date
    	Frame.add(dd) 						
    	mm=API.SpinBox(1,12,220,220,50,20) 			# SpinBox for Month
    	Frame.add(mm)
    	yy=API.SpinBox(1980,2000,280,220,70,20) 		# SpinBox for Year
    	Frame.add(yy)  
    	
    	labelincome=API.Label('Income(lpa)',10,260,100,20)	# Label for Income
    	Frame.add(labelincome)
    	
    	sli=API.Slider(1,30,160,250,150,40) 			# Slider widget for Income
    	Frame.add(sli)
    	
    	
# CheckBoxes for confirmation various conditions
    	checkbox1 = API.CheckBox("I understand risks in mutual funds and investments.",10,290,380,20)
    	checkbox2 = API.CheckBox("I agree to terms and conditions",10,320,380,20)
    	checkbox1.setValue(True)
# Adding CheckBoxes to Main window
    	Frame.add(checkbox1)
    	Frame.add(checkbox2)



# Buttons widgets 
    	submitBtn = API.Button("Register",60,360,130,30)		# Button to Register
    	aboutBtn = API.Button("About",210,360,130,30)			# Button to know about the product

    	
    	submitBtn.clickListener(SubmitButtonClick)			# Triggering a method call on Button click  
    	aboutBtn.clickListener(AboutButtonClick)			# Triggering a method call on Button click 

# Adding Buttons to Main window
    	Frame.add(aboutBtn)
    	Frame.add(submitBtn)

# TextArea where results will be displayed
    	textarea = API.TextArea("Click submit button to see output here!!",10,400,380,180)
    	Frame.add(textarea)

    	Frame.show()  							# Command to show Main window.Enters into Eventloop

