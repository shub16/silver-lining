
import tkMessageBox
import sys,os
import Tkinter as root
import Tkinter as tk
import time
import calendar

try:
    import Tkinter
    import tkFont
except ImportError: # py3k
    import tkinter as Tkinter
    import tkinter.font as tkFont

import ttk




class myWindow(object):
    window = None
    def __init__(self,title,X,Y,width,height):
        self.window = root.Tk()
        self.window.title(title)
        
        # get screen width and height
        #ws = self.window.winfo_screenwidth()
        #hs = self.window.winfo_screenheight()
        # calculate position x, y
        #x = (ws/2) - (width/2)    
        #y = (hs/2) - (height/2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, X, Y))
        
        
    def show(self):
        self.window.mainloop()
        return

        
''' WIDGETS: Button '''
class Button(object):
    controller = None
    callbackMethod = None
    Type = None
    def __init__(self,title,X,Y,width,height,cntrl):
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.controller = root.Button(frame, text=title,command= self.callbackMethod)
        self.controller.pack(fill=root.BOTH, expand=1)

    def buttonListener(self,method):
        self.controller.config(command=method)
        

''' WIDGETS: TextArea '''
class TextBox(object):
    controller = None
    callback = None
    Type = None
    def __init__(self,text,X,Y,width,height,cntrl):
        if(self.controller == None):
            self.text = text
        else:
            self.controller.delete(1.0, root.END)
            self.controller.insert(root.INSERT,text)
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.controller = root.Text(frame)
        self.controller.pack(fill=root.BOTH, expand=1)
        self.controller.insert(root.INSERT,text)

    def getText(self):
        if(self.controller == None):
            return self.text
        else:
            return self.controller.get(1.0, root.END)

    def setText(self,text):
        self.controller.delete(1.0, root.END)
        self.controller.insert(root.INSERT,text)


    def clear(self):
        self.controller.delete(1.0, root.END)
        return True


''' WIDGETS: Label '''
class Label(object):
    controller = None
    Type = None
    v=''
    label_var = 0
    def __init__(self,text,X,Y,width,height,cntrl):
        self.v=text
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.controller = root.Label(frame, text=self.v)
        self.controller.pack(fill=root.BOTH, expand=1)

    def setLabel(self,text):
        self.controller.config(text=text)















def get_calendar(locale, fwday):
    # instantiate proper calendar class
    if locale is None:
        return calendar.TextCalendar(fwday)
    else:
        return calendar.LocaleTextCalendar(fwday, locale)

