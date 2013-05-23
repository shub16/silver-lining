import OutputWindow as win

class Add:
	def __init__(self):
		print "\n--------------------------Welcome to CommonAPI------------------------------\n"
	
	def Start(self, width, height):
		self.Win = win.CommonAPI("My Window", width, height)
	
	def AskforPosition(self):
		xPos = raw_input("\tEnter x-pos:  ")
		yPos = raw_input("\tEnter y-pos:  ")
		return int(xPos), int(yPos)  
	
	def AskforLabel(self):
		label = raw_input("\tEnter label:  ")
		return str(label)
	
	def CreateButton(self, xPos, yPos):
		label = self.AskforLabel()
		self.Win.CreateButton(xPos, yPos, label)

	def ChooseSize(self):
		print "Select a Size for the Window:"
		width = raw_input("\tWidth--  ")
		width = int(width)
		height = raw_input("\tHeight--  ")
		height = int(height)
		self.Start(width, height)
	
	def ChooseWidget(self):
		print "**************************Choose a Widget.******************************\n \n\tEnter 'y' for yes and 'n' for no\n"
		List = ["Button", "RadioButton", "CheckBox", "TextBox", "List"]
		for item in List:
			select = raw_input("Add a "+item+" ?   ")
			select = str(select)
			if select == "y":
				xPos, yPos = self.AskforPosition()
				if item == "Button":
					self.CreateButton(xPos, yPos)
				elif item == "RadioButton":
					self.CreateRadioButton(xPos, yPos)
				elif item == "CheckBox":
					self.CreateCheckBox(xPos, yPos)
				elif item == "TextBox":
					self.CreateTextBox(xPos, yPos)
				else:
					self.CreateList(xPos, yPos)
				print "******************* "+ item + " has been created. **********************\n"
				return
			elif select == "n":
				continue
			else:
				print "Invalid character"
				return
		
	def CreateRadioButton(self, xPos, yPos):
		label = self.AskforLabel()
		self.Win.CreateRadioButton(xPos, yPos, label)
	
	def CreateCheckBox(self, xPos, yPos):
		label = self.AskforLabel()
		self.Win.CreateCheckBox(xPos, yPos, label)
	
	def CreateTextBox(self, xPos, yPos):
		self.Win.CreateTextBox(xPos, yPos)
	
	def CreateList(self, xPos, yPos):
		List = raw_input("Enter the list value:\n")
		List = List.split()
		self.Win.CreateList(xPos, yPos, List)
		
	def End(self):
		self.Win.Show()
		
		
	
def main():
	add = Add()
	add.ChooseSize()
	move = raw_input("\nEnter 'c' to continue and 'q'  to quit:   ")
	while str(move) == "c":
		add.ChooseWidget()
		move = raw_input("\nEnter 'c' to continue and 'q'  to quit:   ")
		print " "
	if str(move) == "q":
		add.End()
	else:
		print "Invalid input"

main()
