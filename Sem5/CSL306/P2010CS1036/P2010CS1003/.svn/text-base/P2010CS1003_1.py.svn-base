import wx
import naveen											# Importing a module naveen.py


''' Frame-widget class'''
class frame(wx.Frame):
    def __init__(self, parent, id, title, l,b):							# Contructor of the frame class
	self.app = wx.App(False)				
	wx.Frame.__init__(self, parent, id, title)						# Initializing a frame
	self.SetSize(wx.Size(l,b))								# Setting size of the frame
	self.Centre()										# Setting the position of the frame
	self.panel = wx.Panel(self, -1)								# Initializing a panel

    def click_close(self, eventfunction):							# Function to handle the close button click
	self.Bind(wx.EVT_CLOSE, eventfunction)	

    def add_widget(self,widget):								# Function to add widgets in the frame
	if(isinstance(widget,button)):								# To add a button
		widget.controller = wx.Button(self.panel, -1, widget.label,  widget.pos, widget.size, widget.style)
	elif(isinstance(widget,textbox)):							# To add a Textbox
		widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.pos, widget.size, widget.style)
	elif(isinstance(widget,drop_list)):							# To add a Combo Box
		widget.controller = wx.ComboBox(self.panel, -1, widget.value,widget.pos,widget.size,widget.choices,widget.style)
	elif(isinstance(widget,static_text)):							# To add a Static Text
		widget.controller = wx.StaticText(self.panel, -1, widget.label, widget.pos)	
	elif(isinstance(widget,radio_button_set)):						# To add a radio button set
		widget.controller = []
		radio_controller = wx.RadioButton(self.panel, -1, widget.labels[0], pos = widget.pos[0], style =widget.style)
		widget.controller.append(radio_controller)
		for i in range(1,len(widget.labels)):
			radio_controller = wx.RadioButton(self.panel, -1, widget.labels[i], pos = widget.pos[i])
			widget.controller.append(radio_controller)
		widget.controller[widget.default_pos].SetValue(True)
 	elif(isinstance(widget,check_box_set)):							# To add a check box set
		widget.controller = []
		for i in range(0,len(widget.labels)):
			chkbx_controller = wx.CheckBox(self.panel, -1, widget.labels[i], widget.positions[i])
			widget.controller.append(chkbx_controller)
		for i in range(0,len(widget.controller)):
			widget.controller[i].SetValue(False)
		for j in range(len(widget.pos_list)):
			widget.controller[widget.pos_list[j]].SetValue(True)


''' Button - widget class '''

class button(wx.Button):
    def __init__(self, x, y, l = 100, b = 30, name = "", style = wx.BU_EXACTFIT):            	# Constructor for button class
	self.label = name								    	# Assigning name to the button	
	self.pos = (x,y)								     	# Setting position of the button
	self.size = wx.Size(l,b)								# Setting size of the button
	self.style = style									# Setting the button style
    def click(self, eventfunction):								# Function to handle button click
	self.controller.Bind(wx.EVT_BUTTON, eventfunction)

''' Text- box widget class'''

class textbox(wx.TextCtrl):
    def __init__(self, x, y, l, b, text = "", style = wx.DEFAULT):				# Constructor for textbox class
	self.text = text									# Setting text in the textbox
	self.pos = (x,y)									# Setting position of the textbox
	self.size = (l,b)									# Setting size of the textbox
	self.style = style									# Setting the style of the textbox
    def clear(self):										# Funtion to clear the contents in textbox
	self.controller.Clear()
    def set_text(self,text):									# Funtion to set text in the textbox
	self.controller.SetValue(text)
    def append_text(self,text):									# Function to append text in the textbox
	self.controller.AppendText(text)
    def get_size(self):
	a = self.controller.GetLastPosition()
	return a
    def get_text(self, start, end):								# Function to get complete text from the textbox
	return self.controller.GetString(start,end) 

''' Combo-box class '''
class drop_list(wx.ComboBox):
    def __init__(self, x, y, l, b, choicelist, value = "", style = wx.CB_READONLY):		# Constructor of the Combo-box class
	self.pos = (x,y)									# Setting position of the combo-box
	self.choices = choicelist								# Setting the list in the combo-box
	self.style = style									# Setting the style of the combo-box
	self.size = (l, b)									# Setting the size of the combo-box
	self.value = value									# Setting the default value in the combo-box
    def get_value(self):									# Function to get selected value in combo-box
	if (self.controller == None):
		return self.value
	else:
		text = self.controller.GetValue()
		self.controller.SetValue(self.value)
		return text

''' Static - text class '''

class static_text(wx.StaticText):					
    def __init__(self, x, y, entry):								# Constructor of the Static-text class
	self.pos = (x,y)									# Setting the position of the static-text
	self.label = entry									# Setting the text in static-text 

''' Radio - Button Group Class '''