class Calendar(ttk.Frame):
    # XXX ToDo: cget and configure

    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta

    def __init__(self, master=None, **kw):
        """
        WIDGET-SPECIFIC OPTIONS

            locale, firstweekday, year, month, selectbackground,
            selectforeground
        """
        # remove custom options from kw before initializating ttk.Frame
        fwday = kw.pop('firstweekday', calendar.MONDAY)
        year = kw.pop('year', self.datetime.now().year)
        month = kw.pop('month', self.datetime.now().month)
        locale = kw.pop('locale', None)
        sel_bg = kw.pop('selectbackground', '#ecffc4')
        sel_fg = kw.pop('selectforeground', '#05640e')

        self._date = self.datetime(year, month, 1)
        self._selection = None # no date selected

        ttk.Frame.__init__(self, master, **kw)

        self._cal = get_calendar(locale, fwday)

        self.__setup_styles()       # creates custom styles
        self.__place_widgets()      # pack/grid used widgets
        self.__config_calendar()    # adjust calendar columns and setup tags
        # configure a canvas, and proper bindings, for selecting dates
        self.__setup_selection(sel_bg, sel_fg)

        # store items ids, used for insertion later
        self._items = [self._calendar.insert('', 'end', values='')
                            for _ in range(6)]
        # insert dates in the currently empty calendar
        self._build_calendar()

        # set the minimal size for the widget
        self._calendar.bind('<Map>', self.__minsize)

    def __setitem__(self, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            self._canvas['background'] = value
        elif item == 'selectforeground':
            self._canvas.itemconfigure(self._canvas.text, item=value)
        else:
            ttk.Frame.__setitem__(self, item, value)

    def __getitem__(self, item):
        if item in ('year', 'month'):
            return getattr(self._date, item)
        elif item == 'selectbackground':
            return self._canvas['background']
        elif item == 'selectforeground':
            return self._canvas.itemcget(self._canvas.text, 'fill')
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(self, item)})
            return r[item]

    def __setup_styles(self):
        # custom ttk styles
        style = ttk.Style(self.master)
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(self):
        # header frame and its widgets
        hframe = ttk.Frame(self)
        lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
        rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
        self._header = ttk.Label(hframe, width=15, anchor='center')
        # the calendar
        self._calendar = ttk.Treeview(show='', selectmode='none', height=7)

        # pack the widgets
        hframe.pack(in_=self, side='top', pady=4, anchor='center')
        lbtn.grid(in_=hframe)
        self._header.grid(in_=hframe, column=1, row=0, padx=12)
        rbtn.grid(in_=hframe, column=2, row=0)
        self._calendar.pack(in_=self, expand=1, fill='both', side='bottom')

    def __config_calendar(self):
        cols = self._cal.formatweekheader(3).split()
        self._calendar['columns'] = cols
        self._calendar.tag_configure('header', background='grey90')
        self._calendar.insert('', 'end', values=cols, tag='header')
        # adjust its columns width
        font = tkFont.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            self._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                anchor='e')

    def __setup_selection(self, sel_bg, sel_fg):
        self._font = tkFont.Font()
        self._canvas = canvas = Tkinter.Canvas(self._calendar,
            background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

        canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
        self._calendar.bind('<Configure>', lambda evt: canvas.place_forget())
        self._calendar.bind('<ButtonPress-1>', self._pressed)

    def __minsize(self, evt):
        width, height = self._calendar.master.geometry().split('x')
        height = height[:height.index('+')]
        self._calendar.master.minsize(width, height)

    def _build_calendar(self):
        year, month = self._date.year, self._date.month


        # update header text (Month, YEAR)
        header = self._cal.formatmonthname(year, month, 0)
        self._header['text'] = header.title()

        # update calendar shown dates
        cal = self._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(self._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            self._calendar.item(item, values=fmt_week)

    def _show_selection(self, text, bbox):
        """Configure canvas for a new selection."""
        x, y, width, height = bbox

        textw = self._font.measure(text)

        canvas = self._canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width - textw, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=self._calendar, x=x, y=y)

    # Callbacks

    def _pressed(self, evt):
        """Clicked somewhere in the calendar."""
        x, y, widget = evt.x, evt.y, evt.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)

        if not column or not item in self._items:
            # clicked in the weekdays row or just outside the columns
            return

        item_values = widget.item(item)['values']
        if not len(item_values): # row is empty for this month
            return

        text = item_values[int(column[1]) - 1]
        if not text: # date is empty
            return

        bbox = widget.bbox(item, column)
        if not bbox: # calendar not visible yet
            return

        # update and then show selection
        text = '%02d' % text
        self._selection = (text, item, column)
        self._show_selection(text, bbox)

    def _prev_month(self):
        """Updated calendar to show the previous month."""
        self._canvas.place_forget()

        self._date = self._date - self.timedelta(days=1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstuct calendar

    def _next_month(self):
        """Update calendar to show the next month."""
        self._canvas.place_forget()

        year, month = self._date.year, self._date.month
        self._date = self._date + self.timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstruct calendar

    # Properties

    def getValue(self):
        """Return a datetime representing the current selected date."""
        if not self._selection:
            return None

        year, month = self._date.year, self._date.month
        return self.datetime(year, month, int(self._selection[0]))



















''' WIDGETS: CheckBox '''
class CheckBox(object):
    controller = None
    value = False
    Type = None
    def __init__(self,title,X,Y,width,height,cntrl):
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.value=root.IntVar()
        self.controller = root.Checkbutton(frame, text=title,variable=self.value)
        #widget.controller.pack(fill=root.BOTH, expand=1)
        self.controller.grid(sticky=root.W)

    def setCheckState(self,value):
        if(value):
            self.controller.select()
        else:
            self.controller.deselect()

    def getCheckState(self):
        if(self.value.get()== 1):
            return True
        else:
            return False

 
''' WIDGETS: RadioGroup '''
class ButtonGroup(object):
    controller = []
    cntrl = None
    selected_index = None
    
    def __init__(self,cntrl):
         self.cntrl = cntrl
           
    def addButtons(self,radiolist):
         for i in range(1,len(radiolist)):
               self.controller.append(radiolist[i])


    def setButtonTrue(self,index):
        button_controller = self.controller[index]
        button_controller.select()
globalvar=0

class RadioButton(object):
    controller = None
    labels=""
    def __init__(self,title,X,Y,width,height,cntrl):
	V=root.IntVar()
        V=0
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        global globalvar
        self.controller= root.Radiobutton(frame, text=title,variable=V,value=globalvar)
	globalvar=globalvar+1
        self.controller.pack(fill=root.BOTH, expand=1)
        self.controller.grid(sticky=root.W)
        self.labels=title



    def isChecked(self):
        for i in range(len(self.controller)):
            if(self.value.get()==i):
                return self.labels[i]
        return None

    def setChecked(self,index):
        button_controller = self.controller[index]
        button_controller.select()




''' WIDGETS: ValueList '''
class ComboBox(object):
    controller = None
    Type = None
    list_var = 0
    list_var = 1

    def __init__(self,title,value,X,Y,width,height,cntrl):
        array = ['']
        self.list_var = root.StringVar()
        self.list_var.set(value)
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.list_var1 = root.StringVar()
        array[0]=title
        array=array+value
        self.list_var1.set(array[0])

        self.controller = apply(root.OptionMenu, (frame, self.list_var1) + tuple(array))
        self.controller.pack(fill=root.BOTH, expand=1)


    def addItems(self,choices):
         self.controller.SetItems(choices)

    def Selected(self):
         return self.list_var1.get()

class PasswordBox:
    controller = None
    callback = None
    Type= "Password"
    def __init__(self,text,X,Y,width,height,cntrl):
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.controller = root.Entry(frame, show="*")
        self.controller.pack(fill=root.BOTH, expand=1)
        self.controller.insert(root.INSERT,text)

    def getText(self):
        return self.controller.get()

    def setText(self,text):
        self.controller.delete(1.0, root.END)
        self.controller.insert(root.INSERT,text)



class Slider:
    controller = None
    callback = None
    Type = "Slider"
    def __init__(self,X,Y,width,height,cntrl):
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.controller = root.Scale(frame, from_=0, to=10, orient=root.HORIZONTAL)
        self.controller.pack()
    def getValue(self):
        return self.controller.get()
    def setRange(self,a,b):
        self.controller.config(from_=a)
        self.controller.config(to=b)


class Cld:
    controller = None
    callback = None
    Type = "Slider"
    def __init__(self,X,Y,width,height,cntrl):
        frame = root.Frame(cntrl.window, width=width,height=height)
        frame.pack_propagate(0) # don't shrink
        frame.pack()
        frame.place(x=X,y=Y)
        self.controller = Calendar(frame,firstweekday=calendar.SUNDAY)
        self.controller.pack(expand=1, fill='both')
    def getValue(self):
        return self.controller.getValue()

    






def IsValidPswd(newps1, newps2):
    if newps1 != newps2:
       print(" Password Error !  Passwords donot match! ")
       return False
    
    if(len(newps1)<=6):               # Check the length of the password
       print(" Password Error ! Password Length should be more than 6. ")
       return False    
    
    if(str(newps1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        
        if(str(newps1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print(" Password Error ! Password cannot be only alphabet.Try combination! ")
            return False   
        
        elif(str(newps1).isdigit()):	    #Invalidates if password contains only digits not a combination.
            print(" Password Error ! Password cannot be only digit.Try combination! ")
            return False
        
        else :			                     
            print ("Password Successfully Changed. !");
            return True
    else:                                            # Invalidates if password have non-alphanumeric characters.
       print (" Password Error ! Password should contain only alphabets and digits.");
       return False











if __name__ == '__main__':

        def call_method():
            print ("\n Your Entered Data \n");
            print ("****************************\n")
            print ("Your Name :  "+ tb.getText());
         #   print ("Your Favourite Tool-Kit is :  "+rbgrp.getValue())
            if(ck1.getCheckState()==True):
			   print ("You Love Animals")
            if(ck2.getCheckState()==True):
               print("You Love Birds")
            print("Your Favourite Animal is : "+ ComboBox.Selected());
			
			
        def exit_method():
            print 'wxPython window made by Abhisaar Sharma'
            return
        
        
        WindowPanel = myWindow('wxPython Window By Abhisaar Sharma' ,50,50,750,600)
        
        #Labels
        nameLbl=Label("Your Name :",20,15,80,30,WindowPanel)
        toollbl=Label("Your Favourite Tool-Kit",15,100,140,40,WindowPanel)
        Listlbl=Label("Your Favourite Animal",280,30,160,60,WindowPanel)
        
        
        #Checkboxes
        ck1=CheckBox("I Love Animals ",20,45,150,50,WindowPanel)
        ck1.setCheckState(0)
        ck2=CheckBox("I Love Birds ",150,45,150,50,WindowPanel)
        ck2.setCheckState(2)
        
        
        
        #Radios
        rbgrp=ButtonGroup(WindowPanel)
        
        rb1=RadioButton("PyQT4",10,140,100,20,WindowPanel)
        rb2=RadioButton("Wx-Python",10,160,100,20,WindowPanel)
        rb3=RadioButton("PyGTK",10,180,100,20,WindowPanel)
        rb4=RadioButton("Tkinter",10,200,100,20,WindowPanel)
        
        rlist=[rb1,rb2,rb3,rb4]
        rbgrp.addButtons(rlist)
        
#        rb1.setChecked(True)
        
        #Textbox
        tb=TextBox("",100,15,150,30,WindowPanel)
        
        #Listbox
        myList=["Elephant","Peacock","Bear","Lion","Tiger","Leopard","Dog","Cat","Wolf","Spider","Parrot","Nightingale"]
        ComboBox=ComboBox("Animals",myList,250,80,150,30,WindowPanel)
   #     listBox.addItems(myList)
        
        #Buttons
        btn= Button("Print On Console",30,320,150,50,WindowPanel)
        btn.buttonListener(call_method)
        Exit_btn= Button("Info",260,320,150,50,WindowPanel)
        Exit_btn.buttonListener(exit_method)
        sld1=Slider(150,390,120,40,WindowPanel)
#        cal=Calendar(400,500,300,300,WindowPanel)
        pwd=PasswordBox('',300,390,120,20,WindowPanel)
        
        calend=Cld(450,290,220,240,WindowPanel)
        WindowPanel.show()

