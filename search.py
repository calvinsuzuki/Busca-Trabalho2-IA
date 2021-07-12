from networkx.algorithms.operators.product import tensor_product
from networkx.classes.function import non_edges
import matplotlib.patches as mpatches
import graph_maker as graph
import plot
import graph_search as gs
import time
import numpy as np
import os

def drawWay(way, color, animate):
	plot.plotPath(axis, way, points, animate, color)

# ----------------------------------User interaction
# Define nodes and edges -  LOOK AT 'graphs' FOLDER
n_nodes = 500
n_edges = 3

# Define origin and target - MAKE SURE THEY ARE IN THE GRAPH 
origin = 136
target = 318
# ----------------------------------

# Make Graph
t = time.time()

# USE IT IF WANT A PREDEFINED GRAPH. 
file = os.path.join('graphs',f'{n_nodes}-{n_edges}.npy')
G, points = graph.loadNodesAndMakeGraph(file)

# USE IT IF WANT TO GENERATE A GRAPH
#G, points = graph.makeGraph(n_nodes, 3)

print("Graph load or make time taken: " + "{:.6f}".format(time.time()-t))

# origin = np.random.randint(n_nodes)
# target = np.random.randint(n_nodes)

print("\nOrigin: " + str(origin) + " Target: " + str(target))

figure, axis = plot.plotXY(G, points)

# Breadth
t = time.time()
way = gs.Breadth(G, origin, target)
print("\n*****\tBreadth\t*****" ) 
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))

drawWay(way, 'red', False)

# Depth
t = time.time()
way = gs.Depth(G, origin, target)
print("\n*****\tDepth\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))

drawWay(way, 'blue', False)


# Best First
t = time.time()
way = gs.BestFirst(G, points, origin, target)
print("\n*****\tBFSearch\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))

drawWay(way, 'darkorange', False)

# A Search
t = time.time()
way = gs.ASearch(G, points, origin, target)
print("\n*****\tASearch\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))

drawWay(way, 'm', False)

# A* Search
t = time.time()
way = gs.Asterix(G, points, origin, target)
print("\n*****\tAsterix\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))

# Define os Patches na legenda do gráfico
red = mpatches.Patch(color='red', label='Largura')
blue = mpatches.Patch(color='blue', label='Profundidade')
orange = mpatches.Patch(color='darkorange', label='Best First')
violet = mpatches.Patch(color='m', label='A')
green = mpatches.Patch(color='green', label='A*')

drawWay(way, 'green', False)
plot.legends([red, blue, orange, violet, green])

print("Complete. Showing results!")
plot.Show()