if __name__ == '__main__':
	
	print "--------Please select a Toolkit to run your code: ----------"
	print "\tPress 1 for TKInter"
	print "\tPress 2 for GTK"
	print "\tPress 3 for Wx"
	print "\tPress 4 for PyQT"
	x = input("Please give your choice: ")
	b=False
	while(b==False):
		if x==1:
			print "You have choosed Tkinter"
			import API_tk as API
		elif x==2:
			print "You have choosed GTK"
			import API_gtk as API
		elif x==3:
			print "You have choosed WX"
			import API_wx as API
		elif x==4:
			print "You have choosed PyQT"
			import API_qt as API
		else:
			print "\n---You have choosed a invalid option"
			x = input("Please provide a valid choice: ")
			continue
		b=True
	
	tagcustomer=0
	def saveLetter(event=None):				# saves the letter into a file
		file_name=filename.getText()
		if file_name=="":				# if file_name not given then give default file name "output"
			file_name="output"
		text_file = open(file_name+".txt", "w")
		text_file.write(textEdit.getText())		# writing the text i.e. letter from the textEdit to text_file
		text_file.close()
		filename.clear()
	def newLetter(event=None):				# inserts the format of the letter in the textEdit
		global tagcustomer
		tagcustomer=0
	        textEdit.clear()
	        textEdit.appendText("FLIPKART")
	        textEdit.appendText("\n")
	        textEdit.appendText("321 Ansari Road")
	        textEdit.appendText("\n")
	        textEdit.appendText("Darya Ganj")
	        textEdit.appendText("\n")
	        textEdit.appendText("Delhi")
	        textEdit.appendText("\n")
	        textEdit.appendText("110002")
	        textEdit.appendText("\n")
	        textEdit.appendText("\n")
		textEdit.appendText("Dear ")
	        textEdit.appendText(",")
	        for i in range(2):
		    textEdit.appendText("\n")
	        textEdit.appendText("Yours sincerely,")
	        #for i in range(2):
	        textEdit.appendText("\n")
	        textEdit.appendText("Flipkart Group")
	        textEdit.appendText("\n")
	        

	def insertCustomer(customer):			# function to inset the details of the customer
		global tagcustomer
		if tagcustomer==1:
		    return
	        if not customer:
	            return
	        customerList = customer.split(', ')	# spliting the customer string w.r.to the commas occuring in the string
	        firstName=customerList[0].split(' ')
	        textEdit.AppendBefore(",",firstName[0])
		string_address=""
		for i in customerList[0:]:
	                    string_address=string_address+i+"\n"
		string_address=string_address+"\n\n"
		textEdit.AppendBefore("Dear",string_address)
		tagcustomer=1
	      
	
	def addParagraph(paragraph):			# function to insert the paragraph in the letter 
	        if not paragraph:
	            return
		textEdit.AppendBefore("Yours sincerely,",paragraph+"\n \n")
	
	Frame = API.WindowFrame(1, 'login' ,800,640)
	letlabel=API.Label("LETTER",15,50,300,20)
	Frame.add(letlabel)
	
	textEdit=API.TextArea("",15,70,430,510)
	Frame.add(textEdit)
	# clist contains the name and address of the customers
	clist=["Ashish Rai, Harmony Enterprises, 12 Adalat Road, New Delhi",
            "Kiran Khanna, 23 Anand Nagar, Aurangabad",
            "Harish Sharma, 38 Sector 6, Rohini, New Delhi",
            "Gaurav Jha, 48 Yara Road, Andheri, Mumbai",
            "Hemant Kumar, Today's Coffee Shop, 53 Sector 17, Chandigarh",
            "Akshat Meena, 67 Nangal Road, Rupnagar, Punjab"]
	cuslabel=API.Label("Customer List",460,50,250,20)	
	Frame.add(cuslabel)
	customer=API.SelectList(clist,460,70,325,200)   			# creating the customer list which containd information of the customer
	Frame.add(customer)
	# plist contains the frequently used paragraphs in letters of the company 
	plist=["Thank you for your payment which we have received today.",	
            "Your order has been dispatched and should be with you within "
                "28 days.",
            "We have dispatched those items that were in stock. The rest of "
                "your order will be dispatched once all the remaining items "
                "have arrived at our warehouse. No additional shipping "
                "charges will be made.",
            "You made a small overpayment (less than Rs 100/-) which we will keep "
                "on account for you, or return at your request.",
            "You made a small underpayment (less than Rs 100/-), but we have sent "
                "your order anyway. We'll add this underpayment to your next "
                "bill.",
            "Unfortunately you did not send enough money. Please remit an "
                "additional Rs 50/-. Your order will be dispatched as soon as the "
                "complete amount has been received.",
            "You made an overpayment (more than Rs 200/-). Do you wish to buy more "
                "items, or should we return the excess to you?"]
	parlabel=API.Label("Paragraphs",460,280,240,20)			
	Frame.add(parlabel)
	paragraph=API.SelectList(plist,460,300,325,220)		# creating the paragraph list 	
	Frame.add(paragraph)
	newLetter()					# initializing the textEdit by a defined format of letter
	customer.clickListener(insertCustomer)
        paragraph.clickListener(addParagraph)
	button=API.Button("New Letter",15,10,100,30)		# 'New' Button for opening a new letter
	Frame.add(button)
	button.clickListener(newLetter)
	button=API.Button("Save",330,590,70,30)	# 'Save' Button to save the letter
	Frame.add(button)
	button.clickListener(saveLetter)		# addign action listener to the 'save' button 
	filelabel=API.Label('Enter Filename',15,590,100,30)
	Frame.add(filelabel)
	filename=API.TextLine(125,590,200,30)		# including a TextLine for specifying the file to save the Letter
    	Frame.add(filename)				# adding the TextLine filename to the Frame
	Frame.show()					# Displaying the window on the screen
