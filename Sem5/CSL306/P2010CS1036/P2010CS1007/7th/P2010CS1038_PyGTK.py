''' This program demonstrates the library used in API '''


import pygtk
pygtk.require('2.0')
import gtk

class Statictext:
		def __init__(self,frame,text):
			self.widget=gtk.Label(text)
			self.widget.show()
		def set_text(self,text):
			self.widget.set_text(text)
			self.widget.show()
			
			
class Windows:
		def __init__(self,title,x,y,width,height):
			self.frame= gtk.Window(gtk.WINDOW_TOPLEVEL)	
			self.frame.connect("delete_event", lambda w,e: gtk.main_quit())	
			self.frame.set_title(title)
			self.frame.set_border_width(10)
			self.frame.set_default_size(width, height)
			self.frame.set_resizable(True)
			self.frame.move(x,y)
			
		def change_title(self,title):
			self.frame.set_title(title)
			return 
					
		def move_to_centre(self):
			self.frame.set_position(gtk.WIN_POS_CENTER_ALWAYS)
			return 
			
		def close_window(self):
			gtk.main_quit()	
		
		def change_color(self,color):
			color = gtk.gdk.color_parse(color)
			self.frame.modify_bg(gtk.STATE_NORMAL,color)
			
		def reset_color(self):
			self.frame.modify_bg(gtk.STATE_NORMAL,None)
				
		def show_window(self,box):	
			self.frame.add(box.widget)
			self.frame.show()	
			gtk.main()
			return			
				
class SingleTextBox:
		def __init__(self,frame,visibility):
			self.frm=frame
			self.widget=gtk.Entry(max=0)
			self.widget.set_text("")
			text=self.widget.get_text()
			
			if visibility==False:
				self.widget.set_visibility(False)
			elif visibility==True:
				self.widget.set_visibility(True)	
			
			self.widget.set_editable(True)
			self.widget.show()
		
		def set_text(self,text1):
			self.widget.set_text(text1)
			return
				
		def get_text(self):
			self.string=self.widget.get_text()
			return self.string
		
				
class MultiTextBox:			
		def __init__(self,frame):
			self.frm=frame
			self.string=gtk.TextBuffer()
			self.string.set_text("type text here")
			self.widget=gtk.TextView(self.string)
			self.widget.set_editable(True)
			self.widget.set_cursor_visible(True)
			self.widget.show()
			
		def set_text(self,text):
			self.widget.set_buffer(text)
			
		def get_text(self):
			str1=self.widget.get_buffer()
			return str1							
			
class button:
		def __init__(self,frame,Label):
			self.frm=frame
			self.widget=gtk.Button(label=Label)	
			self.widget.show()
			
		def bind(self,method,*args):
			if (method!=None and not args) or (method !=None and args[0]==None):
				self.widget.connect("clicked",method)
			elif (method!=None and args!=None):
				self.widget.connect("clicked",method,*args)
		
class ComboBox:
		def __init__(self,frame,name,list_Values):				
			self.frm=frame
			self.widget=gtk.combo_box_new_text()
			self.widget.append_text(name)
			for i in list_Values:
				self.widget.append_text(i)
			if name!=None:	
				self.widget.set_active(0)	
			self.widget.show()
	
		def get_value(self):
			item_text = self.widget.get_active_text()
			return item_text
		
class CheckBox:
		def __init__(self,frame, Label):					
			self.label=Label
			self.widget=gtk.CheckButton(self.label)
			self.frm=frame
			self.widget.show()			
			
		def bind(self,method,*args):
			if (method!=None and not args) or (method !=None and args[0]==None):
				self.widget.connect("toggled",method)
			elif (method!=None and args!=None):
				self.widget.connect("toggled",method,*args)
		
		def get_state(self):
			if self.widget.get_active():
				return True
			return False	
			
			
class RadioButtonList:
		def __init__(self,frame,Labels,ch1,ch2,st,grid,row):
			self.widget2=[]
			self.ch1=ch1
			self.ch2=ch2
			#self.grid=grid
			#self.row=row
			self.st=st.widget
			self.frame=frame
			self.b_labels=Labels
			self.Button1=gtk.RadioButton(None,None)
			self.widget2.append(self.Button1)
			#self.widget=gtk.VBox(False,2)
			for i in self.b_labels:
				self.b=gtk.RadioButton(self.Button1, i)
				#self.widget.pack_start(self.b,False,2)
				grid.widget.attach(self.b,0,1,row,row+1,xoptions=gtk.EXPAND|gtk.FILL, yoptions=gtk.EXPAND, xpadding=0, ypadding=0)
				row=row+1
				self.widget2.append(self.b)
				self.b.show()
				self.b.connect("toggled",self.toggle)
			#self.widget.show()			
				
		def toggle(self,label):
			count=-2
			if self.ch1==1:
				if(self.widget2[self.ch2].get_active()):
					print self.ch2-1,self.widget2[self.ch2-1]
					self.st.set_text("True")					
				else:
					self.st.set_text("False")
			else:
				for i in self.widget2:
					count=count+1
					if i.get_active():
						l="Your choice is:"
						self.st.set_text(l+self.b_labels[count])
					

