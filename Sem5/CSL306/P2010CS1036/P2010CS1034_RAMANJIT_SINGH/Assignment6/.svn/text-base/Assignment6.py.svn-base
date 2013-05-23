#!/usr/bin/env python

from P2010CS1034_PyQt import *

#---------------------------------------------------------------------------------------
def main():
		app = App()

		new=Windows("PyQt",500,100,400, 380)
		grid=Alignment(new)
		new.btn3 = button(new,'OK')
		new.btn4 = button(new,'Cancel')
		new.btn4.bind(new.close_window)

		Label2={}
		Label2[0] = Statictext(new,"Name and Address :")
		Label2[1] = Statictext(new,"I am :")
		Label2[2] = Statictext(new,"Date of Birth :")

		new.nameLine2 = MultiTextBox(new)
		
		new.chb={}
		new.chb[0]=CheckBox(new,"I am a student.")
		new.chb[1]=CheckBox(new,"I am an employee.")
		new.chb[2]=CheckBox(new,"I like reading novels.")
		new.chb[3]=CheckBox(new,"I am addicted to the internet.")
		
		label3=Statictext(new,"")
	
		radio=RadioButtonList(new,['Male','Female'],0,2,label3,grid,4)

		list=("January" , "February", "March", "April", "May", "June" , "July", "August", "September", "October", "November", "December")
		new.cmb1=ComboBox(new,"Day",range(1,32))
		new.cmb2=ComboBox(new,"Month",list)
		new.cmb3=ComboBox(new,"Year",range(1940,2013))

		new.spinlabel = Statictext(new,"Spinbox :	")											# spinbox
		new.sp=SpinCtrl(new,5,-10,10)
	
		new.sliderlabel = Statictext(new,"Slider :	")										# Slider
		new.sl=Slider(new,5,-10,50)
		
		new.pbarlabel = Statictext(new,"Progress Bar :")									# Progress Bar
		new.pb=ProgressBar(new,10,100,300,25)
		
		grid.add(Label2[0],1,0,1)
		grid.add(new.nameLine2,2,0,5)
		grid.add(Label2[1],3,0,1)
		grid.add(label3,5,1,4)
		grid.add(Label2[2],6,0,1)
		grid.add(new.cmb1,7,2,1)
		grid.add(new.cmb2,7,3,1)
		grid.add(new.cmb3,7,4,1)
		grid.add(new.chb[0],8,0,4)
		grid.add(new.chb[1],9,0,4)
		grid.add(new.chb[2],10,0,4)
		grid.add(new.chb[3],11,0,4)
		grid.add(new.spinlabel,12,0,1)
		grid.add(new.sp,12,1,1)
		grid.add(new.sliderlabel,13,0,1)
		grid.add(new.sl,13,1,4)
		grid.add(new.pbarlabel,14,0,1)
		grid.add(new.pb,14,1,4)
		grid.add(new.btn3,16,3,1)
		grid.add(new.btn4,16,4,1)
		
		new.show_window(grid)
		app.loop()
            
if __name__ == '__main__':
    main()

