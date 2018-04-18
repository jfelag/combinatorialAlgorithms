import sys
sys.path.append('..')
from comFuncs import combination
from kSubset import colexUnrank

def checkIfTree(V, E):
	'''
	Checks if (E) is a tree on (V)
	'''
	
	n = len(V)
	k = len(E)
	
	vertexSet = set(V) 
	
	visitedSet = set()
	
	if k == n-1:
		
		for (x,y) in E:
			
			visitedSet.add(x)
			visitedSet.add(y)
		
		return visitedSet == vertexSet
		
	else:
		
		return False




def bruteForce(V, E):
	'''
	Brute force search through all k=(n-1)-subsets in (E)
	'''
	
	validTrees = []
	
	k = len(V) - 1
	m = len(E)
	
	numSubsets = combination(m, k)
	
	for i in range(numSubsets):
		
		subset = colexUnrank(i, k, m)
		
		edgeSubset = []
		
		for j in subset:
			
			edgeSubset.append(E[j-1])
			
		
		isTree = checkIfTree(V, edgeSubset)
		
		if isTree:
			validTrees.append(edgeSubset)
		
	return validTrees


def main():
	V = range(5)
	E = range(7)
	
	bruteForce(V,E)