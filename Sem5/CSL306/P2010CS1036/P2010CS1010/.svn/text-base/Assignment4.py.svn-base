#!/usr/bin/python

import pygtk
import gtk

Students = [('Bonani Hazarika', '2010CS1010', 'CSL_306'), ('Jaspreet Kaur', '2010CS1018', 'CSL_306'),
    ('Manisha Digra', '2010CS1021', 'CSL_306'), ('Manisha Dudi', '2010CS1022', 'CSL_306'),
    ('Tanvi Srivastava', '2010CS1082', 'CSL_306'), ('Neetu Soni', '2010CS1027', 'CSL_306' )]

class CommonAPI:
	#Creating Window
	def __init__ (self, Title, Length, Breadth):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title(Title)
		self.window.set_border_width(10)
		self.window.set_size_request(Length, Breadth)
		self.window.fixed = gtk.Fixed()
		#self.window.grid = gtk.Grid()
		self.radioButton1 = None
		#self.Show()
	
	#Creating Button		
	def CreateButton(self, xPos, yPos, Title ):
		button = gtk.Button( label = Title )
		self.window.fixed.put(button, xPos, yPos )
	
	#Creating Radio Button
	def CreateRadioButton(self, xPos, yPos, Title ):
		radioButton = gtk.RadioButton(self.radioButton1, Title)
		self.radioButton1 = radioButton
		self.window.fixed.put(radioButton, xPos, yPos )
	
	#Creating Check Box
	def CreateCheckBox(self, xPos, yPos, Title ):
		checkButton = gtk.CheckButton( label = Title )
		self.window.fixed.put(checkButton, xPos, yPos)
	
	#Creating Text Box
	def CreateTextBox(self, xPos, yPos):
		textField = gtk.Entry()
		self.window.fixed.put(textField, xPos, yPos)

	#Creating List
	def CreateList(self, xPos, yPos, List):
		store = self.CreateModel(List)
		self.treeView = gtk.TreeView(store)
		self.CreateColumns(self.treeView)
		self.window.fixed.put(self.treeView, xPos, yPos)

	#Creating Columns to add in List
	def CreateColumns(self, treeView):
		rendererText = gtk.CellRendererText()
        	column = gtk.TreeViewColumn("Name", rendererText, text=0)
        	column.set_sort_column_id(0)    
        	self.treeView.append_column(column)

	def CreateModel(self, Students):
        	store = gtk.ListStore(str, str, str)
        	for act in Students:
        		store.append([act[0], act[1], act[2]])
        	return store
		
	#The show function
	def Show(self):
		self.window.add(self.window.fixed)
		self.window.connect("delete-event", gtk.main_quit)
		self.window.show_all()
		gtk.main()

			
		
#The main function
if __name__ == "__main__":
        api = CommonAPI("A4", 500, 500)
        api.CreateButton(200,200,"Button")
        api.CreateCheckBox(10,80,"Red")
        api.CreateCheckBox(10,100,"Black")
        api.CreateRadioButton(80,80,"Blue")
        api.CreateRadioButton(80,100,"Green")
        api.CreateTextBox(100,20)
	api.CreateList(20, 130, Students)
        api.Show()
