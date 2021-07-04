import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def plotGraph(graph):
    
    plt.plot()
    
    nx.draw(graph, with_labels=True, font_weight='bold')

    plt.show()

def plotXY(graph, points, label = True):
    
    edges = list(graph.edges)
    plt.scatter(points[:,0], points[:,1])
    
    if label:
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            label = "{}".format(i)

            plt.annotate(label, # this is the text
                        (x,y), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,5), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center

    for edge in edges:
        x_vec = [points[edge[0]][0], points[edge[1]][0]]
        y_vec = [points[edge[0]][1], points[edge[1]][1]]
        plt.plot(x_vec, y_vec)
    
    plt.show()
    
def plotNodesResults(tests, time_mtx, len_mtx):
    
    nrows = len(tests)
    ncols = len(tests[0])
    nmethods = len(time_mtx[0])
    
    figT, axs = plt.subplots(nrows, ncols)
    
    for i in range(nrows):
        for j in range(ncols):
            x = np.arange(nmethods)
            axs[i][j].bar(x, time_mtx[i], 0.3)
    plt.show()
    
def plotEdgesResults():
    pass