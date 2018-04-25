import numpy as np

'''
Psuedocode from paper
============================
Procedure S; begin
	Procedure GROW; begin
		if T has V vertices
			return E
		else
			make FF an empty list
			loop
				pop e from E
				e goes from T to v not in T
				add e to T
				push each (v,w) (w not in T) onto F
				remove each (w,v) (w in T) from F
				GROW
				pop each (v,w) (w not in T) from F
				restore each edge (w,v) (w in T) in F
				remove e from T and G
				add e to FF
				if (w,v) exists s.t. w is not a child of v in L
					b = False
				else
					b = True
			until b
			pop every e from FF
				push e onto F
				add e to G
	end GROW
	initialize T = [r]
	F = {(r,v) : v child of r}
	GROW
end S
'''


def gmTrees(V, E):
	'''
	Finds spanning trees as described in 
	Gabow, Myers 1978
	'''
	
	#for undirected graphs, the algorithm
	#  requires making each edge bidirectional
	newE = []
	for e in E:
		newE.append(e)
		newE.append(e[::-1])
	
	return S(V, newE)
	

def grow():
	'''
	"GROW" subroutine described in paper
	'''
	if len(VT) == n:
		return ET
	else:
		FF = []
		loop:
			
			#pop e from E
			e = F.pop()
			
			#e goes from T to v not in T (e = (a,v))
			'''write this line'''
			
			#add e to T
			T.append(e)
			
			#push each (v,w) (w not in T) onto F
			'''write this line'''
			
			#remove each (w,v) (w in T) from F
			'''write this line'''
			
			GROW
			
			#pop each (v,w) (w not in T) from F
			for edge in F:
				if edge[0] == v and edge[1] not in T:
					F.remove(edge)
			
			restore each edge (w,v) (w in T) in F
			
			#remove e from T and G
			T.remove(e)
			G.remove(e)
			
			#add e to FF
			FF.append(e)
			
			#if (w,v) exists s.t. w is not a child of v in L
			'''write this line'''
				#b = False
			#else:
				#b = True
				
		until b
		
		#pop every e from FF
		for edge in FF:
			#push e onto F
			F.append(edge)
			#add e to G
			G.append(edge)



def S(V, E):
	'''
	"S" subroutine described in paper
	'''

	T = [1]
	for e in E:
		if e[0] = T[0]:
			F.append(e)
			
	GROW
	
	
	
	
