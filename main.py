import graph
import plot
import GraphSearch as gs

G, points = graph.makeGraph(50, 3)

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

plot.plotXY(G, points, label = True)
# plot.plotGraph(G)



