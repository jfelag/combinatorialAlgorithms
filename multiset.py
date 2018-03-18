'''
MULTISET
--------


'''

from math import factorial

def combination(n, k):
	
	try:
		x = factorial(n) / (factorial(k) * factorial(n-k))
	except:
		x = 0
	
	return x

def rank(T, k, n):
	
	#base cases
	if k==1:
		return T[0]
	elif n==1:
		return 1
	else:
		
		if T[0] != 1:
			T = [x-1 for x in T]
			return combination(n+k-2,k-1) + rank(T, k, n-1)
		else:
			return rank(T[1:], k-1, n)
			

def unrank(r, k, n):
	
	if k == 1:
		return [r]
	if r == 1:
		return [1]*k
	if n == 1:
		return [1]
	
	if r > combination(n+k-1,k):
		return 'undefined'
	
	else:
		c = 0
		for i in range(k):
			c += combination(n+k-(i+2), n-(i+2) )
			if r <= c:
				return [i+1] + unrank(r-k,k-1,n)

def successor(T, k, n):
	
	if T[k-1] != n:
		T[k-1] += 1
		return T
	else:
		c = 1
		while T[k-(c+1)] == n:
			c += 1
			if c == k:
				return "undefined"
			
		T[k-(c+1)] += 1
		
		for i in range(k-c,k):
			T[i] = T[k-(c+1)]
		
		return T
	

def main():
	
	print "TEST ONE"
	
	T = [1,1,1]
	for i in range(35):
		print i+1, unrank(i+1, 3, 4)
		T = successor(T,3,4)
		