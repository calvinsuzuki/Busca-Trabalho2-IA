import graph
import plot

G, points = graph.makeGraph(1000, 3)

for i in range(len(G.nodes)):
    print(G[i])

# print(G[9])

plot.plotXY(G, points)
# plot.plotGraph(G)


