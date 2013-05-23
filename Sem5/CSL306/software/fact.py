def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return n*fact(n-1)
t=input()
a=[]
for i in range(0,t):
	#a.append(input())
	print fact(input())
	#yield
#for i in range(0,t):
#	print fact(a[i])
