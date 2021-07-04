import graph
import plot

G, points = graph.makeGraph(3000, 3)

for i in range(len(G.nodes)):
    print(G[i])

# print(G[9])

plot.plotXY(G, points, label = False)
# plot.plotGraph(G)


