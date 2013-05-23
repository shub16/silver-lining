import OutputWindow as out


def main():
	win = out.CommonAPI("Change Password", 400, 400)		
	T1 = win.CreateTextBox(200, 50 )
	T2 = win.CreateTextBox(200, 100, True)
	T3 = win.CreateTextBox(200, 150, True)
	T4 = win.CreateTextBox(200, 200, True)
	win.CreateLabel(50, 50, "Name")
	win.CreateLabel(50, 100, "Old Password")
	win.CreateLabel(50, 150, "New Password")
	win.CreateLabel(50, 200, "Confirm Password")
	button = win.CreateButton(200, 250, "Submit")
	button.connect("clicked", out.GetValues, [T1,T2,T3,T4] )
	win.Show()
	
main()
