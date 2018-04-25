from subset import lexUnrank
from comFuncs import combination
import numpy as np


def selectPartition(n):
	'''
	Selects a random partition of a graph on 2*(n) vertices
	returns two parts X0, X1
	Algorithm 5.7 in book
	'''
	
	#selects random partition to be X0
	r = np.random.randint(0, combination(2*n, n))
	X0 = lexUnrank(2*n, r)
	
	#X1 is the complement of X0 
	X1 = np.array(range(2*n))
	X1 = np.delete(X1, X0)
	
	return ([X0, X1])
	
	