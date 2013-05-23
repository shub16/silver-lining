#!/usr/bin/python 

import os
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from functools import partial

# function that gets called when the pushbutton is pressed
def pushButton(obj):

    # extract the values of the various widgets and perform some actions
    name = obj.tl.getValue()
    print "Username: %s" % name
    pwd = obj.ps.getValue()
    print "Password: %s" % pwd
    t1 = obj.rb.getValue()
    print "Gender: %s" % t1
    d = obj.cl.getValue()
    print "You selected the date: %s" % d
    t2 = obj.lv.getValue()
    print "Preferred GUI toolkit: %s" % t2
    fb = obj.tb.getValue()
    print "Your feedback:"
    print fb
    i = obj.sb.getValue()
    print "Rating from 0 to 5: %d" % i
    s = obj.s.getValue()
    print "Rating from 0 to 10: %d" % s
    if obj.cb.getValue():
    	print "That's great! Hope to see you again"
    else:
	print "I'm sorry. I will try to improve"    

# function to create all the widgets one by one and return a list of widgets
def createWidgets(obj):

    # this contains the list of all the widgets created in that order
    lstWidgets = []

    obj.lb = LabelWidget(obj, "Enter username:")
    lstWidgets.append(obj.lb.getWidget())

    obj.tl = TextLineWidget(obj)
    lstWidgets.append(obj.tl.getWidget())

    obj.plb = LabelWidget(obj, "Enter password:")
    lstWidgets.append(obj.plb.getWidget())

    obj.ps = PasswordWidget(obj)
    lstWidgets.append(obj.ps.getWidget())

    obj.rb = RadioButtonWidget(obj, ["Male", "Female"])
    for b in obj.rb.getWidget():
        lstWidgets.append(b)

    obj.cll = LabelWidget(obj, "Select your birthdate:")
    lstWidgets.append(obj.cll.getWidget())

    obj.cl = CalendarWidget(obj)
    for w in obj.cl.getWidget():
	lstWidgets.append(w)

    obj.lvl = LabelWidget(obj, "Select your preferred GUI toolkit:")
    lstWidgets.append(obj.lvl.getWidget())

    obj.lv = ListWidget(obj, ["PyQt", "Tkinter", "wxpython", "PyGTK"])
    lstWidgets.append(obj.lv.getWidget())

    obj.tbl = LabelWidget(obj, "Feedback about this window:")
    lstWidgets.append(obj.tbl.getWidget())

    obj.tb = TextBoxWidget(obj)
    lstWidgets.append(obj.tb.getWidget())

    obj.sbl = LabelWidget(obj, "Rate this window from 0 (very bad) to 5 (excellent):")
    lstWidgets.append(obj.sbl.getWidget())

    obj.sb = SpinBoxWidget(obj, 0, 5)
    lstWidgets.append(obj.sb.getWidget())

    obj.sl = LabelWidget(obj, "You can rate the window using this slider: mimimum - 0, maximum - 10:")
    lstWidgets.append(obj.sl.getWidget())

    obj.s = SliderWidget(obj, 0, 10)
    lstWidgets.append(obj.s.getWidget())

    obj.cb = CheckBoxWidget(obj, "I will use this application again")
    lstWidgets.append(obj.cb.getWidget())

    obj.bu = ButtonWidget(obj, "Done", partial(pushButton, obj))
    lstWidgets.append(obj.bu.getWidget())

    obj.cbu = ButtonWidget(obj, "Close", obj.close)
    lstWidgets.append(obj.cbu.getWidget())

    return lstWidgets
 
def main(): 
   
    root = QApplication(sys.argv)
    # creating an object of the class MyWindow
    obj = WindowLayout(root, 300, 400)
    obj.setWindowTitle('PyQt Application')
    # create all widgets
    lstWidgets = createWidgets(obj)
    # layout of the window 
    obj.createLayout(lstWidgets)       
    sys.exit(root.exec_())

###########################################################################################################

# class for the text line widget
class TextLineWidget(QWidget):

    # create the text line
    def __init__(self, parent):
	QWidget.__init__(self)
	self.widget = QLineEdit()

    # function to return the widget
    def getWidget(self):
	return self.widget
	
    # function to extract the value of the widget
    def getValue(self):
	val = self.widget.text()
	return val

# class for the text box widget
class TextBoxWidget(QWidget):

    # create the text box
    def __init__(self, parent):
	QWidget.__init__(self)
	self.widget = QTextEdit()

    # function to return the widget
    def getWidget(self):
	return self.widget
	
    # function to extract the value of the widget
    def getValue(self):
	val = self.widget.document().toPlainText()
	return val

# class for the push button widget
class ButtonWidget(QWidget):

    # create the push button
    def __init__(self, parent, name, function, *args):
	QWidget.__init__(self)
	self.widget = QPushButton(name, self)
	# call function when button in pressed
	self.widget.clicked.connect(partial(function, *args))

    # function to return the widget
    def getWidget(self):
	return self.widget

