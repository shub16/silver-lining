from gtkGUI import*

           
#Functions bind to button events
def Submit(self):
    newps1 = NewPstb.getText();
    print "Hello",newps1
    newps2 = ReNewPstb.getText();
    if(validate(newps1,newps2)):
        #print ("Success !!! Password Successfully Changed !");
        OldPstb.setText("");
        NewPstb.setText("");
        ReNewPstb.setText("");
    else:
        print ("Retry by Entering new Password!  ");
        OldPstb.setText("");
        NewPstb.setText("");
        ReNewPstb.setText("");
 




def validate(newps1, newps2):
    if newps1 != newps2:
       print("\nError !!!!!  Passwords Don't Match! Please Enter Again. ")
       return False
    
    if(len(newps1)<=6):               # Check the length of the password
       print("\nError !!!!!  Length of the password should be more than 6. ")
       return False    
    
    if(str(newps1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        
        if(str(newps1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print("\nError !!!!!  Entered password containg only alphabets.Enter alphanumeric values")
            return False   
        
        elif(str(newps1).isdigit()):        #Invalidates if password contains only digits not a combination.
            print("\nError !!!!!  Entered password containg only numeral.Enter alphanumeric values")
            return False
        
        else :                                 
            #print ("Password Successfully Changed. !");
            print ("\nSuccess !!!  Password Successfully Changed !");
           # print (" Your Password Is Successfully Changed :)");
            return True
    else:                                            # Invalidates if password have non-alphanumeric characters.
       print ("\nError !!!!!  Special characters are not allowed.Enter only alphamueric values ");
       return False

#Constructor canvas

canvas = Main_Window(1, 'Change Password | Harmandeep_PyGtk' ,600,350)
userLbl =    LabelText("Username         ",10,40,120,30)
usrtb = TextField("",160,40,300,25)

canvas.add_widget(userLbl)
canvas.add_widget(usrtb)
OldPswdLbl = LabelText("Current Password ",20,100,120,30)
OldPstb= TextFieldPass("",160,100,300,25)

canvas.add_widget(OldPswdLbl)
canvas.add_widget(OldPstb)
NewPswdLbl = LabelText("New Password     ",20,160,120,30)
NewPstb= TextFieldPass("",160,160,300,25)
canvas.add_widget(NewPswdLbl)
canvas.add_widget(NewPstb)
label =      LabelText("ConfirmPassword   ",20,220,120,30)
ReNewPstb = TextFieldPass("",160,220,300,25)
canvas.add_widget(label)
canvas.add_widget(ReNewPstb)
btn= Button("Register",235,280,120,30)

btn.on_click(Submit)
canvas.add_widget(btn)

      
if __name__ == '__main__':
	canvas.show()


        
    



  
