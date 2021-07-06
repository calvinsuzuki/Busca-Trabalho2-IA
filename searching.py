from networkx.algorithms.operators.product import tensor_product
from networkx.classes.function import non_edges
import graph
import plot
import GraphSearch as gs
import time
import numpy as np

n_nodes = 20
# Make Graph
t = time.time()
G, points = graph.makeGraph(n_nodes, 3)
print("makeGraph time taken: " + "{:.6f}".format(time.time()-t))

origin = np.random.randint(n_nodes)
target = np.random.randint(n_nodes)

print("\nSearching node " + str(target) + " from node " + str(origin))

# Breadth
t = time.time()
string = gs.Breadth(G, origin, target)
print("\nBreadth time taken: " + "{:.6f}".format(time.time()-t))

if string == '-1' :
	print("Breadth: Not found!")
else :
	print("Found! The Breadth way is " + string)

# Depth
t = time.time()
string = gs.Depth(G, origin, target)
print("\nDepth time taken: " + "{:.6f}".format(time.time()-t))

if string == '-1' :
	print("Depth: Not found!")
else :
	print("Found! The Depth way is " + string)

# Best First
t = time.time()
string = gs.BestFirst(G, points, origin, target)
print("\nBestFirst time taken: " + "{:.6f}".format(time.time()-t))

if string == '-1' :
	print("BestFirst: Not found!")
else :
	print("Found! The BestFirst way is " + string)

# A Search
t = time.time()
string = gs.ASearch(G, points, origin, target)
print("\nASearch time taken: " + "{:.6f}".format(time.time()-t))

if string == '-1' :
	print("ASearch: Not found!")
else :
	print("Found! The ASearch way is " + string)

# A* Search
t = time.time()
string = gs.Asterix(G, points, origin, target)
print("\nAsterix time taken: " + "{:.6f}".format(time.time()-t))

if string == '-1' :
	print("Asterix: Not found!")
else :
	print("Found! The Asterix way is " + string)


plot.plotXY(G, points)