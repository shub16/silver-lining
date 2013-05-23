import sys
import time
		
if __name__ == '__main__':
	x=raw_input("Enter 1 for PyGTK, 2 for PyQT, 3 for WxPython, 4 for Tkinter : ")
	if x=='1':
		from P2010CS1038_PyGTK import *
	elif x=='2':
		from P2010CS1034_PyQt import *
	elif x=='3':
		from P2010CS1067_WxPython import *
	elif x=='4':
		from P2010CS1007_Tkinter import *	
	else:
		print "Please Enter a valid number."
		sys.exit()
	
	app =App()
	frame= Windows('What\'s up buddy!!!',250,250,900,600)
	
	
	v=Alignment(frame)
	
	img=image(frame)
	
	t1=SingleTextBox(frame,1)
																					
	but=button(frame,'Browse')
	
	v.add(t1,1,1,3)
	v.add(but,1,4,1)
	v.add(img,2,1,10)
	def onbrowse(event):
		#print 'onbrowse called'
		d=FileDialog(frame,'Choose a file')
		filepath=d.get_value()
		#print filepath
		t1.set_text(filepath)
		img.set_image(filepath)
	
	
	but.bind(onbrowse)
	
	
	
	
	
	'''img=Image(frame,'/home/nchy13/Desktop/qwe/dice.jpg')
	
	#v.add(img,0,0,1)
	
	
	slide=Slider(frame,10,1,60)
	
	but=button(frame,"selet duration of slide show")
	but1=button(frame,"Submit")
	prog=ProgressBar(frame,0,1,10,20)
	
	v.add(slide,1,1,1)
	v.add(but,2,1,1)
	v.add(prog,3,1,1)
	v.add(img,6,0,10)
	
	
	def duration(event):
		timer=slide.get_value()
		
		initial=time.time()
	
		for x in range(0,5):
			time.sleep(1)
			prog.set_value(x+1)
	
	paths=['/home/nchy13/Desktop/qwe/danger.jpg','/home/nchy13/Desktop/qwe/picture.jpg']
	
	
	
	def dur(*args):
		
		v.add(img,6,0,10)
		time.sleep(1)
		img.set_image(paths[i])
		print time.time()
		i=j
		i=i+1
		if((i-j)==2):
			return
		dur()
		
	
	but1.bind(dur)
			
	
	#img.set_image()
	
	#print img.widget.GetDepth
	#print img.widget.GetHeight
	

	#img.set_size(350,550)
	
	print img.depth
	print img.height
	
	sld=Slider(frame,175,150,500)
	sc=SpinCtrl(frame,0,-100,200)
	g=ProgressBar(frame,20,100,50,20)
	
	
	
	x=sld.get_val()
	print x
	y=sc.get_val()
	print y
	
	z=g.get_val()
	print z
	
	'''
	
	frame.show_window(v)
	
	app.loop()

