import random
def ksmall(A,k):			# this function gives the kth smallest number in the list
		lower_array = []	# it contains the element lower than the random splitter selected 
		greater_array = []	# it contains the element greater than the random splitter selected
		n = len(A)-1
		random_index = random.randint(0,n)
		random_splitter = A[random_index]
		for i in range (0,n+1):
			if A[i]>random_splitter :
				greater_array.append(A[i])
			if A[i]<random_splitter :
				lower_array.append(A[i])
		if k>len(A)-len(greater_array):		
			i = len(A)-len(greater_array)
			return ksmall(greater_array,k-i)	# finds the kth smallest in the greater_array 
		if k<=len(lower_array):
			return ksmall(lower_array,k)		# finds the kth smallest in the lower_array 
		else:
			return random_splitter				# random_splitter is the kth smallest element 

def median(A):									# function to find the median							
	n=len(A)
	if n%2==0:
		return ksmall(A,n/2)					# finds the n/2 th element if n is even
	else:
		return ksmall(A,(n/2)+1)				# finds the (n/2)+1 th element if n is odd
