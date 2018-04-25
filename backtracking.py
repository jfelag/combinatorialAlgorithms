import numpy as np

def estimateBacktrack():
	'''
	Samples one size for backtrack tree
	Average multiple calls to get accurate estimate
	Algorithm 4.5 in book
	'''
	
	return 0
	

def probe():
	'''
	Subroutine for algorithm 4.5
	'''
	
	return 0
	
	

def reduce(M):
	'''
	Finds a lower bound for a Hamiltonian Path
	Algorithm 4.11 in book
	'''
	
	A = np.array(M)
	
	print A
	
	m = A.shape[0]
	
	val = 0
	
	low = 0
	
	for i in range(m):
		low = np.min(A[i][:])
		print A[i][:]
		A[i][:] -= low
		val += low
	
	for i in range(m):
		low = np.min(A[:][i])
		print A[:][i]
		A[:][i] -= low
		val += low
		
	return val
	