class radio_button_set(wx.RadioButton):
    default_pos = 0										# Setting 1st entry as default
    controller = None
    def __init__(self, style = wx.CB_READONLY):							# Constructor of the Radio-Button group class
	self.labels = []									# Initializing the list of labels
	self.pos = []										# Initializing the list of positions
	self.style = style									# Setting the style of the radio buttons

    def add_radio_button(self, x, y, entry):							# Function to add radio buttons in the group
	self.labels.append(entry)
	self.pos.append((x,y))		
        
    def get_value(self):									# Function to return the selected value
	for i in range(len(self.controller)):
		if(self.controller[i].GetValue()):
			return self.labels[i]
    def set_default(self,pos):									# Function to set the default selection
	self.controller[pos].SetValue(True)

''' Check - box group class '''

class check_box_set(wx.CheckBox):	
    controller = None
    pos_list = []
    def __init__(self):										# Constructor of the Checkbox group
	self.labels = []									# Initializing the list of entries
	self.positions = []									# Initializing the list of positions

    def add_check_box(self, x, y, entry):							# Function to add a checkbox in the group
	self.labels.append(entry)			
	self.positions.append((x,y))

    def get_marked(self):									# Function to return list of checked entries
	marked = []
	for i in range(len(self.controller)):						
		if(self.controller[i].IsChecked()):
			marked.append(self.labels[i])
	return marked
									# Function to check the entries at the positions given in input list
    def set_marked(self, pos_list=[]):								 
	if(self.controller == None):
		self.pos_list = pos_list
	else:	
		for i in range(len(self.controller)):
			self.controller[i].SetValue(False)
		for j in range(len(pos_list)):
			self.controller[j].SetValue(True)


