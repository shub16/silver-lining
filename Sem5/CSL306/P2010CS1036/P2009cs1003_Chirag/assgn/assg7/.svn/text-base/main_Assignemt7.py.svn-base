import guru as pyFltk_Assignment7

def main():

    dw = pyFltk_Assignment7.Window(500,400,"DEMO")
    tabWidget = pyFltk_Assignment7.TabPanel(1,1,500,400,dw)
    
    #TextLine & TextArea Page
    textline_page = pyFltk_Assignment7.Page(50,50,400,340,"AC",tabWidget)
    textline_group = pyFltk_Assignment7.GroupBox(80,80,320,270,"TextLine",textline_page)
    t1 = pyFltk_Assignment7.TextLine(200,130,150, 30,"Normal","Name",textline_page)
    t2 = pyFltk_Assignment7.TextLine(200,180,150, 30,"Password","Password",textline_page)
    l1=pyFltk_Assignment7.Label(30,130,"Name",textline_page)
    l2=pyFltk_Assignment7.Label(30,180,"Password",textline_page)
    
    textarea_group = pyFltk_Assignment7.GroupBox(100,250,280,70,"TextArea",textline_page)
    t3 = pyFltk_Assignment7.TextArea(200,280,150,30,"Address",textline_page)
    l3=pyFltk_Assignment7.Label(30,280,"Address",textline_page)
    textline_group.setLayouts("Vertical",textline_page,l1,t1,l2,t2)
    textarea_group.setLayouts("Vertical",textline_page,l3,t3)
    textline_page.setPage(textline_group,textarea_group)

    #CheckBox Page
    checkbox_page = pyFltk_Assignment7.Page(50,50,400,340,"AC",tabWidget)
    checkbox = pyFltk_Assignment7.GroupBox(80,80,320,220,"CheckBoxes",checkbox_page)
    c1 = pyFltk_Assignment7.CheckBox(150,150,100,50,"CheckBox1",False,checkbox_page)
    c2 = pyFltk_Assignment7.CheckBox(150,250,100,50,"CheckBox2",False,checkbox_page)

    checkbox_group = pyFltk_Assignment7.GroupBox(50,50,400,400,"Checked CheckBoxes", checkbox_page)
    c3 = pyFltk_Assignment7.CheckBox(150,100,100,100,"CheckBox1",True,checkbox_page)
    c4 = pyFltk_Assignment7.CheckBox(150,200,100,100,"CheckBox2",True,checkbox_page)

    checkbox.setLayouts("Vertical",checkbox_page,c1,c2)
    checkbox_group.setLayouts("Vertical",checkbox_page,c3,c4)
    checkbox_page.setPage(checkbox,checkbox_group)

    #Button Page
    button_page = pyFltk_Assignment7.Page(50,50,400,340,"Button",tabWidget)
    button_group = pyFltk_Assignment7.GroupBox(80,80,320,220,"Buttons",button_page)
    but1 = pyFltk_Assignment7.Button(150,100,150,50,"Normal Button",1,button_page)
    but2 = pyFltk_Assignment7.Button(150,170,150,50,"Return Button",2,button_page)
    but3 = pyFltk_Assignment7.Button(150,230,150,50,"Light Button",4,button_page)
    
    button_group.setLayouts("Vertical",button_page,but1,but2,but3) #Group Layout Setting
    button_page.setPage(button_group) #Page Layout Setting

    #DropDownList Page
    ddl_page = pyFltk_Assignment7.Page(50,50,400,340,"DropDownList",tabWidget)
    ddl_group = pyFltk_Assignment7.GroupBox(80,80,320,220,"DropDownList",ddl_page)
    List = ["INDIA","USA","RUSSIA","CHINA","JAPAN","SOUTH AFRICA"]
    ddl = pyFltk_Assignment7.DropDownList(200,150,150,40,List,"DropDownList",ddl_page)
    l4=pyFltk_Assignment7.Label(30,150,"Address",ddl_page)
    ddl_group.setLayouts("Vertical",ddl_page,l4,ddl)
    ddl_page.setPage(ddl_group)

    #Slider Page
    slider_page = pyFltk_Assignment7.Page(50,50,400,340,"Slider",tabWidget)
    slider_Hgroup = pyFltk_Assignment7.GroupBox(80,80,320,120,"Horizontal",ddl_page)
    slider1= pyFltk_Assignment7.Slider(150,95,200,20,"Naruto", 2, 0, 100, "Horizontal", slider_page)
    slider2= pyFltk_Assignment7.Slider(150,130,200,20,"Bleach", 3, 0, 200, "Horizontal", slider_page)
    slider3= pyFltk_Assignment7.Slider(150,165,200,20,"Death note", 1, 0, 150, "Horizontal", slider_page)
    slider_Hgroup.setLayouts("Vertical",slider_page,slider1,slider2,slider3)
    
    slider_Vgroup = pyFltk_Assignment7.GroupBox(80,220,320,150,"Vertical",ddl_page)
    slider4= pyFltk_Assignment7.Slider(120,240,20,100,"Code geass",4, 0, 100, "Vertical", slider_page)
    slider5= pyFltk_Assignment7.Slider(220,240,20,100,"Kenichi",5, 0, 100, "Vertical", slider_page)
    slider6= pyFltk_Assignment7.Slider(320,240,20,100,"Hitman Reborn",6, 0, 100, "Vertical", slider_page)    
    slider_Vgroup.setLayouts("Horizontal",slider_page,slider4,slider5,slider6)
    
    slider_page.setPage(slider_Hgroup,slider_Vgroup)

    #RadioButton Page
    radio_page = pyFltk_Assignment7.Page(50,50,400,340,"RadioButton",tabWidget)
    radio_group = pyFltk_Assignment7.GroupBox(80,80,320,300,"RadioButton",radio_page)
    rb1 = pyFltk_Assignment7.RadioButton(150,120,100,50,"Radio Button1",radio_page)
    rb2 = pyFltk_Assignment7.RadioButton(150,200,100,50,"Radio Button2",radio_page)
    rb3 = pyFltk_Assignment7.RadioButton(150,270,100,50,"Radio Button3",radio_page)

    radio_group.setLayouts("Vertical",radio_page,rb1,rb2,rb3)
    radio_page.setPage(radio_group)

    #SpinBox Page
    spinbox_page = pyFltk_Assignment7.Page(50,50,400,340,"SpinBox",tabWidget)
    spinbox_group = pyFltk_Assignment7.GroupBox(80,80,320,300,"SpinBox",spinbox_page)
    sb1 = pyFltk_Assignment7.SpinBox(110,150,230,50,"SpinBox",1,spinbox_page)
    sb2 = pyFltk_Assignment7.SpinBox(110,250,230,50,"SpinBox",2,spinbox_page)
    
    spinbox_group.setLayouts("Vertical",spinbox_page,sb1,sb2)
    spinbox_page.setPage(spinbox_group)

    
    tabWidget.addPage(checkbox_page,"CheckBox")
    tabWidget.addPage(textline_page,"TextLine")
    tabWidget.addPage(button_page,"Buttons")
    tabWidget.addPage(ddl_page,"DropDownList")
    tabWidget.addPage(slider_page,"Sliders")
    tabWidget.addPage(radio_page,"Radio Buttons")
    tabWidget.addPage(spinbox_page,"Spin Box")
    ''' Layout setting for main display '''
    dw.displayWindow(tabWidget)


if __name__ == '__main__':
    main()                                                                                      #Calling main function
