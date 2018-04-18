from math import floor
from comFuncs import set_diff

def prufer(E, n):
	'''
	Takes an edge set (E) and number of vertices (n)
	Returns Prufer Code 
	Algorithm 3.18 in book'''
	
	d = [0]*n
	
	for x,y in E:
		d[x] += 1
		d[y] += 1
	
	for i in range(1,n-1):
		x = n
		while d[x] != 1:
			x -= 1
		y = n
		while (x,y) not in E:
			y -= 1
		L[i-1] = y
		d[x] -= 1
		d[y] -= 1
		E = set_diff(E,[(x,y)])
	
	return L

def invPrufer(L, n):
	'''
	Takes Prufer Code (L) and number of vertices (n)
	Returns edge set for the labeled tree
	Algorithm 3.19 in book'''
	
	E = []
	
	
	


def pruferToRank(L, n):
	'''
	Takes Prufer Code (L) and number of vertices (n)
	Returns its rank
	Algorithm 3.20 in book'''
	
	r = 0
	p = 1
	
	for i in range(n-2, 0,-1):
		r += p*(L[i-1] - 1)
		p *= n
	
	return r

def rankToPrufer(r, n):
	'''
	Takes rank (r) and number of vertices (n)
	Returns Prufer Code
	Algorithm 3.21 in book'''
	
	L = [0]*(n-2)
	
	for i in range(n-2,0,-1):
		
		L[i-1] = r%n + 1
		
		r = int(floor( (r-L[i-1]+1)/n ))
	
	return L