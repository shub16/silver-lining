import sys

import P2009CS1003_Assignment4                                                            #importing my file


def main():

    Window = P2009CS1003_Assignment4.Widgets()                                                    #Creating object of my file
    
    window = Window.setWindow(700,700,700,700,"SB_Assignment_3")                               #initiating window                                      
    
    Window.createTextArea(100,10,500, 50,"Name")                                                 #Calling textbox function
    
    Window.createTextArea(100,70,500, 50,"Email")                                                #Calling textbox function   
    
    Window.createRadioButton(200,170,100,40,"Male")                                             #Calling radio button function

    Window.createRadioButton(400,170,100,40,"Female")                                           #Calling radio button function

    Window.createTextArea(100,250,500, 50,"Address")                                             #Calling textbox function

    country_list = ["-----Choose Country-----","INDIA","USA","RUSSIA","CHINA","JAPAN","SOUTH AFRICA"]

    droplist = Window.createDropDownList(100, 320, 500, 60,country_list, "Country")                  #Calling Drop down list function
    
    Window.createCheckBox(200,420,100,40,"Web Surfing")                                         #Calling checkbox function

    Window.createCheckBox(200,480,100,40,"Travelling")                                          #Calling checkbox function

    Window.createCheckBox(200,540,100,40,"Reading")                                             #Calling checkbox function

    Window.createButton(260,620,100,60,"Submit");                                               #Calling create button function
    
    Window.endWindow()                                                                     #Ending window
        
if __name__ == '__main__':
    main()                                                                                  #Calling main function
