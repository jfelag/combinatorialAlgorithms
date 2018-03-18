'''
COMBINATORIAL FUNCTIONS
-----------------------
General purpose use for cleaner
operations in the code of this directory

'''


from math import factorial

def combination(n, k):
	
	try:
		x = factorial(n) / (factorial(k) * factorial(n-k))
	except:
		x = 0
	
	return x

def k_permutation(n, k):
	
	try:
		x = factorial(n) / factorial(n-k)
	except:
		x = 0
	
	return x

'''SET OPERATIONS LISTED BELOW--
ASSUMES SETS ARE REPRESENTED IN 
BINARY FORMAT WITH SAME LENGTH'''


def union(A, B):
	'''Union of two sets
	Algorithm 1.6 in book'''
	
	C = []
	
	if len(A) != len(B):
		return None
	
	for i in range (0, len(A)):
		
		C.append( A[i] | B[i] )
	
	return C
	

def intersection(A, B):
	'''Intersection of two sets
	Algorithm 1.7 in book'''
	
	C = []
	
	if len(A) != len(B):
		return None
	
	for i in range (0, len(A)):
		
		C.append( A[i] & B[i] )
		
	return C
	
def set_diff(A, B):
	
	C = []
	
	if len(A) != len(B):
		return None
	
	for i in range (0, len(A)):
		
		#1 exclusive or x flips bit
		C.append( A[i] & (1^B[i]) )
		
	return C
	


def sym_diff(A, B):
	
	C = set_diff(A, B) 
	D = set_diff(B, A) 
	
	return union(C, D)
	
	