import matplotlib.pyplot as plt
import random
import numpy as np
import networkx as nx
import time


# Busca por profundidade
def Depth(graph, origin, target):

	return __BlindSearch(graph, origin, target, "Depth")

# Busca por largura
def Breadth(graph, origin, target):

	return __BlindSearch(graph, origin, target, "Breadth")

def BestFirst(graph, points, origin, target):
	
	return __HeuristicSearch(graph, points, origin, target, 0, 1)

def ASearch(graph, points, origin, target):

	return __HeuristicSearch(graph, points, origin, target, 1, 10)

def Asterix(graph, points, origin, target):

	return __HeuristicSearch(graph, points, origin, target, 1, 1)

# Funcão que faz busca cega
def __BlindSearch(graph, origin, target, mode, DBG = False):

	# Finaliza ao encontrar o caso especificado
	if origin==target:
		if DBG :
			print("Your origin is your target!")
		return [origin]

	# Inicializa a busca partindo da origem
	node = origin
	# Lista de 'nodes' visitados
	visited = []
	# Lista de busca 
	search = [origin]
	# Lista de caminhos
	src_way = [[origin]]

	while(True) :
		if DBG :
			print("\nVisited list is " + str(visited))
			print("Searching list is " + str(search))
			print("L = " + str(src_way))

		if mode == "Depth" :
			position = len(search)-1
		# No final da lista
		if mode == "Breadth" :
			position = 0

		# Define o novo node para recomeçar a busca
		node = search[position]

		# Se o nó procurado for esse, retorne True
		if target==node:
			return src_way[position]

		if DBG :
			print("Not found! Lets see "+str(node)+" neighbors...")

		# neighbors = Lista de vizinhos de 'node'
		neighbors = list(graph.neighbors(node))

		# Remove 'node' da lista de procura
		search.pop(position)
		aux_str = src_way.pop(position)

		position-=1

		if position == -1:
			position = 0

		visited.append(node)

		# Se 'node' nao possui vizinhos
		if len(neighbors) == 0 :

			if DBG :
				print("Node " + str(node) + " have no neighbors!")

			# Se a lista de procura for vazia: Nó não encontrado!
			if len(search) == 0 :
				return [-1]
			
			# Retira-se o item da lista 
			search.pop(position)
			src_way.pop(position)
			node = search[position]

		# Se 'node' possui vizinhos
		else :
			# Remove os vizinhos já presentes na lista de visitados
			for element in visited :
				try :
					neighbors.remove(element)
				except :
					pass

			# Remove os vizinhos já presentes na lista de procura
			for element in search :
				try :
					neighbors.remove(element)
				except :
					pass
			# Insere novos 'nodes' na lista de procura
			for element in neighbors :
				# Caminho
				way = []
				way.extend(aux_str)
				way.append(element)

				src_way.append( way )	
				search.append( element )

			# E se a lista de procura for vazia
			if len(search) == 0 :
				return [-1]

			

	return [-1]

# Função de busca heurística
def __HeuristicSearch(graph, points, origin, target, G, H, DBG = False):

	# Finaliza ao encontrar o caso especificado
	if origin==target:
		if DBG :
			print("Your origin is your target!")
		return [origin]

	# Heuristica euclidiana
	if H!=0 :
		h_euclidian = __dist(points[origin], points[target])
	else :
		h_euclidian = 0
	# Lista heuristica euclidiana
	visited = [ [origin] ]
	# Lista heuristica
	#           ( HTotal ; HCaminho ; Nó ; Caminho ao Nó )
	nodesData = [(H*h_euclidian, 0, origin, [origin] )]

	while(True) :
		
		if G==0 and H==0:
			nodeMin = nodesData[0]
		else:
			# Analisa o 'node' com a menor heuristica
			nodeMin = getMinNode(nodesData)

		HTOTAL = nodeMin[0]
		HWAY = nodeMin[1]
		NODE = nodeMin[2]
		WAY = nodeMin[3]
		
		if DBG :
			print("L = ")
			for j in range(len(nodesData)):
				print("{:.2f}".format(nodesData[j][0]) +" "+ "{:.2f}".format(nodesData[j][1]) +" "+ str(nodesData[j][2]) +" ("+ str(nodesData[j][3]) + ")") 

		# Se o nó procurado for esse, retorne o "Caminho ao Nó"
		if target==NODE:
			return WAY

		if DBG :
			print("Not found! Lets see "+str(NODE)+" neighbors...")

		# neighbors = Lista de vizinhos de 'node'
		neighbors = list(graph.neighbors(NODE))

		# Remove 'node' da lista de procura
		nodesData.remove(nodeMin)

		visited.append(NODE)

		# Se 'node' nao possui vizinhos
		if len(neighbors) == 0 :

			if DBG :
				print("Node " + str(NODE) + " have no neighbors!")

			# Se a lista de nós for vazia: Nó não encontrado!
			if len(nodesData) == 0 :
				return [-1]

		# Se 'node' possui vizinhos
		else :
			# Remove os vizinhos já presentes na lista de visitados
			for element in visited :
				try:
					neighbors.remove(element)
					# print("HEY! I know you... ("+str(euclidian_list[i][1])+")")					
				except:
					pass
					# print("I must be mistaken. ("+str(euclidian_list[i][1])+")")	

			for i in range(len(nodesData)) :
				try:
					neighbors.remove(nodesData[i][2])
					# print("HEY! I know you... ("+str(euclidian_list[i][1])+")")					
				except:
					pass
					# print("I must be mistaken. ("+str(euclidian_list[i][1])+")")	

			# Insere novos 'nodes' na lista
			for element in neighbors :
				# Heuristica euclidiana [ [dist, node] ]
				if H != 0 :
					h_euclidian = __dist(points[element], points[target])
				else :
					h_euclidian = 0

				# print("Visited list ("+str(euclidian_list)+")")

				if G != 0 :
					# Heuristica de caminho
					h_way = HWAY + __dist( points[element], points[NODE] )
				else : 
					h_way = 0

				# Heuristica total
				h_total = G*h_way + H*h_euclidian

				# Caminho
				way = []
				way.extend(WAY)
				way.append(element)

				nodesData.append( (h_total, h_way, element, way) )

			# E se a lista de procura for vazia
			if len(nodesData) == 0 :
				return [-1]

			# Ordena a lista de 'nodes' com suas heuristicas
			# A nodesData[0] é o novo node para recomeçar a busca

	return [-1]

# Calcula distancia entre dois pontos
def __dist(pt0, pt1):
    
    return np.sqrt((pt0[0]-pt1[0])**2+(pt0[1]-pt1[1])**2)

def getMinNode(nodesData):

	nodesData = sorted(nodesData , key=lambda k: [k[0]])

	return nodesData[0]

