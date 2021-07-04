import graph
import plot
import GraphSearch as gs

G, points = graph.makeGraph(500, 3)

string = gs.BLSearch(G, 0, 10)

if string == '-1' :
	print("Not found!")
else :
	print("Found! The way is " + string)

string = gs.BPSearch(G, 0, 10)

if string == '-1' :
	print("Not found!")
else :
	print("Found! The way is " + string)

plot.plotXY(G, points)
# plot.plotGraph(G)



