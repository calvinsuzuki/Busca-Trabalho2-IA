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

# Busca por BestFirst
def BestFirst(graph, points, origin, target):
	
	return __HeuristicSearch(graph, points, origin, target, 0, 1)

# Busca por BestFirst A
def ASearch(graph, points, origin, target):

	return __HeuristicSearch(graph, points, origin, target, 1, 10)

# Busca por BestFirst A*
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

		# Se o nó procurado for esse, retorne True
		if target==node:
			return src_way[0]

		if DBG :
			print("Not found! Lets see "+str(node)+" neighbors...")

		# neighbors = Lista de vizinhos de 'node'
		neighbors = list(graph.neighbors(node))

		# Remove 'node' da lista de procura
		search.pop(0)
		aux_str = src_way.pop(0)

		# Adiciona o 'node' visitado na lista de visitados
		visited.append(node)

		# Se 'node' nao possui vizinhos
		if len(neighbors) == 0 :

			if DBG :
				print("Node " + str(node) + " have no neighbors!")

			# Se a lista de procura for vazia: Nó não encontrado!
			if len(search) == 0 :
				return [-1]
			
			# Retira-se o item da lista 
			search.pop(0)
			src_way.pop(0)
			node = search[0]

		# Se 'node' possui vizinhos
		else :

			# Filtragem de vizinhos

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

			# Insere vizinhos filtrados na lista de procura
			for element in neighbors :
				# Caminho
				way = aux_str.copy()
				# way.extend(aux_str)
				way.append(element)

				# print(f'Tamanho do way: {len(way)}')
				# print(f'Tamanho do way_str: {len(aux_str)}')

				# No começo da lista
				if mode == "Depth" :
					src_way.insert(0, way )	
					search.insert(0, element )
				# No final da lista
				if mode == "Breadth" :
					src_way.append( way )	
					search.append( element )

				way = []

			# Se a lista de procura for vazia, caminho não encontrado!
			if len(search) == 0 :
				return [-1]

			# Define o novo 'node' para recomeçar a busca
			node = search[0]

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
	# Lista heuristica = ( HTotal ; HCaminho ; Nó ; Caminho ao Nó )
	nodesData = [(H*h_euclidian, 0, origin, [origin] )]

	while(True) :
		
		if G==0 and H==0:
			nodeMin = nodesData[0]
		else:
			# Adquire o 'node' com a menor heuristica
			nodeMin = getMinNode(nodesData)

		# Registra variaveis auxiliares
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

		# Adiciona 'node' na lista de visitados
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
				except:
					pass
			# Remove os vizinhos já presentes na lista de procura
			for i in range(len(nodesData)) :
				try:
					neighbors.remove(nodesData[i][2])				
				except:
					pass

			# Insere novos 'nodes' na lista
			for element in neighbors :
				
				if H != 0 :
					# Heuristica euclidiana [ [dist, node] ]
					h_euclidian = __dist(points[element], points[target])
				else :
					h_euclidian = 0

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

			# Se a lista de procura for vazia, entao, caminho nao encontrado
			if len(nodesData) == 0 :
				return [-1]

	return [-1]

# Calcula distancia entre dois pontos
def __dist(pt0, pt1):
    
    return np.sqrt((pt0[0]-pt1[0])**2+(pt0[1]-pt1[1])**2)

# Ordena a lista de procura e retorna o menor elemento heuristico
def getMinNode(nodesData):

	nodesData = sorted(nodesData , key=lambda k: [k[0]])

	return nodesData[0]

