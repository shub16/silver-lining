import random


def partition(A,key,start,end):
	pos=start
	temp=A[key]
	A[key]=A[start]
	start=start+1
	while True:
		while start <=end and A[start]<temp:
			start=start+1
		while start<=end and A[end]>=temp:
			end=end-1
		if end < start:
			break		
		if A[end]<=temp and A[start]>temp:
			t=A[end]
			A[end]=A[start]
			A[start]=t
			start=start+1
			end=end-1	
	A[pos]=A[end]
	A[end]=temp
	return end
					


def ksmall(A,k,start,end):
	
	print "Key",k,"Start",start,"End",end
	if(start<end):
		mykey=random.randint(start,end)
		#mykey = (start+end)/2
		print "Random Key", mykey,"Start",start,"End",end
		print "A Before" ,A
		x=partition(A,mykey,start,end)
		print "after partition" ,A
		print "X is",x , "K is",k
		if(x==k):
			print "x equals k",A[x]
			return
	
		if (k<x):
			ksmall(A,k,start,x-1)
		if (k>x):
			ksmall(A,k-x,x+1,end)
	else :
		print A[start]
			
	



A=[3,8,1,55,21,98,42,35,66,78]
k=5

ksmall(A,k-1,0,len(A)-1)




