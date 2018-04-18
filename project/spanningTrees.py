import time
import numpy as np 
from matrixFuncs import constructLaplacian
from matrixFuncs import determinant
from matrixFuncs import matrixMinor
from backtrack import backtrackTrees
from gabowMyers import gmTrees
from bruteForce import bruteForce

def convertSetsToMatrix(V, E):
	'''
	Takes in vertex set and edge set
	Return adjacency matrix
	'''
	
	n = len(V)
	
	M = np.zeros((n,n), dtype='int')
	
	for i,j in E:
		
		M[i-1][j-1] = 1
		M[j-1][i-1] = 1
		
	return M

def enumerateTrees(A):
	'''
	Gives the number of spanning trees in a simple, undirected graph
	See: Kirchhoff's Matrix-Tree Theorem
	'''
	
	#Laplacian matrix of graph
	L = constructLaplacian(A)
	
	n = np.shape(A)[0]
	
	Q = matrixMinor(L,0,0)
	
	#print Q
	
	d = determinant(Q)
	
	return d

def readablePrint(L):
	'''
	Prints the list of trees nicely
	'''
	
	try:
		for l in L:
			print l
	except TypeError:
		pass

def runAlgorithm(V, E, alg='bruteforce'):
	
	if alg == 'backtrack':
		return backtrackTrees(V, E)
	elif alg == 'gm':
		return gmTrees(V, E)
	else:
		return bruteForce(V, E)
	
	
def runTest(V, E):
	
	A = convertSetsToMatrix(V, E)
	#print A
	
	print "Number found from Kirchhoff's Matrix-Tree Theorem"
	print enumerateTrees(A)
	
	algorithms = ['bruteforce', 'backtrack', 'gm']
	
	for a in algorithms:
		
		start = time.time()

		trees = runAlgorithm(V, E, a)

		print '%s run time:'%a, time.time() - start

		print 'All spanning trees'
		readablePrint(trees)

		print 'Number found in search'
		print len(trees)
		print ' '

	
def main():
	
	V = [1,2,3,4]
	E = [(1,2),(2,4),(4,3),(3,1),(2,3)]
	
	print 'TEST ONE'
	runTest(V,E)
	
	V = [1,2,3]
	E = [(1,2),(1,3),(2,3)]
	
	print 'TEST TWO'
	runTest(V,E)
	