''' Demonstration '''

		
if __name__=='__main__':									# To be executed only if this file is run
	def OnClickClear(event):								# Function to handle clear button click
		dlg = wx.MessageDialog(frame1, "Do you really want to clear records?","Confirm", wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)
		result = dlg.ShowModal()							# Dialog to confirm action
		dlg.Destroy()
		if result == wx.ID_YES:
	        	tb1.clear()

	def OnClickExit(event):									# Function to handle Exit button click in frame1
		dlg = wx.MessageDialog(frame1, "Do you really want to close this application?","Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
		result = dlg.ShowModal()							# Dialog to confirm exit
		dlg.Destroy()
		if result == wx.ID_OK:
			frame1.Destroy()
			exit(0)

	def OnClickSubmit(event):								# Function to handle submit button click
		a = 0
		mrkd1 = chkboxset1.get_marked()
		mrkd2 = chkboxset2.get_marked()
		for i in range(0,len(mrkd1)):
			for j in range(0,len(mrkd2)):
				if(mrkd1[i] == mrkd2[j]):
					a = a + 1					
		if( a > 0):		
			dlg = wx.MessageDialog(frame1, "Courses dropped and added cannot be the same : " + str(a) + " errors","Error", wx.OK|wx.ICON_EXCLAMATION)										# Dialog to show error
			dlg.ShowModal()
			dlg.Destroy()
		elif( len(mrkd1) != 0) | (len(mrkd2) != 0):					# Showing the entries in the textbox
			text = tb2.get_text(0, tb2.get_size())
			tb1.append_text("Name        :  " +text+"\n")
			tb2.set_text("")
			text = tb3.get_text(0, tb3.get_size())
			tb1.append_text("Entry No  :  " +text+"\n")
			tb3.set_text("")
			text = combo1.get_value()
			tb1.append_text("Year           :  " +text+"\n")
			text = radioset1.get_value()
			tb1.append_text("Branch      :  " +text+"\n")
			if(len(mrkd1) != 0):	
				tb1.append_text("\nCourses Added --->\n")		
				for i in range(0,len(mrkd1)):
					tb1.append_text(str(i+1) +") "+mrkd1[i]+"\n")
				chkboxset1.set_marked()
	
			if(len(mrkd2) != 0):
				tb1.append_text("\nCourses Dropped --->\n")		
				for i in range(0,len(mrkd2)):
					tb1.append_text(str(i+1) +") "+mrkd2[i]+"\n")
				chkboxset2.set_marked()
			text = radioset2.get_value()
			tb1.append_text("\nAdd-Drop  :  "+text+"\n\n\n")
			radioset2.set_default(1)	
	
	def OnClickWx(event):									# Function to handle wxPython button click
		frame1.Show(True)
		frame0.Show(False)

	def OnClickQt(event):									# Function to handle PyQt button click
		frame0.Show(False)
		frame2app = naveen.main()
		frame2app.MainLoop()	

	def OnClickExit0(event):								# Function to handle Exit button click in frame0
		dlg = wx.MessageDialog(frame0, "Do you really want to close this application?","Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
		result = dlg.ShowModal()
		dlg.Destroy()
		if result == wx.ID_OK:
			frame0.Destroy()
			exit(0)

	
	app = wx.App(0)
	frame0 = frame(None, -1, 'Choose One', 320, 160)					# Creating main-frame
	frame0.click_close(OnClickExit0)							# Close button click
	st01 = static_text(10, 10, "Choose any one of the options ---> ")			# Static text in main-frame	
	frame0.add_widget(st01)									# Adding the static text

	button01 = button(10, 40, name="1. wxPython", style=wx.BU_LEFT)				# Creating wxPython Button
	frame0.add_widget(button01)								# Adding the wxPython button
	button01.click(OnClickWx)								# wxPython button click

	button02 = button(10, 70, name = "2. PyQt", style = wx.BU_LEFT)				# Creating PyQt Button
	frame0.add_widget(button02)								# Adding the PyQt Button
	button02.click(OnClickQt)								# PyQt Button Click

	button03 = button(10, 100, 100, name  = "3. Exit", style = wx.BU_LEFT)			# Creating Exit Button
	frame0.add_widget(button03)								# Adding Exit button
	button03.click(OnClickExit0)								# Exit Button click

	frame0.Show()										# Displaying the main frame


	frame1 = frame(None, -1, 'Assignment-3', 800, 650)					# Creating frame1
	frame1.click_close(OnClickExit)								# Close button click for frame1

	tb1 = textbox(404, 4,390, 590, style = wx.TE_MULTILINE|wx.TE_READONLY)			# Creating Multiline Read-Only Textbox
	frame1.add_widget(tb1)									# Adding it to frame1

	tb2 = textbox(130, 15, 250, 25 )							# Creating a Default Textbox
	frame1.add_widget(tb2)									# Adding it to frame1

	tb3 = textbox(130, 50, 250, 25 )							# Creating a Default Textbox
	frame1.add_widget(tb3)									# Adding it to frame1

	button1 = button(700, 610, 85, 25, "Clear")						# Creating Clear Button
	frame1.add_widget(button1)								# Adding it to frame1
	button1.click(OnClickClear)								# Handling Clear button click
	
	button2 = button(150, 580, 85, 25, "Submit")						# Creating Submit Button
	frame1.add_widget(button2)								# Adding it to frame1
	button2.click(OnClickSubmit)								# Handling Submit Button Click

	st1 = static_text(15, 15, "Name : ")							# Creating static text1
	frame1.add_widget(st1)									# Adding it to frame1

	st2 = static_text(15, 50, "Entry No : ")						# Creating static text2
	frame1.add_widget(st2)									# Adding it to frame1

	st3 = static_text(15, 85, "Year : ")							# Creating static text3
	frame1.add_widget(st3)									# Adding it to frame1
	
	st4 = static_text(15, 120, "Branch : ")							# Creating static text4
	frame1.add_widget(st4)									# Adding it to frame1
	
	st5 = static_text(15, 190, "Courses Added : ")						# Creating static text5
	frame1.add_widget(st5)									# Adding it to frame1
	
	st6 = static_text(15, 350, "Courses Dropped : ")					# Creating static text6
	frame1.add_widget(st6)									# Adding it to frame1
	
	year = ['1st year', '2nd year', '3rd year', '4th year', '5th year']			# List of entries in combo-box
	combo1 = drop_list(130, 85, 250, 25, year, "Please select a value", wx.CB_READONLY)	# Creating a Combo box
	frame1.add_widget(combo1)								# Adding it to frame1
	
	radioset1 = radio_button_set(wx.RB_GROUP)						# Creating a Radio Button Set1			
	radioset1.add_radio_button(130, 120, "Computer Science and Engineering")		# Adding entries
	radioset1.add_radio_button(130, 140, "Electrical Engineering")
	radioset1.add_radio_button(130, 160, "Mechanical Engineering")
	frame1.add_widget(radioset1)								# Adding it to frame1
	
	radioset2 = radio_button_set(wx.RB_GROUP)						# Creating a Radio Button Set2
	radioset2.add_radio_button(80, 540, "Approved")						# Adding entries
	radioset2.add_radio_button(210, 540, "Not Approved")
	frame1.add_widget(radioset2)								# Adding it to frame1
	radioset2.set_default(1)								# Default value
	
	chkboxset1 = check_box_set()								# Creating a Checkbox Set1
	chkboxset1.add_check_box(50, 220, "CSL 301 : Introduction to Databases")		# Adding entries
	chkboxset1.add_check_box(50, 245, "CSL 302 : Artificial Intelligence")
	chkboxset1.add_check_box(50, 270, "CSL 306 : Software Engineering")
	chkboxset1.add_check_box(50, 295, "CSL 468 : Special Topics in Computer Science")
	chkboxset1.add_check_box(50, 320, "MAL 212 : Modern Algebra")
	frame1.add_widget(chkboxset1)								# Adding it to frame1		
	
	chkboxset2 = check_box_set()								# Creating a Checkbox Set2
	chkboxset2.add_check_box(50, 380, "CSL 301 : Introduction to Databases")		# Adding entries
	chkboxset2.add_check_box(50, 405, "CSL 302 : Artificial Intelligence")
	chkboxset2.add_check_box(50, 430, "CSL 306 : Software Engineering")
	chkboxset2.add_check_box(50, 455, "CSL 468 : Special Topics in Computer Science")
	chkboxset2.add_check_box(50, 480, "MAL 212 : Modern Algebra")
	frame1.add_widget(chkboxset2)								# Adding it to frame1
	
	app.MainLoop()

