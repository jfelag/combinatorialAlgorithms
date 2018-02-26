from math import factorial


def combination(n, k):
	
	try:
		x = factorial(n) / (factorial(k) * factorial(n-k))
	except:
		x = 0
	
	return x
	


def unrank(r, k, n):
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
