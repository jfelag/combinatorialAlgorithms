'''
k-SUBSET
--------
A list of items taken from 
[1,2,3,...,n] that are distinct
Ranking includes ONLY length k subsets
    (number of 1s in list is k)
'''


from comFuncs import combination


def colexUnrank(r, k, n):
	'''unranks colex ordering
	Algorithm 2.10 in book'''
	
	T = [0]*k
	x = n
	for i in range(1,k+1):
		
		c = combination(x, k+1-i)
			
		while c > r:
			
			x -= 1
			c = combination(x, k+1-i)
			
		T[i-1] = x+1
		r -= combination(x, k+1-i)
	return T


def successor(T, k, n):
	
	T = T[::-1]
	inOrder = True
	offender = -1
	
	for i in range(1, k):
		
		if T[i-1] + 1 != T[i]:
			inOrder = False
			offender = i-1
			break
	
	if inOrder:
		if T[k-1] == n:
			return "undefined"
		T[k-1] += 1
		dec = T[0] - 1
		for i in range(0,k-1):
			T[i] -= dec
	else:
		T[offender] += 1
	
	return T[::-1]
