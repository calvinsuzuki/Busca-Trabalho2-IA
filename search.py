from networkx.algorithms.operators.product import tensor_product
from networkx.classes.function import non_edges
import matplotlib.patches as mpatches
import graph_maker as graph
import plot
import graph_search as gs
import time
import numpy as np

# Simplifica a chamada para animação
def drawWay(way, color, animate):
	plot.plotPath(axis, way, points, animate, color)

# Define os Patches na legenda do gráfico
red = mpatches.Patch(color='red', label='Largura')
blue = mpatches.Patch(color='blue', label='Profundidade')
orange = mpatches.Patch(color='darkorange', label='Best First')
violet = mpatches.Patch(color='m', label='A')
green = mpatches.Patch(color='green', label='A*')

n_nodes = 500
# Make Graph
t = time.time()
# USE IT IF WANT A PREDEFINED GRAPH
G, points = graph.loadNodesAndMakeGraph('/graph/500-3.npy')
#G, points = graph.makeGraph(n_nodes, 3)
print("makeGraph time taken: " + "{:.6f}".format(time.time()-t))

origin = 136
target = 318

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

#anime(way, 'red')

# Depth
t = time.time()
way = gs.Depth(G, origin, target)
print("\n*****\tDepth\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))

#anime(way, 'blue')


# Best First
t = time.time()
way = gs.BestFirst(G, points, origin, target)
print("\n*****\tBFSearch\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))

# anime(way, 'darkorange')

# A Search
t = time.time()
way = gs.ASearch(G, points, origin, target)
print("\n*****\tASearch\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))

# anime(way, 'm')

# A* Search
t = time.time()
way = gs.Asterix(G, points, origin, target)
print("\n*****\tAsterix\t*****" )  
print("Time taken: " + "{:.6f}".format(time.time()-t))

if way == [-1] :
	print("Not found!")
else :
	print("The way is " + str(way))

anime(way, 'green')
plot.legends([green])
plot.Show()