import matplotlib.pyplot as plt
import networkx as nx

def plotGraph(graph):
    
    plt.plot()
    
    nx.draw(graph, with_labels=True, font_weight='bold')

    plt.show()

def plotXY(graph, points):
    
    edges = list(graph.edges)
    plt.scatter(points[:,0], points[:,1])
    
    for edge in edges:
        x_vec = [points[edge[0]][0], points[edge[1]][0]]
        y_vec = [points[edge[0]][1], points[edge[1]][1]]
        plt.plot(x_vec, y_vec)
    
    plt.show()