import matplotlib.pyplot as plt
import random
import numpy as np
import networkx as nx

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
				# No começo da lista
				if mode == "Depth" :
					src_way.insert(0, way )	
					search.insert(0, element )
				# No final da lista
				if mode == "Breadth" :
					src_way.append( way )	
					search.append( element )

			# E se a lista de procura for vazia
			if len(search) == 0 :
				return [-1]

			# Define o novo node para recomeçar a busca
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
	h_euclidian = __dist(points[origin], points[target])
	# Lista heuristica euclidiana
	euclidian_list = [ [h_euclidian, origin] ]
	# Lista heuristica
	#           ( HTotal ; HCaminho ; Nó ; Caminho ao Nó )
	nodesData = [(H*h_euclidian, 0, origin, [origin] )]

	while(True) :

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

		# Se 'node' nao possui vizinhos
		if len(neighbors) == 0 :

			if DBG :
				print("Node " + str(NODE) + " have no neighbors!")

			# Se a lista de nós for vazia: Nó não encontrado!
			if len(nodesData) == 0 :
				return [-1]
			

		# Se 'node' possui vizinhos
		else :

			for element in WAY :
				try:
					neighbors.remove(element)
				except:
					pass


			for i in range(len(euclidian_list)) :
				try:
					neighbors.remove(euclidian_list[i][1])
					# print("HEY! I know you... ("+str(euclidian_list[i][1])+")")					
				except:
					pass
					# print("I must be mistaken. ("+str(euclidian_list[i][1])+")")	

			# Insere novos 'nodes' na lista
			for element in neighbors :
				# Heuristica euclidiana [ [dist, node] ]
				try:
					h_euclidian = euclidian_list[np.where(np.array(euclidian_list, dtype="object")[:,1] == element)][0][0]
					# print("HEY! I know you... ("+str(element)+")")
				except:
					h_euclidian = __dist(points[element], points[target])
					euclidian_list.append([h_euclidian, element])

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

				# Depois de encontrado a heuristica total para um certo 'node'
				# verifica se este é melhor ou pior que um já encontrado
				try:
					position = np.where(np.array(nodesData, dtype="object")[:,2]==element)[0][0]

					if h_total < nodesData[position][0] :
						nodesData.pop(position)
						nodesData.append( (h_total, h_way, element, way) )	

				except:
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
	position = np.where(np.array(nodesData, dtype="object")[:,0]==np.amin(np.array(nodesData, dtype="object")[:,0]))[0][0]

	return nodesData[position]

