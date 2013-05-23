import pyFltk_API as modul

# To return result of "validate" method along with different attributes
class Result() :
    def  __init__(self) :
        pass

# Return true, if both passwords are equal & matches the criteria
def if_valid_pwd(new_password1, new_password2):
    result = Result()                                                         # result object to hold Result of validate method
    result.match = None
    if isinstance(new_password1, str) and isinstance(new_password2, str) :    # check, whether password is string or not
        pass
    else :
        raise TypeError("argument should be strings")                         
     
    if len(new_password1)==0 or len(new_password2) == 0:                      # If passwords are empty
        result.text, result.value = "Please Enter Both the passwords ", False
        return result
    
    if new_password1 != new_password2 :                                       # Whether, both passwords are same or not
        result.text, result.value = "Passwords don't matches", False
        return result
    else:
        result.value = False                                                  # False means, passwords doesn't satisfy criteria yet
        alpha = False                                                         # if password has alphabet character
        numeric = False                                                       # if password has numeric character
        no_char = 0                                                           # No. of characters in password
        for c in new_password1 :
            if not result.value :
                if (c >= 'a' and c <='z') or (c >= 'A' and c <='Z') :         # 'c' is an alphabet
                    alpha = True
                elif c >= '0' and c <= '9' :                                  # 'c' is a number
                    numeric = True
                no_char = no_char + 1
                result.value = numeric and alpha and ( no_char>6 )
            else :                                                          
                break                                                         # Now, password is validated 
        if result.value :
            result.text = "Passwords matches & satisfy the criteria :)  \n"
        else :
            result.text = "Passwords matches,\nBut!!!, Don't satisfy the criteria \n"
        
    return result
    
# Customizes "change password" button callback function & show the dialog
def change_pwd_action_listener(widget, pwd) :
    result = if_valid_pwd(pwd[0].getValue(), pwd[1].getValue())
    modul.py_dialog(result.text)                                               # Show result in a dialog
    return

# Application to change password
class Pwd_Application():
    def __init__(self) :
        self.win = modul.Py_Window( 600, 400, " Registration Form ")
        self.win.name = modul.Py_Input( 160, 40, 250, 30, "Name : ",'N' )
        self.win.old_pwd = modul.Py_Input(160, 80, 250, 30, "Old Password : " ,'S')
        self.win.pwd = []
        self.win.pwd.append( modul.Py_Input( 160, 120, 250, 30, "New Password : " ) )
        self.win.pwd.append( modul.Py_Input( 160, 160, 250, 30, "New Password : " ) )
        self.win.change_btn = modul.Py_Button( 200, 300, 140, 60, "Change password")
        self.win.change_btn.action_listener(change_pwd_action_listener, self.win.pwd)
        self.win.finish()
        modul.run_app()
        
if __name__ == '__main__':
    Pwd_Application()