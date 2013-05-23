#! /usr/bin/python

import sys
from PyQt4 import QtGui, QtCore
from functools import partial

class Label(QtGui.QLabel):

    def __init__(self, x, y, name, parent):
        super(Label, self).__init__(parent)
        self.setText(name)
        self.move(x,y)
        
class TextArea(QtGui.QTextEdit):

    def __init__(self,x, y, height, width, name, parent):
        super(TextArea, self).__init__(parent)
        self.setGeometry(x,y,width,height)

class TextLine(QtGui.QLineEdit):

    def __init__(self, x, y, height, width, mode, name, parent):
        super(TextLine, self).__init__(parent)
        
        if mode == "Normal" or mode =="normal":
            self.setEchoMode(self.Normal)
        elif mode == "Password" or mode =="password":
            self.setEchoMode(self.Password)
        elif mode == "NoEcho" or mode =="noecho":
            self.setEchoMode(self.NoEcho)
        elif mode == "PasswordEchoOnEdit":
            self.setEchoMode(self.PasswordEchoOnEdit)
            
        self.setGeometry(x,y,height,width)

    def setValue(self, text):
        self.setText(text)

    def getValue(self):
        text = self.text()
        return text
        

class Button(QtGui.QPushButton):

    def __init__(self, x, y, height, width, name, mode, parent):
        super(Button, self).__init__(name,parent)
        if mode == 1:
            self.setGeometry(x,y,height,width)
        if mode == 2:
            self.setCheckable(True)
            self.setChecked(True)
            self.setGeometry(x,y,height,width)
        if mode == 2:
            self.setFlat(True)
            self.setGeometry(x,y,height,width)
        else:
            self.setGeometry(x,y,height,width)

    def callback(self,method,List):
        self.clicked.connect(partial(method, List))

class CheckBox(QtGui.QCheckBox):
    
    def __init__(self, x, y, height, width, name, state, parent):
        super(CheckBox,self).__init__(name,parent)
        self.setChecked(state)  
        self.setGeometry(x,y,height,width)

    def clicked(self):
        self.stateChanged.connect(self.changeTitle)

    def triState(self, value):
        self.setTristate(value)

    def changeTitle(self, state):
        print 'change'
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('Check Box in use')
        else:
            self.setWindowTitle('Check Box not used')

class RadioButton(QtGui.QRadioButton):
    
    def __init__(self, x, y, height, width, name, parent):
        super(RadioButton,self).__init__(name,parent)
        self.setChecked(True)
        self.setGeometry(x,y,height,width)

    def changeText(self):
        print 'change'
        if self.isChecked():
            self.setWindowTitle('Radio Button on')
        else:
            self.setWindowTitle('Radio Button off')

class DropDownList(QtGui.QComboBox):

    def __init__(self, x, y, height, width, List, name, parent):
        super(DropDownList, self).__init__(parent)
        for i in List:
            self.addItem(i)
        self.setGeometry(x,y,height,width)

class Calendar(QtGui.QCalendarWidget):

    def __init__(self, x, y, parent, *args):
        super(Calendar,self).__init__(parent)
        self.setGridVisible(True)
        self.move(x,y)
        if len(args) == 2:
            self.resize(250,250)
        '''self.clicked[QtCore.QDate].connect(self.showDate)
        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)'''

    def showDate(self,date):
        self.lbl.setText(date.toString())

class Slider(QtGui.QSlider):
    
    def __init__(self, x, y, height, width, name, mode,minValue, maxValue, orientation, parent):
        super(Slider,self).__init__(parent)
        if orientation == "Horizontal" or orientation == "horizontal":
            self.setOrientation(QtCore.Qt.Horizontal)
        elif orientation == "Vertical" or orientation == "vertical":
            self.setOrientation(QtCore.Qt.Vertical)
        
        self.setRange(minValue, maxValue)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        if mode == 1:
            self.setTickPosition(self.NoTicks)
        elif mode == 2:
            self.setTickPosition(self.TicksBothSides)
        elif mode == 3:
            self.setTickPosition(self.TicksAbove)
        elif mode == 4:
            self.setTickPosition(self.TicksBelow)
        elif mode == 5:
            self.setTickPosition(self.TicksLeft)
        elif mode == 6:
            self.setTickPosition(self.TicksRight)
        else:
            self.setTickPosition(self.NoTicks)

        self.setGeometry(x,y,height,width)

    def setNumber(self,value):
        self.setValue(value)

    def getValue(self):
        value = self.value()
        return value

