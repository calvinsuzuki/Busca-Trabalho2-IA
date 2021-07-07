from networkx.algorithms.operators.product import tensor_product
from networkx.classes.function import non_edges
import graph_maker as graph
import plot
import graph_search as gs
import time
import numpy as np

n_nodes = 10000
# Make Graph
t = time.time()
# USE IT IF WANT A PREDEFINED GRAPH
G, points = graph.loadNodesAndMakeGraph('10000-3.npy')
#G, points = graph.makeGraph(n_nodes, 3)
print("makeGraph time taken: " + "{:.6f}".format(time.time()-t))

# origin = 45
# target = 83

origin = np.random.randint(n_nodes)
target = np.random.randint(n_nodes)

print("\nOrigin: " + str(origin) + " Target: " + str(target))


# Breadth
t = time.time()
way = gs.Breadth(G, origin, target)
print("\n*****\tBreadth\t*****" ) 
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))

# Depth
# t = time.time()
way = gs.Depth(G, origin, target)
print("\n*****\tDepth\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))


# Best First
# t = time.time()
way = gs.BestFirst(G, points, origin, target)
print("\n*****\tBFSearch\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))


# A Search
# t = time.time()
way = gs.ASearch(G, points, origin, target)
print("\n*****\tASearch\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))


# A* Search
# t = time.time()
way = gs.Asterix(G, points, origin, target)
print("\n*****\tAsterix\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))


# plot.plotXY(G, points)