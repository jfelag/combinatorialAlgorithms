'''
GRAY CODES
----------
A list of all binary strings of a certain length
such that the Hamming distance between any pair of
adjacent members is 1
'''
from math import floor
from comFuncs import sym_diff, element_of, union, insert

def genBinaryReflected(n):
	'''
	Returns Binary reflected Gray Code sequence with strings of length n
	'''
	T = ['0', '1']
	
	if n == 0:
		return []
	elif n == 1:
		pass
	else:
	
		for i in range(n-1): #start at 1, so we need next n-1
			T = T + T[::-1]

			for j in range(len(T)):
				if j < len(T)/2:
					T[j] = '0'+T[j]
				else:
					T[j] = '1'+T[j]
				
	return T

def successor(n, T):
	'''
	return successor of gray code
	Algorithm 2.3 in book'''
	
	A = [0] * n
	U = []
	
	if len(T)%2 == 0:
		A[-1] = 1
		U = sym_diff(T, A)
	else:
		j = n
		while j not in T and j > 0:
			j -= 1
		if j == 1:
			return 'undefined'
		A[j-2] = 1 
		U = sym_diff(T, A)
	
	return U

def rank(n, T):
	'''
	Ranking for Gray Code
	Algorithm 2.4 in book'''
	
	r = 0
	b = 0
	
	for i in range(n-1, -1, -1):
		
		if element_of(n-i, T):
			b = 1-b
		if b == 1:
			r += 2**i
			
	return r

def unrank(n, r):
	
	T = [0]*n
	bp = 0
	
	for i in range(n-1, -1, -1):
		b = floor(r/(2**i))
		if b != bp:
			A = [0]*n
			A = insert(n-i, A)
			T = union(T, A)
		bp = b
		r -= b*2**i
	return T
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	