class SpinBox(QtGui.QSpinBox):
    def __init__(self,x,y,height,width,name,mode,parent):
        super(SpinBox,self).__init__(parent)

    def Range(self,minVal,maxVal):
        self.setRange(minVal,maxval)

    def setStep(self,step):
        self.setSingleStep(step)

    def Value(value):
        self.setValue(value)

class GroupBox(QtGui.QGroupBox):
    def __init__(self,x,y,height,width,name, parent):
        super(GroupBox,self).__init__(name,parent)
        #self.setGeometry(x,y,height,width)

    def setLayouts(self,layoutStyle,page, *widgets):
        if layoutStyle == "Vertical":
            layout = QtGui.QVBoxLayout(page)
        elif layoutStyle == "Horizontal":
            layout = QtGui.QHBoxLayout(page)
        else:
            layout = QtGui.QVBoxLayout(page)
        for widget in widgets:
            layout.addWidget(widget)
        self.setLayout(layout)

class TabPanel(QtGui.QTabWidget):
    def __init__(self,x,y,height,width,parent):
        super(TabPanel,self).__init__(parent)

    def addPage(self, page, pageName):
        self.addTab(page, pageName)

class Page(QtGui.QWidget):
    def __init__(self,x,y,height,widgth,label,parent):
        super(Page, self).__init__(parent)

    def setLayouts(self,group, *widgets):
        layout = QtGui.QVBoxLayout(self)
        for widget in widgets:
            layout.addWidget(widget)
        group.setLayout(layout)

    def setPage(self, *args):
        mainlayout = QtGui.QVBoxLayout(self)
        for widget in args:
            mainlayout.addWidget(widget)
        mainlayout.addStretch(1)           #SEE THIS LATER COMMENTED BECAUSE WE ARE USING ABSOLUTE POSITIONING
        self.setLayout(mainlayout)

class HorizontalLayout(QtGui.QHBoxLayout):
    def __init__(self,parent):
        super(HorizontalLayout,self).__init__(parent)

    def addWidgets(self, *args):
        for widget in args:
            self.addWidget(widget)

    def stretch(self, value):
        self.addStretch(value)

    def spacing(self, value):
        self.addSpacing(value)
        
    def AddLayout(self, layout):
        self.addLayout(layout)

class VerticalLayout(QtGui.QVBoxLayout):
    def __init__(self,parent):
        super(VerticalLayout,self).__init__(parent)

    def addWidgets(self, *args):
        self.addStretch(1)
        for widget in args:
            self.addWidget(widget)

    def stretch(self, value):
        self.addStretch(value)

    def spacing(self, value):
        self.addSpacing(value)
        
    def addLayouts(self, *layouts):
        for layout in layouts:
            self.addLayout(layout)

class Window(QtGui.QDialog):
    def __init__(self, height, width, title):
        self.app = QtGui.QApplication(sys.argv)
        super(Window, self).__init__()
        self.resize(height, width)
        self.setWindowTitle(title)
        self.center

    def center(self):
        qr = self.frameGeometry()                                   # Getting current window frame of my desktop
        cp = QtGui.QDesktopWidget().availableGeometry().center()    # Getting center point of my Desktop wiondow
        qr.moveCenter(cp)                                           # moving the center of the window to the cp
        self.move(qr.topLeft())

    def displayWindow(self,widget):
        ml = QtGui.QVBoxLayout(self)
        ml.addWidget(widget)
        self.setLayout(ml)
        self.show()
        sys.exit(self.app.exec_())
    
'''class Window(QtGui.QWidget):
    
    def __init__(self, x, y, height, width, title):
        self.app = QtGui.QApplication(sys.argv)
        super(Window, self).__init__()
        self.setGeometry(x, y, height, width)
        self.setWindowTitle(title)
        self.center

    def center(self):
        qr = self.frameGeometry()                                   # Getting current window frame of my desktop
        cp = QtGui.QDesktopWidget().availableGeometry().center()    # Getting center point of my Desktop wiondow
        qr.moveCenter(cp)                                           # moving the center of the window to the cp
        self.move(qr.topLeft())    

    def displayWindow(self):
        self.show()
        sys.exit(self.app.exec_())'''