# class for the label widget
class LabelWidget(QWidget):

    # create the label
    def __init__(self, parent, title):
	QWidget.__init__(self)
	self.widget = QLabel(title)

    # function to return the widget
    def getWidget(self):
	return self.widget

# class for the password field widget
class PasswordWidget(QWidget):
    
    # create the password field
    def __init__(self, parent):
	QWidget.__init__(self)
	self.widget = QLineEdit()
	# replace characters with * in the password field
	self.widget.setEchoMode(2)

    # function to return the widget
    def getWidget(self):
	return self.widget

    # function to extract the value of the widget
    def getValue(self):
	val = self.widget.text()
	return val

# class for the spin box widget
class SpinBoxWidget(QWidget):

    # create the spin box
    def __init__(self, parent, fromvalue, tovalue):
	QWidget.__init__(self)
	self.widget = QSpinBox(self)
	self.widget.setMaximum(tovalue)
	self.widget.setMinimum(fromvalue)

    # function to return the widget
    def getWidget(self):
	return self.widget

    # function to extract the value of the widget
    def getValue(self):
	val = self.widget.value()
	return val

# class for the check box widget
class CheckBoxWidget(QWidget):

    # create the check box
    def __init__(self, parent, name):
	QWidget.__init__(self)
	self.widget = QCheckBox(name, self)

    # function to return the widget
    def getWidget(self):
	return self.widget

    # function to extract the value of the widget
    def getValue(self):
	if self.widget.isChecked():
	    return True
	else:
	    return False

# class for the radio button widget
class RadioButtonWidget(QWidget):

    # create the radio buttons
    def __init__(self, parent, labels):
	QWidget.__init__(self)
	# create a group of radio buttons
	self.rbg = QButtonGroup(self)
	self.widget = []
	n = 1
	for i in labels:
	    # create a list of all radio buttons within a group
	    self.widget.append(QRadioButton(i))
	    # add all radio buttons to the group
	    self.rbg.addButton(self.widget[n-1], n)
	    n = n + 1

    # function to return the widget
    def getWidget(self):
	return self.widget

    # function to extract the value of the widget
    def getValue(self):
	b = self.rbg.checkedButton()
	if b is None:
	    return ""
	t = b.text()
	return t

# class for the list widget
class ListWidget(QWidget):
    
    # create the list
    def __init__(self, parent, values):
	QWidget.__init__(self)
	self.widget = QListWidget(self)
	# add all the values to the list
	self.widget.addItems(values)

    # function to return the widget
    def getWidget(self):
	return self.widget

    # function to extract the value of the widget
    def getValue(self):
	i = self.widget.currentItem()
	if i is None:
	    return ""
	t = i.text()
	return t

# class for the slider widget
class SliderWidget(QWidget):

    # create the slider
    def __init__(self, parent, fromvalue, tovalue):
	QWidget.__init__(self)
	self.widget = QSlider(Qt.Horizontal, self)
	self.widget.setFocusPolicy(Qt.NoFocus)
	self.widget.setMinimum(fromvalue)
	self.widget.setMaximum(tovalue)

    # function to return the widget
    def getWidget(self):
	return self.widget

    # function to extract the value of the widget
    def getValue(self):
	return self.widget.value()

# class for the calendar widget
class CalendarWidget(QWidget):

    # create the calendar
    def __init__(self, parent):
	QWidget.__init__(self)
	self.widget = []
	self.widget.append(QCalendarWidget(self))
	self.widget[0].setGridVisible(True)

    # function to return the widget
    def getWidget(self):
	return self.widget

    # function to extract the value of the widget
    def getValue(self):
	return self.widget[0].selectedDate().toString()

# class for creating the layout
class WindowLayout(QWidget): 
    def __init__(self, parent, width, height): 
        QWidget.__init__(self)

    # function that takes in a list of widgets and places them in a grid layout and displays the window on screen
    def createLayout(self, lstWidgets):
	
	layout = QGridLayout(self)
	# list to hold the relative positions of the widgets
	arr = [1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1]
	i = 0
	# r and c are used for specifying the grid in which to place the widget
	r = 0		
        c = 0
	# place the first widget
	layout.addWidget(lstWidgets[0], r, c)
	for wgt in lstWidgets[1:]:
	    # for all the other widgets take the relative position from the list of relative positions
	    f = arr[i]
	    if f == 1:
       	        layout.addWidget(wgt, r, c+2, 2, 2)
		c = c + 2
	    else:
		c = 0
		layout.addWidget(wgt, r+2, c, 2, 2)
		r = r + 2
	    i= i + 1

        self.setLayout(layout)

	# show widget on screen
    	self.show()

if __name__ == "__main__": 
    main()
