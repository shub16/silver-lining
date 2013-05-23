import anyqt as g

from math import *
#function to calculate the string
def OnBtnEqualButton( event):
        txt = text.get_text()
        # needs to contain a float so eg. 3/5 is 3/5.0
        # otherwise division 3/5 would result in zero
        if '/' in txt:
            if '.' not in txt:
                if 'sin' or 'cos' or 'tan' not in txt:
                        txt = txt + '.0'
        txt=str(txt)
        # now evaluate the math string
        txt = repr(eval(txt))
        # and show result in edit box
        text.set_text(txt)

def b0click(event):
        val = '0'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)


def b9click(event):
        val = '9'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)
        

def b8click(event):
        val = '8'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)


def b7click(event):
        val = '7'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)


def b6click(event):
        val = '6'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)


def b5click(event):
        val = '5'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)
        

def b4click(event):
        val = '4'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)


def b3click(event):
        val = '3'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)


def b2click(event):
        val = '2'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)
        
        

def b1click(event):
        val = '1'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)

def bpclick(event):
        val = '+'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)

def bsclick(event):
        val = '-'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)

def bdivclick(event):
        val = '/'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)

def bmulclick(event):
        val = '*'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)
        
def bdotclick(event):
        val = '.'
        # get existing text box text
        txt = text.get_text()
        # append text
        txt = txt + val
        # update text box text
        text.set_text(txt)

def bacclick(event):
        val = ''
        text.set_text(val)

f=g.frame(1,"calculator",510,400)
text=g.text_field()
text.pos=(20,10)
text.size=(480,40)
text.label=""
f.append(text)

#nums'

bac=g.button()
bac.label="AC"
bac.size=(80,60)
bac.pos=(300,60)	
bac.onclick(bacclick)
f.append(bac)


bmul=g.button()
bmul.label="x"
bmul.size=(60,60)
bmul.pos=(230,60)	
bmul.onclick(bmulclick)
f.append(bmul)

b9=g.button()
b9.label="9"
b9.size=(60,60)
b9.pos=(160,60)
b9.onclick(b9click)	
f.append(b9)	

b8=g.button()

b8.label="8"
b8.size=(60,60)
b8.pos=(90,60)	
b8.onclick(b8click)
f.append(b8)

b7=g.button()
b7.label="7"
b7.size=(60,60)
b7.pos=(20,60)	
b7.onclick(b7click)
f.append(b7)

bdiv=g.button()
bdiv.label="/"
bdiv.size=(60,60)
bdiv.pos=(230,120)	
bdiv.onclick(bdivclick)
f.append(bdiv)

b6=g.button()
b6.label="6"
b6.size=(60,60)
b6.pos=(160,120)	
b6.onclick(b6click)
f.append(b6)	

b5=g.button()
b5.label="5"
b5.size=(60,60)
b5.pos=(90,120)	
b5.onclick(b5click)
f.append(b5)

b4=g.button()
b4.label="4"
b4.size=(60,60)
b4.pos=(20,120)	
b4.onclick(b4click)
f.append(b4)


bp=g.button()
bp.label="+"
bp.size=(60,60)
bp.pos=(230,180)
bp.onclick(bpclick)	
f.append(bp)


b3=g.button()
b3.label="3"
b3.size=(60,60)
b3.pos=(160,180)
b3.onclick(b3click)	
f.append(b3)	

b2=g.button()
b2.label="2"
b2.size=(60,60)
b2.pos=(90,180)
b2.onclick(b2click)	
f.append(b2)

b1=g.button()
b1.label="1"
b1.size=(60,60)
b1.pos=(20,180)
b1.onclick(b1click)	
f.append(b1)

bs=g.button()
bs.label="-"
bs.size=(60,60)
bs.pos=(230,240)	
bs.onclick(bsclick)
f.append(bs)


b0=g.button()
b0.label="0"
b0.size=(60,60)
b0.pos=(160,240)	
b0.onclick(b0click)
f.append(b0)	

bdot=g.button()
bdot.label="."
bdot.size=(60,60)
bdot.pos=(90,240)	
bdot.onclick(bdotclick)
f.append(bdot)

be=g.button()
be.label="="
be.size=(60,60)
be.pos=(20,240)
be.onclick(OnBtnEqualButton)	
f.append(be)






f.show()
