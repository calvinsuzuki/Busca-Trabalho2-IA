import graph
import plot
import GraphSearch as gs

G, points = graph.makeGraph(100, 3)

for i in range(len(G.nodes)):
    print(G[i])

# print(G[9])

string = gs.BLSearch(G, 0, 10)

if string == -1 :
	print("Not found!")
else :
	print("Found! The way is " + string)

plot.plotXY(G, points)
# plot.plotGraph(G)



