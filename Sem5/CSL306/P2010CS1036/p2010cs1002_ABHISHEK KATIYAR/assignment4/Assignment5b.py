import anyqt as g

           
#Functions bind to button events
def Submit(self):
    user = User_Name.get_text();
    print "Hello",user
    New_Passps1 = New_Pass.get_text()
    New_Passps2 = ReNew_Pass.get_text();
    if(Validate(New_Passps1,New_Passps2)):
        print (" Your Password Is Successfully Changed :)");
        Old_Pass.set_text("");
        New_Pass.set_text("");
        ReNew_Pass.set_text("");
    else:
        print (" Please Enter Your Password Again !!!!!");
        Old_Pass.set_text("");
        New_Pass.set_text("");
        ReNew_Pass.set_text("");
 




def Validate(New_Passps1, New_Passps2):
    if New_Passps1 != New_Passps2:
       print(" Error !!!!!  Passwords Don't Match! Please Enter Again. ")
       return False
    
    if(len(New_Passps1)<=6):               # Check the length of the password
       print(" Error !!!!!  Length of the password should be more than 6. ")
       return False    
    
    if(str(New_Passps1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        
        if(str(New_Passps1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print(" Error !!!!!  Entered password containg only alphabets.Enter alphanumeric values")
            return False   
        
        elif(str(New_Passps1).isdigit()):        #Invalidates if password contains only digits not a combination.
            print(" Error !!!!!  Entered password containg only numeral.Enter alphanumeric values")
            return False
        
        else :                                 
            #print ("Password Successfully Changed. !");
            print (" Your Password Is Successfully Changed :)");
            return True
    else:                                            # Invalidates if password have non-alphanumeric characters.
       print (" Error !!!!! Special characters are not allowed.Enter only alphamueric values ");
       return False

#Constructor canvas

if __name__=='__main__':
	f=g.frame(1,"password checker",510,300)
	
	
	User_Name=g.text_field()
	User_Name.pos=(20,60)
	User_Name.size=(150,20)
	User_Name.label="User_Name"
	l1=g.static_text()
	l1.pos=(20,20)
	l1.label="User Name"
	
	f.append(l1)
	f.append(User_Name)
	
	
	Old_Pass=g.text_field2()
	Old_Pass.visibility=False
	Old_Pass.pos=(20,120)
	Old_Pass.size=(150,20)
	Old_Pass.label="Old_Pass password"
	l2=g.static_text()
	l2.pos=(20,80)
	l2.label="Old Password"
	f.append(l2)
	f.append(Old_Pass)
	
	New_Pass=g.text_field2()
	New_Pass.pos=(20,180)
	New_Pass.visibility=False
	New_Pass.size=(150,20)
	New_Pass.label="New_Pass password"
	l3=g.static_text()
	l3.pos=(20,140)
	l3.label="New Password"
	f.append(l3)
	f.append(New_Pass)
	
	ReNew_Pass=g.text_field2()
	ReNew_Pass.pos=(20,240)
	ReNew_Pass.visibility=False
	ReNew_Pass.size=(150,20)
	ReNew_Pass.label="ReNew_Pass New_Pass password"
	l4=g.static_text()
	l4.pos=(20,200)
	l4.label="Retype new password"
	l4.size=(150,20)
	f.append(l4)

	f.append(ReNew_Pass)
	
	
	
	but=g.button()
	
	but.label="submit"
	but.pos=(200,140)
	
	but.onclick(Submit)
	f.append(but)
	
	f.show()

      



        
    



  
