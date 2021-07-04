import graph
import plot
import GraphSearch as gs

G, points = graph.makeGraph(50, 3)

string = gs.Breadth(G, 0, 10)

if string == '-1' :
	print("Not found!")
else :
	print("Found! The Breadth way is " + string + "\n")

string = gs.Depth(G, 0, 10)

if string == '-1' :
	print("Not found!")
else :
	print("Found! The Depth way is " + string)

plot.plotXY(G, points, label = True)
# plot.plotGraph(G)



