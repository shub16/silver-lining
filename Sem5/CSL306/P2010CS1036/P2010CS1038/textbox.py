import pygtk
pygtk.require('2.0')
import gtk

choice=int(raw_input("Enter the choice:\n1 for running \"PyGTK\" code or 2 for running \"wxpython\" code or 3 for running \"tkinter\" code:"))
class TextBox:
	def enter_callback(auto, widget, entry):
		entry_text = entry.get_text()
		print "Entry contents: %s\n" % entry_text
	
	def close(auto, button):
		gtk.main_quit()
	#function for creating window
	def make_frame(auto, title, width, height):
		# a window with the given title
		frame = gtk.Window(gtk.WINDOW_TOPLEVEL)
		frame.set_title(title)
		
		frame.set_border_width(10)

		# setting the size of window and resize option
		frame.set_default_size(width, height)
		frame.set_resizable(True)
		return frame

	#function for adding textbox
	def make_tbox(auto,text):
		string=gtk.TextBuffer()
		string.set_text(text)
		#creats a text box
		txt=gtk.TextView(string)
		txt.set_cursor_visible(True)
		#function for editing the text
		txt.set_editable(True)
		txt.show()			
		return txt
		
	#function for making a button
	def make_button(auto, Label,method,*args):
		#creats the button with the given label
		button=gtk.Button(label=Label)
		
		button.show()
		button.connect("clicked",method, *args)
		return button
			
	#function for making radio buttons	
	def make_rbutton(auto, Labels):
		r_buttons=[]
		b_labels=Labels
		button1=gtk.RadioButton(None,None)
		button1.show()
		r_buttons.append(button1)
		for i in Labels:
			b=gtk.RadioButton(button1, i)
			b.set_border_width(5)
			r_buttons.append(b)
			b.show()
		return r_buttons	
	
	#funtion for adding value widgets to the window	
	def value_list(auto, list_Values, active):
		#creating an empty combo-box
		combo_box=gtk.combo_box_new_text()
		#adding list_Values in the combo box
		for i in list_Values:
			combo_box.append_text(i)
		if list_Values.count(active)>0:
			combo_box.set_active(list_Values.index(active))
		else:
			combo_box.set_active(-1)
		combo_box.show()
		return combo_box
	
		
	def print_l(auto,button,text):
		buf=text.get_buffer()
		#iterators used here to get the buffer into a string
		msg=buf.get_text(buf.get_start_iter(), buf.get_end_iter(), False)
		if msg!="":
			print "The text on the text box was \n", msg
		else:
			print "There was no text!\n"
			
	#function for making vertical box			
	def make_vbox(auto, Widgets_list):
		vbox=gtk.VBox(False,2)
		for i in Widgets_list:
			vbox.pack_start(i, True, False)
		vbox.show()
		return vbox
	
	def make_hbox(auto,Widgets_list):
		hbox = gtk.HBox(False, 0)
		for i in Widgets_list:
			hbox.pack_start(i, True, False)
		hbox.show()
		return hbox
		
	#function for adding checkboxes	
	def add_check_button(auto, Label, value):
		check_button=gtk.CheckButton(Label)
		check_button.set_active(value)
		check_button.show()
		return check_button	
	
	def make_changes(auto,button,check_button1, check_button2,frame,t_box):
		if check_button1.get_active():
			msg_buf=t_box.get_buffer()
			msg=msg_buf.get_text(msg_buf.get_start_iter(), msg_buf.get_end_iter(), False)
			frame.set_title(msg)
		else:
			if check_button2.get_active():
				frame.set_title("Yes")
				
	def add_label(auto, text):
		label=gtk.Label(text)
		label.set_alignment(0,1)
		label.show()
		return label
		
			
	def __init__(auto):
		l=[]
		title="Sample"
		width=500
		height=100
		frame=auto.make_frame(title,width,height);
		text="type text"
		txt=auto.make_tbox(text)
		button1_label="Ok"
		button1=auto.make_button( button1_label,auto.print_l, txt)			
		box1=auto.make_vbox([txt, button1])
		rbutton=auto.make_rbutton(["PyGTK", "PyGobject", "PyQT"])
		for i in rbutton:
			l.append(i)
		box2=auto.make_vbox(l)	
		check_button1=auto.add_check_button("Check text entered ", True)
		check_button2=auto.add_check_button("Is tool PyGTK", False)
		button2_label="Reflect Changes"
		button2=auto.make_button(button2_label,auto.make_changes,check_button1,check_button2,frame,txt) 
		box3=auto.make_hbox([check_button1,check_button2,button2])	
		box2.set_border_width(10)		
		label3=auto.add_label("Which programming domain you prefer?")
		list_box=auto.value_list(["Procedural","Object-oriented","Functional"],None)
		box4=auto.make_vbox([label3, list_box])
		button4_label="Close Window"
		button4=auto.make_button(button4_label,auto.close)	
		box5=auto.make_vbox([button4])
		box=auto.make_vbox([box1, box2, box3, box4,box5])
		frame.add(box)
		frame.show()
				
	def main(auto):
		gtk.main()
		return 0

if choice==1:
	entry=TextBox()
	entry.main()
elif choice==2:
	import module_wx
elif choice==3:
	import module_tkinter
else:	
	print("wrong choice")	
				