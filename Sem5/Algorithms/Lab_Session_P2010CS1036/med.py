import random
import time
import math
import matplotlib.pyplot as plt
import median as m
def median(A):
	n=len(A)							# calculates the length of the list
	a=math.pow(n,0.75)
	s=int(math.ceil(a))
	r=[]
	half=n/2
	ld=0
	lu=0
	X=True
	x=math.sqrt(n)
	y=a/2
	p=int(math.floor(y-x))
	q=int(math.ceil(y+x))
	while X==True:
		i=0
		while i<s:						# chooses the n^(3/4) elements randomly from A and append into r
			rand=random.choice(range(0,n))
			r.append(A[rand])
			i=i+1
		r.sort()
		d=r[p-1]						# takes the (1/2)n^(3/4)-sqrt(n) element in r
		u=r[q-1]						# takes the (1/2)n^(3/4)+sqrt(n) element in r
		C=[]
		ld=0
		lu=0
		for i in A:					
			if(i<=u and i>=d):
				C.append(i)			# builds a list C for x belonging to A s.t. x is in between d and u 
			if(i<d):
				ld=ld+1				# counts the number of elements in A which are less than d
			if(i>u):
				lu=lu+1				# counts the number of elements in A which are greater than u
		if(ld > half or lu > half):
			X=True
			continue
		elif len(C)<= 4*a:
			C.sort()				# sort the list C if cardinality of set C is less than and equal to 4*n^(3/4)
			X=False
		else:
			X=True
			continue
	m=math.floor(half)-ld+1
	#print " The median is : ",m		# median is the floor(n/2)-ld+1 th element in C
tt1=[]
tt2=[]
p=[]
for j in range(1,11):
	list1=[]
	for i in range(0,j*1000):
		rand=(random.random(),random.random())
		list1.append(rand)
	t1=time.time()
	median(list1)
	t2=time.time()
	tt1.append(t2-t1)
	p.append(j*1000)
	n=len(list1)
	if n%2==0:
		t1=time.time()
		m.ksmall(list1,n/2)					# finds the n/2 th element if n is even
		t2=time.time()
		tt2.append(t2-t1)
	else:
		t1=time.time()
		m.ksmall(list1,(n/2)+1)
		t2=time.time()
		tt2.append(t2-t1)
plt.ylabel("Time taken")
plt.xlabel("No. of points")
plt.plot(p,tt1,label="New")
plt.plot(p,tt2,label="Old")
plt.legend()
plt.show()
