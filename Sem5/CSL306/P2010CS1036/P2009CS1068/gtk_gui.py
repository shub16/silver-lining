#!/usr/bin/python 

import pygtk
pygtk.require('2.0')
import gtk

class SpinBoxWidget:
	"""Class for the spin button widget."""
	
	def __init__(self, parent, fromValue, toValue):
		"""Constructor."""
		displayDigits=3
		incrementSize=1
		adjustment=gtk.Adjustment(value=fromValue, lower=fromValue, upper=toValue, step_incr=incrementSize, page_incr=incrementSize)
		self.spinButton=gtk.SpinButton(adjustment, incrementSize, displayDigits)
		self.spinButton.set_range(fromValue, toValue)
		self.spinButton.set_update_policy(gtk.UPDATE_IF_VALID)
		self.spinButton.set_wrap(False)
		self.spinButton.set_snap_to_ticks(True)
		self.show()
		
	def getValue(self):
		return self.spinButton.get_value()
	
	def setValue(self, value):
		self.spinButton.set_value(value)
	
	def show(self):
		self.spinButton.show()
	
	def getWidget(self):
		return self.spinButton

class SliderWidget:
	"""Class for the horizontal scale widget."""	
	
	def __init__(self, parent, fromValue, toValue):
		"""Constructor."""
		incrementSize=1
		adjustment=gtk.Adjustment(value=fromValue, lower=fromValue, upper=toValue, step_incr=incrementSize, page_incr=incrementSize)
		self.scale=gtk.HScale(adjustment)
		self.scale.set_digits(2)
		self.show()

	def getValue(self):
		self.scale.get_value()

	def setValue(self, value):
		self.scale.set_value(value)

	def show(self):
		self.scale.show()

	def getWidget(self):
		return self.scale

class CalendarWidget:
	"""Class for the calendar widget."""
	
	def __init__(self, parent):
		"""Constructor."""
		self.cal=gtk.Calendar()
		self.cal.set_display_options(gtk.CALENDAR_SHOW_HEADING) 
		self.cal.set_display_options(gtk.CALENDAR_SHOW_DAY_NAMES)
		self.cal.set_display_options(gtk.CALENDAR_SHOW_WEEK_NUMBERS)
		self.show()

	def getValue(self):
		self.cal.get_date()

	def setValue(self, year, month, date):
		self.cal.select_month(month, year)
		self.cal.select_day(date)

	def show(self):
		self.cal.show()

	def getWidget(self):
		l=[]
	        l.append(self.cal)
	        return l

class TextLineWidget:
	"""Class for a single text line widget."""
	
	def __init__(self, parent):
		"""Constructor."""
		self.txtLine=gtk.Entry()
		self.show()
	
	def getValue(self):
		return self.txtLine.get_text()

	def setValue(self, text):
		self.txtLine.set_text(text)

	def show(self):
		self.txtLine.show()

	def getWidget(self):
		return self.txtLine

class TextBoxWidget:
	"""Class for the text box widget."""

	def __init__(self, parent):
		"""Constructor."""
		self.txtBox=gtk.TextView(None)
		self.txtBox.set_wrap_mode(gtk.WRAP_WORD_CHAR)
		self.txtBox.set_cursor_visible(True)
		self.txtBox.set_editable(True)
		self.show()
	
	def getValue(self):
		buf=self.txtBox.get_buffer()
		return buf.get_text(buf.get_start_iter(), buf.get_end_iter(), False)
	
	def setValue(self, text):
		buf=self.txtBox.get_buffer()
		buf.set_text(text)
	
	def show(self):
		self.txtBox.show()
	
	def getWidget(self):
		return self.txtBox

class LabelWidget:
	"""Class for the Label Widget."""

	def __init__(self, parent, text):
		"""Constructor."""		
		self.label=gtk.Label(text)
		self.label.set_alignment(0,0)
		self.show()
		
	def getValue(self):
		return self.label.get_text()
		
	def setValue(text):
		self.label.set_label(text)
	
	def show(self):
		self.label.show()
	
	def getWidget(self):
		return self.label
		
class PasswordFieldWidget:
	"""Class for the password fields that require encryption."""
	
	def __init__(self, parent):
		"""Constructor."""
		self.pwdField=gtk.Entry(0)
		self.pwdField.set_visibility(False)
		self.show()
		
	def getValue(self):
		return self.pwdField.get_text()
	
	def setValue(self, password):
		self.pwdField.set_text(password)
		
	def show(self):
		self.pwdField.show()
	
	def getWidget(self):
		return self.pwdField
		
class ButtonWidget:
	"""Class for Button widget."""
	
	def __init__(self, parent, name, function, *args):
		"""Constructor."""
		self.btn=gtk.Button(label=name)
		self.btn.connect("clicked", function, *args)
		self.show()
		
	def show(self):
		self.btn.show()
	
	def getWidget(self):
		return self.btn

class CheckBoxWidget:
	"""Class for check box widget."""
	
	def __init__(self, parent, name, varname):
		"""Constructor."""
		self.cBox=gtk.CheckButton(name)
		self.show()

	def getValue(self):
		return self.cBox.get_active()

	def setValue(self,is_active):
		self.cBox.set_active(is_active)
	
	def show(self):
		self.cBox.show()
	
	def getWidget(self):
		return self.cBox

