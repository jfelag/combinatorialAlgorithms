'''
SUBSET
------
A list of distinct items taken from
the list [1,2,3,...,n]
Ranking includes EVERY subset 

'''



from math import floor

def lexRank(n, T):
	'''
	ranks subsets of [1,2,3,...,n]
	Algorithm 2.1 in book
	'''
	r = 0
	for i in range(1,n+1):
		if i in T:
			r += 2**(n-i)
	return r

def lexUnrank(n,r):
	'''
	unranks subsets of [1,2,3,...,n]
	Algorithm 2.2 in book
	'''
	T = []
	for i in range(n,0,-1):
		if r % 2 == 1:
			T = [i] + T
		r = floor(r/2)
	return T
