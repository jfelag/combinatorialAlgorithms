import numpy as np


def genPartitions(m, B, N):
	'''p(m) = genPartitions(m,m,0) '''
	
	if m == 0:
		return []
	else:
		for i in range(1, min(B,m)):
			list[N+1] = i
			return genPartitions(m-i,i,N+1)

def partitionInverse(V):
	
	#convert to numpy array
	V = np.array(V)
	
	#get max element
	m = np.max(V)
	
	#get size
	s = V.size
	
	#define matrix (block method for representing partition)
	A = np.zeros((s,m))
	
	#put numbers into block repr (1 means block is there)
	for i in range(s):
		A[i] = np.concatenate((np.ones(V[i]), np.zeros(m-V[i])))

	#Inverse array to return
	I = []
	for i in range(m):
		I.append(np.sum(A[:,i]))
		
	return I
	
