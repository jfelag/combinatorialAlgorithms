import numpy as np

'''# CONTAINS FUNCTIONS REGARDING TO MATRIX OPERATIONS #'''

def determinant(A):
	'''
	Computes determinant of matrix A
	*Wrote my own because np.linalg.det returned float
	*   and rounding it gave the wrong values
	---
	Alternate: product of the eigenvalues
	'''
	
	#n = np.shape(A)[0]
	#if n == 2:
	#	return A[0][0]*A[1][1] - A[1][0]*A[0][1]
	#d = 0
	#for i in range(n):
	#	d += ((-1)**i) * A[0][i]*determinant(matrixMinor(A, 0, i))	
	#return d
	
	
	#return the real part of the product of the eigenvalues
	return int(np.real(np.round(np.prod(np.linalg.eigvals(A)))))


def matrixMinor(A, r, c):
	'''
	computes the minor of A by deleting row (r) and column (c)
	'''
	
	#delete row
	Ar = np.delete(A, r, 0)
	
	#delete column
	Arc = np.delete(Ar, c, 1)
	
	return Arc

def constructLaplacian(A):
	'''
	constructs the Graph Laplacian for (A)
	'''
	
	n = np.shape(A)[0]
	
	#degree sequence of all n vertices
	degSeq = A.sum(axis=1)
	
	L = np.zeros((n,n), dtype='int')
	
	for i in range(n):
		for j in range(n):
			
			entry = 0
			
			if i == j:
				#L_{i,i} = deg(i)
				entry = degSeq[i]
			else:
				if A[i][j] == 0:
					#not adjacent, 0
					entry = 0
				else:
					#adjacent, -1
					entry = -1
			
			L[i][j] = entry
			
	return L
