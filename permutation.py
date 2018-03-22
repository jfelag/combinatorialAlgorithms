'''
PERMUTATIONS
------
Reordering of the integers
1,2,3,...,n

'''
from math import factorial

def lexSuccessor(n, p):
	'''
	return successor of p
	in lex ordering
	Algorithm 2.14 in book
	'''
	
	print 'do this'
	

def lexRank(n, p):
	'''
	Ranks p in lex ordering
	Algorithm 2.15 in book
	'''
	
	r = 0
	for j in range(1, n+1):
		
		r += (p[j-1]-1)*factorial(n-j)
		
		for i in range(j+1,n+1):
			
			if p[i-1] > p[j-1]:
				
				p[i-1] -= 1
	
	return r

def lexUnrank(n, r):
	'''
	Unanks r in lex ordering
	Algorithm 2.16 in book
	'''
	
	print 'do this'
	



def trotterJohnsonRank(n, p):
	'''
	ranks p in Trotter-Johnson ordering
	Algorithm 2.17 in book
	'''
	
	r = 0
	
	for j in range(2,n+1):
		k = 1
		i = 1
		while p[i-1] != j:
			if p[i-1] < j:
				k += 1
			i += 1
		if r%2 == 0:
			r = j*r + j - k
		else:
			r = j*r + k - 1
	
	return r


def trotterJohnsonUnrank(n, r):
	'''
	Unranks r in Trotter-Johnson ordering
	Algorithm 2.18 in book
	'''
	
	print 'do this'


def permParity(n, p):
	'''
	Returns the parity of p (even [0] or odd [1] 
	number of inversions to get list in ascending order)
	Does NOT count inversions. Algorithm below does, but has slower run time complexity
	Algorithm 2.19 in book
	'''
	
	a = [0] * n
	c = 0
	for j in range(1,n+1):
		if a[j-1] == 0:
			c += 1
			a[j-1] = 1
			i = j
			while p[i-1] != j:
				i = p[i-1]
				a[i-1] = 1
				
	return (n-c)%2
	

def countInversions(n, p):
	'''
	Returns number of inversions to get p in ascending order
	Can be used to get parity, but is slower than the above algorithm
	'''
	
	c = 0
	
	for i in range(0,n):
		for j in range(i+1,n):
			
			if p[j] < p[i]:
				
				c += 1
				
	return c


def trotterJohnsonSuccessor(n, p):
	'''
	returns successor of p in 
	Trotter-Johnson ordering
	Algorithm 2.20 in book
	'''
	
	print 'do this'
	











































