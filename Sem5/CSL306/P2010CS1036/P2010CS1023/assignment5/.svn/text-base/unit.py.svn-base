from anygui import anywx as g

           
#Functions bind to button events
def Submit(self):
    NewPstbps1 = NewPstb.get_text();
    print "Hello",NewPstbps1
    NewPstbps2 = ReNewPstb.get_text();
    if(Validate(NewPstbps1,NewPstbps2)):
        print (" Your Password Is Successfully Changed :)");
        #OldPstb.set_text("");
        #NewPstb.set_text("");
        #ReNewPstb.set_text("");
    else:
        print (" Please Enter Your Password Again !!!!!");
        #OldPstb.set_text("");
        #NewPstb.set_text("");
        #ReNewPstb.set_text("");
 




def Validate(NewPstbps1, NewPstbps2):
    if NewPstbps1 != NewPstbps2:
       print(" Error !!!!!  Passwords Don't Match! Please Enter Again. ")
       return False
    
    if(len(NewPstbps1)<=6):               # Check the length of the password
       print(" Error !!!!!  Length of the password should be more than 6. ")
       return False    
    
    if(str(NewPstbps1).isalnum()):             #checks if password conatins only alpha or numeric fiels
        
        if(str(NewPstbps1).isalpha()):          # invalidates if  password contains only alphabets not a combination.
            print(" Error !!!!!  Entered password containg only alphabets.Enter alphanumeric values")
            return False   
        
        elif(str(NewPstbps1).isdigit()):        #Invalidates if password contains only digits not a combination.
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
	
	
	usrtb=g.text_field()
	usrtb.pos=(20,20)
	usrtb.size=(100,20)
	usrtb.label="usrtb name"
	f.add(usrtb)
	
	
	OldPstb=g.text_field()
	OldPstb.pos=(20,50)
	OldPstb.size=(100,20)
	OldPstb.label="OldPstb password"
	f.add(OldPstb)
	
	NewPstb=g.text_field()
	NewPstb.pos=(20,80)
	NewPstb.size=(100,20)
	NewPstb.label="NewPstb password"
	f.add(NewPstb)
	
	ReNewPstb=g.text_field()
	ReNewPstb.pos=(20,110)
	ReNewPstb.size=(100,20)
	ReNewPstb.label="ReNewPstb NewPstb password"
	f.add(ReNewPstb)
	
	
	
	but=g.button()
	
	but.label="submit"
	
	but.onclick(Submit)
	f.add(but)
	
	f.show()

      



        
    



  
