import matplotlib.pyplot as plt
import random
import numpy as np
import networkx as nx

DBG = False

def __BlindSearch(G, origin, objective, mode):

	node = origin
	visited = []

	search = [origin]
	src_way = [str(origin)]

	if origin==objective:
		print("Visiting " + str(search) + "...")
		return str(origin)

	while(True) :
		if DBG :
			print("\nVisited list is " + str(visited))
			print("Searching list is " + str(search))
			print("L = " + str(src_way))

		# Se o nó procurado for esse, retorne True
		if objective==node:
			return str(src_way[0])

		if DBG :
			print("Not found! Lets see "+str(node)+" neighbors...")

		# node_neigh = Lista de vizinhos de 'node'
		node_neigh = [n for n in list(G.neighbors(node))]

		# Remove 'node' da lista de procura
		search.pop(0)
		aux_str = src_way.pop(0)

		visited.append(node)

		# Se 'node' nao possui vizinhos
		if len(node_neigh) == 0 :

			if DBG :
				print("Node " + str(node) + " have no neighbors!")

			# E se a lista de procura for vazia
			if len(search) == 0 :
				return '-1'
		
			search.pop(0)
			src_way.pop(0)
			node = search[0]
		# Se 'node' possui vizinhos
		else :

			for element in visited :
				try :
					node_neigh.remove(element)
				except :
					pass

			for element in search :
				try :
					node_neigh.remove(element)
				except :
					pass

			for j in range(len(node_neigh)) :
				if mode == "Depth" :
					src_way.insert(0, aux_str +" "+ str( node_neigh[j] ) )	
					search.insert(0, node_neigh[j])
				if mode == "Breadth" :
					src_way.append( aux_str +" "+ str( node_neigh[j] ) )	
					search.append( node_neigh[j])

			# E se a lista de procura for vazia
			if len(search) == 0 :
				return '-1'

			node = search[0]

	return '-1'

def Depth(G, origin, objective):

	return __BlindSearch(G, origin, objective, "Depth")

def Breadth(G, origin, objective):

	return __BlindSearch(G, origin, objective, "Breadth")
