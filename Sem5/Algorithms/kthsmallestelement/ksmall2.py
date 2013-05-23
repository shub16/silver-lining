import random



def Kthsmall(A,k,length):

        n = length-1
        rand = random.randint(0, length-1)
        piv = A[rand]
        print "Random Is :",piv
        A1 = []
        A2 = []
        for i in range (0,n+1):
                if A[i]<piv :
                        A1.append(A[i])
                        print "New List Is: ",A1
                if A[i]>piv :
                        A2.append(A[i])
                        print "New List Is: ",A2
        if k <= len(A1):
        	#print "Ok1"
                return Kthsmall(A1, k ,len(A1))
                
        if k > len(A) - len(A2):
        	#print "Ok2"
        	i = len(A) - len(A2)
                return Kthsmall(A2, k - i , len(A2))
                
        else :
        	#print "Ok3"
                return piv
 
A = (3,8,1,55,21,98,42,35,66,78)

length = len(A) 

Kth_Smallest = Kthsmall(A,10,length)

print "Kth Smallest is :: ",Kth_Smallest
