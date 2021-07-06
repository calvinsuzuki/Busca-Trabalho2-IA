from networkx.algorithms.operators.product import tensor_product
from networkx.classes.function import non_edges
import graph
import plot
import GraphSearch as gs
import time
import numpy as np

n_nodes = 500
# Make Graph
t = time.time()
G, points = graph.makeGraph(n_nodes, 3)
print("makeGraph time taken: " + "{:.6f}".format(time.time()-t))

origin = np.random.randint(n_nodes)
target = np.random.randint(n_nodes)

print("\nSearching node " + str(target) + " from node " + str(origin))

# Breadth
t = time.time()
way = gs.Breadth(G, origin, target)
print("\nBreadth time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Breadth: Not found!")
else :
	print("Found! The Breadth way is " + str(way))

# Depth
t = time.time()
way = gs.Depth(G, origin, target)
print("\nDepth time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Depth: Not found!")
else :
	print("Found! The Depth way is " + str(way))

# Best First
t = time.time()
way = gs.BestFirst(G, points, origin, target)
print("\nBestFirst time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("BestFirst: Not found!")
else :
	print("Found! The BestFirst way is " + str(way))

# A Search
t = time.time()
way = gs.ASearch(G, points, origin, target)
print("\nASearch time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("ASearch: Not found!")
else :
	print("Found! The ASearch way is " + str(way))

# A* Search
t = time.time()
way = gs.Asterix(G, points, origin, target)
print("\nAsterix time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Asterix: Not found!")
else :
	print("Found! The Asterix way is " + str(way))


plot.plotXY(G, points)