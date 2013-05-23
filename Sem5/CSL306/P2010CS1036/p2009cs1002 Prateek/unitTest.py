from AnyGUI.fltkGUI import *
import unittest
#xGUI(Environment = "fltk")

#Functions bind to button events
def SubmitButtonClick(event=None):  
    cost = 0
    final = "\n\n\n\n\nPIZZA CORNER\n\n"
    final = final + "\nPizza Size: " + rb1.getValue()
    final = final + "\nPizza Type: "
    if(checkbox1.getValue()):
        final = final + "Mushroom :"
    if(checkbox2.getValue()):
        final = final + "Paneer :"
    if(checkbox3.getValue()):
        final = final + "Onion: "
    if(checkbox4.getValue()):
        final = final + "Capsicum: "
    final = final + "\nCheese content: " + str(slidr.getValue())
    if(text_discount.getText() == "Group11"):
        final = final + "\nValid Discount Coupon : Yes"
    else:
        final = final + "\nValid Discount Coupon : No"

    final = final + "\n\n\nName: " + text_name.getText()
    final = final + "\nDelivery Address: " + text_address.getText()
    final = final + "\nContact number: " + text_phone.getText()

    #final = final + "\n\n\nTotal Cost: " + str(cost)
    final = final + "\nBank for Payment:" + valuelist.getValue()
    final = final + "\n\nThanks for ordering."


    dia.show(400,350,text_name.getText() + "Order" , final);


def AboutButtonClick(event = None):
    about = "\n\n\tIT'S A SEFTWARE PROJECT BY GROUP 11\n\nWE DON'T ORDER PIZZA's"
    dia2.show(400,300, "\n\n\tPizza Corner by Group 11" , about);

if __name__ == '__main__':
    #unittest.main()



    canvas = Canvas(1, 'AnyGUI -v1.7 | Group11_Pizza_Corner' ,900,600)

    label_heading = LabelText("Pizza Corner ", 300,20,100,100,50)
    label_ropar = LabelText("at IIT Ropar ", 600,30,150,30,20)
    canvas.add(label_heading)
    canvas.add(label_ropar)
    
    
    label_size = LabelText("Pizza Size ", 30,130,120,30,16)
    canvas.add(label_size)
    rb1 = RadioGroup(80,50)
    rb1.addRadioButton("Small",60,160)
    rb1.addRadioButton("Medium",60,190)
    rb1.addRadioButton("Large",60,220)
    rb1.setButtonTrue(2)
    canvas.add(rb1)

    label_type = LabelText("Choose the Topping ", 200,130,170,30,14)
    canvas.add(label_type)
    checkbox1 = CheckBox("Mushroom ",200,160,150,15)
    checkbox2 = CheckBox("Paneer",200,190,150,15)
    checkbox3 = CheckBox("Onion",200, 220,150,15)
    checkbox4 = CheckBox("Capsicum",200, 250,150,15)
    checkbox1.setValue(True)
    canvas.add(checkbox1)
    canvas.add(checkbox2)
    canvas.add(checkbox3)
    canvas.add(checkbox4)

    label_discount = LabelText("Dicount Coupon Number ",630,150,200,30,12)
    text_discount = TextField("",600,180,200,25)
    canvas.add(label_discount)
    canvas.add(text_discount)


    label_type = LabelText("Cheese content \n 50% being normal", 400,150,120,60,14)
    canvas.add(label_type)
    slidr = Slider("",400,200,150,30,0,100)
    canvas.add(slidr)


    label_name = LabelText("Name: ",30,350,120,30,12)
    text_name = TextField("Name: ",160,350,300,25)
    canvas.add(label_name)
    canvas.add(text_name)
	
    label_address = LabelText("Address for delivery: ",30,390,150,30,12)
    text_address = TextField("Address",160,390,300,25)
    canvas.add(label_address)
    canvas.add(text_address)

    label_phone = LabelText("Contact number ",30,430,120,30,12)
    text_phone = TextField("Contact number ",160,430,300,25)
    canvas.add(label_phone)
    canvas.add(text_phone)

    
    #radioGroup1
    
    
	
    cities = ['Citi Bank', 'State Bank of India', 'State Bank of Ropar', 'ICICI', 'Punjab National Bank', 'Canara Bank', 'HDFC' ]
    valuelist = ValueList(cities,600,320,200,20,"<Payment type>")
    canvas.add(valuelist)

    checkbox = CheckBox("WARNING: You are warned not to order pizza.", 100,500,400,60)
    canvas.add(checkbox)



    submitBtn = Button("ORDER",580,500,120,30)
    aboutBtn = Button("About us",720,500,120,30)



    dia = Dialog(text_name.getText() + "Order" ,"This is test dialog")
    dia2 = Dialog("Pizza Corner" ,"This is test dialog")
    
    #canvas.add(dia)
    #canvas.add(dia2)
    #Creating Buttons
	#submitBtn = Button("Submit",100,300,120,30)

    #Callback methods on buttons click
    submitBtn.clickListener(SubmitButtonClick)
    aboutBtn.clickListener(AboutButtonClick)
    #Adding buttons to canvas
    canvas.add(submitBtn)
    canvas.add(aboutBtn)

    canvas.show()
