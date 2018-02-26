


def rank(T, k, n):
	
	if k==1:
		return T[0]
	elif n==1:
		return 1
	else:
		return T[0] + rank(T[1:], k-1, n)
	
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