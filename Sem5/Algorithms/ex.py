import random
import math
import time
_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):  
    #assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
    	return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    #assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
        	#print "composite"
            return False
 
    return True # no base tested showed n as composite

if __name__ == '__main__':
      #n=int(raw_input(" Enter the no. to check for primality:  "))
      n=2
      for i in range(1,2203):
		n=n*2
      n=n-1
      #print n
      t1=time.time()
      z=  is_probable_prime(n)
      t2=time.time()
      print t2-t1	
      if (z== True):
		print "probably prime"	
      else:
		print "composite"

    
