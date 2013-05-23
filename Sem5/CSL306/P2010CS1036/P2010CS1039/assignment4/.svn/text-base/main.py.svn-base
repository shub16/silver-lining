import gtk
import sys
#import gtkapi
#import assignment4a as anygui1






#**********************************************************************************
#This is our main function

def Main():
    sampleProgram()
    
    
def sampleProgram():

    print " Enter Your Choice:  "
    print " 1 pyGTk GUI"
    print " 2 wXPYTHON GUI"
    print " 3 pyQt GUI"
    print " 4 tKINTER "
    print " 5 Exit "

    loop = 0
    #ensure whether a valid number is given
    while(loop == 0):           
        
        try:
            x = int(raw_input())
            loop = 1
        except ValueError:
            print 'Enter a valid number please'
            loop = 0
    
    #call PyGTk GUI output
    if x == 1:
        import santoshreddy_pygtk_assign4 as anygui
        

    #call FLTK GUI output
    elif x == 2:
        #pyFLTK_P2009CS1011.pyFLTK()
        import gauravsharma_wxpython_assign4 as anygui
        
    #call pyQT GUI output
    elif x == 3:
        #pyQT_P2009CS1027.PyQt()
        import gauravsaini_pyqt_assign4 as anygui
        
    #call tkinter GUI output
    elif x == 4:
       # tkinter_P2009CS1001.tkinter()
       import vikasmeena_tkinter_assign4 as anygui
       
    elif x == 5:
        print "bye"
        
    #exit
    else:
        print "Not a desired Number"

    #print "Exiting...."

    if x!=1 and x!=2 and x!=3 and x!=4:

        sys.exit(0)   

    #Functions bind to button events
	
    def SubmitButtonClick(event=None):
	
        report = " You are giving your review of the following dishes of "+ relist.getValue() +' in ' +valuelist.getValue()+".\n"
	
        if(checkbox1.getValue()):
	
            report = report + " Pizza\n"
	

    
	
        if(checkbox2.getValue()):
	
            report = report + " Cheese tomato\n"

        if(checkbox3.getValue()):
	
            report = report + " Chicken Tikka Butter Masala\n"
		
        if(checkbox4.getValue()):
	
            report = report + " Chana Masala\n"
	    
	
        report = report + " You felt food was---> "+rb1.getValue()+".\n"
        
        if(rb2.getValue()=='Not for me!'):
            report =report + "You would not revisit the Restaurant. \n"
        else:
            report =report + "You would love to have a visit again. \n"
	
    
	
        textarea.appendText("_______________________\n"+report+"\n\n")
	
        return True 
	
    
	
    def AboutButtonClick(event=None):
	
        textarea.setText("Created by qtGUI Author :\n")
	
        return True
	
    
	
    
	
    
	
    #Constructor Frame
	
    Frame = anygui.Canvas(1, 'Survey' ,800,500)
	
    
	
    
	
    #Dropdown valuelist
	
    cities = ['New Delhi', 'London', 'Ropar', 'Ludhiana', 'Chandigrah', 'Rome', 'Jaipur' ]
    restaurants = ['Mc Donalds','Pind Baluchi', 'KFC' , 'CCD']
	
    valuelist = anygui.ValueList(cities,10,10,130,30,"   Select city")
    relist = anygui.ValueList(restaurants,160,10,180,30,"   Select restaurant")
	
    Frame.add(valuelist)
    Frame.add(relist)
	
    
	
    #checkboxs
	
    checkbox1 = anygui.CheckBox("Pizza",10,45,215,15)
	
    checkbox2 = anygui.CheckBox("cheese tomato",10,65,235,15)
    checkbox3 = anygui.CheckBox("Chicken Tikka Butter Masala",10,85,235,15)
    checkbox4 = anygui.CheckBox("Chana Masala",10,105,235,15)
	
    checkbox1.setValue(True)
    #dishes  = Label('Dishes you like:',10,20,210,15)
    #Frame.add(dishes)
    Frame.add(checkbox1)
	
    Frame.add(checkbox2)
    Frame.add(checkbox3)
    Frame.add(checkbox4)
	
    
	
    #radioGroup1
	
    rb1 = anygui.RadioGroup(80,50)
	
    rb1.addRadioButton("Nice",10,130)
	
    rb1.addRadioButton("Good",90,130)
	
    rb1.addRadioButton("Great",170,130)
	
    rb1.setButtonTrue(2)
	
    Frame.add(rb1)
    #radioGroup2
    rb2 = anygui.RadioGroup(150,50)
    rb2.addRadioButton("Like to visit again!",10,170)
    rb2.addRadioButton("Not for me!",170,170)
    rb2.setButtonTrue(0)
    Frame.add(rb2)
    #TextArea
    textarea = anygui.TextArea("\n Click submit button to see output here!!",480,10,280,400)
    Frame.add(textarea)
    #Creating Buttons
    submitBtn = anygui.Button("Submit",130,460,120,30)
    aboutBtn = anygui.Button("About",260,460,120,30)
    #Callback methods on buttons click
    submitBtn.clickListener(SubmitButtonClick)
    aboutBtn.clickListener(AboutButtonClick)
    #Adding buttons to Frame
    Frame.add(aboutBtn)
    Frame.add(submitBtn)
    Frame.show()

        
    
        
if __name__ == '__main__':
    Main()




