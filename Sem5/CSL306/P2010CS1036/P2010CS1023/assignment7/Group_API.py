-------------------------------------------------------------------

Group Members:-
Sunit Tanwar
Arjun Sunel
Manjeet Singh 
Abhishek Katiyar

-------------------------------------------------------------------

API Summary:-

-------------------------------------------------------------------

Class frame:
	
	def init(self)
	def __init__(self, id, title,width,height)
	def show(self)
	def append(self,widget)
	
Class static_text:
	
	static_text.pos=(X1,X2)
	static_text.size=(size[1],size[2])
	static_text.label="Label"
	def init(self)
	
Class button:
	
	button.pos=(x1,x2) 
	button.size=(size[1],size[2])
	button.label="Default String"
	
	def init(self)
	def onclick(self,method)
	
Class text_area:
	
	text_area.text="Default String"
	text_area.pos=(x1,x2)
	text_area.size=(size[1],size[2])
	
	def init(self)
	def set_text(self,text)
	def append_text(self,text)
	def clear(self)
	
Class text_field:
	text_field.label="Default String"
	text_field.pos=(x1,x2)
	text_field.size=(size[1],size[2])
	text_field.visibility=Boolean value
	
	def init(self)
	def set_text(self,text)
	def get_text(self)
	
Class check_box:
	check_box.label="Default String"
	check_box.pos=(x1,x2)
	check_box.size=(size[1],size[2])
	
	def init(self)
	def set_value(self,value)
	def get_value(self)
	
Class radio_buttons:
	
	def init(self)
	def add_rb(self,label,x,y)
	def get_value(self)
	def set_true(self,pos)
	
Class combo_box:
	
	combo_box.pos=(x,y)
	combo_box.size(size[1],size[2])
	combo_box.labels=[]
	def init(self)
	def get_value(self)

------------------------------------------------------------------------

For Documentation, refer to trac

------------------------------------------------------------------------
	
	
	
	
