import anytk4 as g
f=g.frame(1,"sample GUI Window",750,500)

user=g.text_field()
user.size=(100,50)
user.pos=(50,40)
lb1=g.static_text()
lb1.pos=(50,20)
lb1.size=(100,20)
lb1.label="Name"
f.append(lb1)
f.append(user)

user2=g.text_field()
user2.size=(100,50)
user2.pos=(50,120)

lb2=g.static_text()
lb2.pos=(50,100)
lb2.size=(100,20)
lb2.label="Entry Number"
f.append(lb2)
f.append(user2)

tbox=g.text_area()
tbox.pos=(300,40)
tbox.size=(400,130)
f.append(tbox)

def SubmitButtonClick():
	
        report = " Your favourite ice-cream is "+combo_box.get_value()+"\n"
        if(cb1.get_value()):
            report = report + " You hate exams.You are no exception\n"
        else:
            report = report + " You don't hate exams.\n"

        if(cb2.get_value()):
            report = report + " You want money.\n"
        else:
            report = report + " You don't want money.\n"

        report = report + " You are "+rb1.get_value()+"\n"
        

        tbox.append_text(report)
        return True 


lb3=g.static_text()
lb3.label="Hate Exams?"
lb4=g.static_text()
lb4.label="Want Money?"
lb4.pos=(50,250)
lb3.pos=(50,180)
cb1=g.check_box()
cb1.pos=(50,230)

cb1.label="tick me!"
cb2=g.check_box()
cb2.pos=(50,300)

cb2.label="tick me too!"
f.append(cb1)
f.append(lb4)
f.append(lb3)
f.append(cb2)

lb5=g.static_text()
lb5.pos=(300,190)
lb5.label=("How are you feeling today?")
lb5.size=(180,20)
f.append(lb5)

rb1 = g.radio_buttons()
rb1.size=(150,20)
rb1.add_rb("Awesome",300,230)
rb1.add_rb("On Cloud Nine",300,260)
rb1.add_rb("Lousy",300,290)
rb1.set_true(2)
f.append(rb1)
lb6=g.static_text()
lb6.pos=(500,190)
lb6.label=("Favourite Ice-Cream?")
lb6.size=(180,20)
f.append(lb6)


icecream = ['Butterscotch','Vanilla','Chocolate','Black Current' ]
combo_box = g.combo_box()
combo_box.size=(200,30)
combo_box.labels=icecream
combo_box.pos=(500,230)
combo_box.default="Strawberry"
f.append(combo_box)

button1=g.button()
button1.label="Submit"
button1.pos=(300,350)
button1.onclick(SubmitButtonClick)
f.append(button1)




f.show()
