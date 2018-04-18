from comFuncs import combination
from math import factorial

def stirling2(m,n):
	
	s = 0
	
	for j in range(1, n+1):
		
		s += (-1)**(n-j) * combination(n,j) * (j**m)
	
	return s/factorial(n)


for i in range(1,11):
	m = i*10
	print stirling2(m, 2) == int(2**(m-1)) - 1