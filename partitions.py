'''
PARTITION
---------
How many ways you can break up a 
number, n, into a sum of positive integers.

P(3) : 1 + 1 + 1 == 1 + 2 == 3,
so P(3) = 3
'''

import numpy as np


def genPartitions(m, B, N):
	'''main genPartitions(m,m,0) to run
	lists paritions of m
	Algorithm 3.1 in book'''
	
	if m == 0:
		return []
	else:
		for i in range(1, min(B,m)):
			list[N+1] = i
			return genPartitions(m-i,i,N+1)

def partitionConjugateMatrix(V):
	'''conjugate of specific part
	Algorithm 3.2 in book, however this 
	implementation makes use of matrix operations'''
	
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

def enumPartitions(m,n):
	'''
	
	Algorithm 3.5 in book'''
	
	P = np.zeros((m+1,n+1))
	P[0][0] = 1
	
	
	for i in range(1,m+1):
		for j in range(1, min(i,n) + 1):
			if i < 2*j:
				P[i][j] = P[i-1][j-1]
			else:
				P[i][j] = P[i-1][j-1] + P[i-j][j] 
	
	return int(P[-1][-1])
	
	
def lexSuccessor(m, n, A):
	'''
	
	Algorithm 3.7 in book'''
	#print A
	i = 2
	while i <= n and A[0] <= A[i-1] + 1:
		#print A[0], A[i-1] + 1
		i += 1
	if i == n+1:
		return "undefined"
	else:
		A[i-1] += 1
		d = -1
		for j in range(i-1, 1, -1):
			d += A[j-1] - A[i-1]
			A[j-1] = A[i-1]
		A[0] += d
		return A
	
	
	

def lexRank(m, n, A):
	'''
	
	Algorithm 3.8 in book'''
	
	B = A
	
	r = 0
	
	while m > 0:
		if B[n-1] == 1:
			m -= 1
			n -= 1
		else:
			for i in range(1,n+1):
				B[i-1] -= 1
			r += enumPartitions(m-1,n-1)
			m -= n
	return r
	
	
	
	
	



def main():
	
	
	P = lambda m,n: enumPartitions(m,n)
	
	print P(26,4)+P(21,4)+P(15,3)+P(10,2)+P(7,2)
	
	
	A = [8,6,6,4,3,1]
	
	while len(A) > 1:
		
		if A[-1] == 1:
			A.pop(-1)
		else:
			print sum(A)-1, len(A)-1
			A = [x-1 for x in A]
	
	
	
	
	