class Alignment:
		def __init__(self,frame):
			self.widget=gtk.Table(10,5,False)
			
		def add(self,v,row,column,columnspan):
			self.widget.attach(v.widget,column,column+columnspan,row,row+1,xoptions=gtk.EXPAND|gtk.FILL, yoptions=gtk.EXPAND, xpadding=0, ypadding=0)
			self.widget.show()	
				

class App:
		def __init__(self):
			pass
		def loop(self):
			pass	
			


class SpinCtrl:
		def __init__(self, frame, val, minv, maxv):
			self.frm=frame
			self.adj1 = gtk.Adjustment(val, minv, maxv, 1.0, 0.1, 0.0)
			self.widget= gtk.SpinButton( self.adj1, 1.0, 0)			
			self.widget.set_wrap(True)
			#self.widget.set_value(val+20)
			self.widget.show()
									
		def get_value(self):	
			self.s=self.widget.get_value()
			return self.s

class Slider:
		def __init__(self, frame, val, minv, maxv):
			self.frm=frame
			self.adj1 = gtk.Adjustment(val, minv, maxv, 0.1, 0.1, 0.0)
			self.widget = gtk.HScale(self.adj1)
			self.widget.show()
		
		def get_value(self):
			self.s=self.widget.get_value()
			return self.s			
			
class ProgressBar:
		def __init__(self, frame, val, rang, width, height):			
			self.adj1 = gtk.Adjustment(val, 0.0, rang, 0.1, 0.1, 0.0)
			self.widget = gtk.ProgressBar(self.adj1)
			self.widget.set_size_request(width,height)
			self.widget.show()
			
		def set_value(self,val):
			self.widget.set_value(val)
			
			
			
		def get_value(self):
			self.s=self.widget.get_value()	
			return self.s

class image:
		def __init__(self,frame):					
			#self.b = gtk.gdk.pixbuf_new_from_file("index.jpeg")
			self.widget=gtk.Image()
			#self.widget.set_from_pixbuf(self.b)
			#self.widget.show()
			
		def set_image(self,path):
			self.pixbuf = gtk.gdk.pixbuf_new_from_file(path)
			self.widget.set_from_pixbuf(self.pixbuf)
			self.widget.show()
		
		
class FileDialog:
		def __init__(self,frame,text):
			self.frm=frame
			self.widget = gtk.FileChooserDialog(text,None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
gtk.STOCK_OPEN, gtk.RESPONSE_OK))
			self.widget.set_default_response(gtk.RESPONSE_OK)
			#self.widget.show()		
			
		def get_value(self):
			self.widget.show()
			filter = gtk.FileFilter()
			filter.set_name("All files")
			filter.add_pattern("*")
			self.widget.add_filter(filter)
			filter = gtk.FileFilter()
			filter.set_name("Images")
			filter.add_mime_type("image/png")
			filter.add_mime_type("image/jpeg")
			filter.add_mime_type("image/gif")
			filter.add_pattern("*.png")
			filter.add_pattern("*.jpg")
			filter.add_pattern("*.gif")
			filter.add_pattern("*.tif")
			filter.add_pattern("*.xpm")
			self.widget.add_filter(filter)

			response = self.widget.run()
			if response == gtk.RESPONSE_OK:
				path1=self.widget.get_filename()
			elif response == gtk.RESPONSE_CANCEL:
				print "Closed, no files selected"
			self.widget.destroy()
			return path1
								

'''			

#This is not part of library

if __name__ == "__main__":		
	def print_l(self,*args):
		self.b=args
		if self.b!=None:
			for i in self.b:
				print "The text in textbox is ",i.get_text()
	
	title="Sample"
	width=500
	height=500	
	frame=Windows(title,750,350,width,height)
	frame.change_title("hello world")
	
	tb1=MultiTextBox(frame)
	tb2=SingleTextBox(frame,True)
	st=Statictext(frame,"programming language")
	st.set_text("Which programming language you prefer?")

	cbx1=ComboBox(frame,"Select your choice:",["C","C++","Java","Python"])
	
	cb1=CheckBox(frame,"yahoo!")
	cb2=CheckBox(frame,"google!")
	
	def callback(event):	
		if(cb1.get_state()):
			frame.change_color('#CD7054')
		else:
			frame.reset_color()
				
	cb1.bind(callback)
	cb2.bind(callback)
	st2=Statictext(frame,"")
	st2.set_text("City in which you live:")
	grid1=Alignment(frame)
	
	btn=button(frame,"Submit")
	btn.bind(print_l,tb2)
	
	
	
	
	#grid1.add(tb1,1,1)
	grid1.add(tb2,0,0,1)
	grid1.add(btn,0,1,1)

	grid1.add(cb1,1,0,1)
	grid1.add(cb2,1,1,1)
	
	grid1.add(st,2,0,1)
	grid1.add(cbx1,3,0,2)
	grid1.add(st2,4,0,1)
	rb=RadioButtonList(frame,["Dehli","Mumbai","Chennai","Kolkata"],0,2,st2,grid1,5)
	#grid1.add(rb,7,1,2)
	
	frame.show_window(grid1)
'''
	