class RadioButtonWidget:
	"""Class for radio button widget."""
	
	def __init__(self, parent, labels, varname):
		"""Constructor."""
		bLabels=labels
	#	The list of radio buttons
		self.rButtons=[]
	#	Creating the first radio button with the 'group' parameter as 'None' and adding it to the list
		b1=gtk.RadioButton(None, bLabels.pop(0))
		self.rButtons.append(b1)
	#	Creating the rest of radio buttons with the 'group' parameter as the first radio button and adding them to the list
		for i in labels:
			b=gtk.RadioButton(None, i)
			b.set_group(b1)
			self.rButtons.append(b)
		self.show()
	
	def show(self):
		for b in self.rButtons:
			b.show()
	
	def getValue(self):
		for b in self.rButtons:
			if(b.get_active()):
				return b.get_label()
	
	def setValue(self, value):
		for b in self.rButtons:
			if b.get_label()==value:
				b.set_active(True)
	
	def getWidget(self):
		return self.rButtons
				
class ListWidget:
	"""Class for list value widget."""
	
	def __init__(self, parent, values):
		"""Constructor."""
		self.listBox=gtk.combo_box_new_text()
		for i in values:
			self.listBox.append_text(i)
		self.show()

	def show(self):
		self.listBox.show()				
			
	def getValue(self):
		return self.listBox.get_active_text()
	
	def getWidget(self):
		return self.listBox
	
class WindowLayout:
	"""Class for creating the window, box etc. and setting the layout of the window."""
	
	def __init__(self, parent, width, height):
		"""Constructor."""
		title="PyGTK Application"
		self.window=self.createWindow(title, width, height)
		
	def createWindow(self, Title, width, height):
		"""This function creates and returns a window widget with the given title and dimensions and sets some default features."""
	
	#	creating a window with the given title
		window=gtk.Window(gtk.WINDOW_TOPLEVEL)		
		window.set_title(Title)

	#	setting the position of the window to be at the centre, even if resized
		window.set_position(gtk.WIN_POS_CENTER_ALWAYS)

	#	setting the size of window and allowing it to be resized
		window.set_default_size(width, height)
		window.set_resizable(True)
		
	#	setting the features
		window.set_decorated(True)
		window.set_deletable(True)
		
		return window
	
#	def createVbox(self, Widgets_list, space):
#		"""This function creates and returns a vertical box widget and puts the widgets in the given list with the specified spacing in the box."""
	
	#	Creating the vertical box widget
#		box=gtk.VBox(False, space)
		
	#	Set the spacing
#		box.set_spacing(space)
	
	#	Pack the widgets in the box
#		for i in Widgets_list:
#			box.pack_start(i, False, False, space)
		
#		box.show()
		
#		return box
		
#	def createHbox(self, Widgets_list, space):
#		"""This function creates and returns a horizontal box widget and puts the widgets in the given list with the specified spacing in the box."""
	
	#	Creating the horizontal box widget
#		box=gtk.HBox(False, space)
		
	#	Set the spacing
#		box.set_spacing(space)
	
	#	Pack the widgets in the box
#		for i in Widgets_list:
#			box.pack_start(i, False, False, space)
		
#		box.show()
		
#		return box	

	
#	def createCompoundButton(self, name, image, width, height, function, *args):
#		"""This functions creates a compund button with an image and text on the button."""
#		img=gtk.Image()
#		imgBuf=gtk.gdk.pixbuf_new_from_file_at_size(image, width, height)
#		img.set_from_pixbuf(imgBuf)
#		img.show()

#		label=gtk.Label(name)
#		label.show()

#		box=gtk.HBox()
#		box.pack_start(img)
#		box.pack_start(label)
#		box.show()

#		button=gtk.Button()
#		button.add(box)
#		button.connect("clicked", function, *args)
#		button.show()

#		return button
		
#	def createHSeparator(self):
#		"""This function creates and returns a horizontal separator widget."""
	
	#	Create the separator
#		separator=gtk.HSeparator()
#		separator.show()
		
#		return separator

	def createLayout(self, lstWidgets):
		"""This function defines the layout of the window as desired by user and add the widgets to the window."""
		
	#	spacing parameter for the packing of boxes
		space=3
	
	#	A vertical box to put in the final window. all other boxes are packed in this box
		Vbox=gtk.VBox(False, space)
		Vbox.set_spacing(space)	

	#	The widgets are added to the horizontal boxes based on whether they are present in the same or in the next line
		Hbox=gtk.HBox(False, space)
		Hbox.set_spacing(space)	
	
	#	Pack the first widget in the first horizontal box
		Hbox.pack_start(lstWidgets[0], True, True, space)
		
	#	For all the widgets, ask the user where to place and then create a new horizontal box if needed and add the previous ones to the vertical box
		for wgt in lstWidgets[1:]:
			f = int( raw_input( "Where do you want the next widget?\nSame line(1)\nNext line(2)\n" ) )
			
			if f == 1:
				Hbox.pack_start(wgt, True, True, space)
			
			else:
				Vbox.pack_start(Hbox, True, True, space)
				Hbox.show()
				Hbox=gtk.HBox(False, space)
				Hbox.set_spacing(space)	
				Hbox.pack_start(wgt, True, True, space)
	
	#	Add the final box to the vertical box
		Vbox.pack_start(Hbox, True, True, space)
		Hbox.show()
	
		Vbox.show()
	
	#	Add the vertical box to the window and display the window
		self.window.add(Vbox)
		self.window.show()
		gtk.main()

def setup():
	root=None
	return root
