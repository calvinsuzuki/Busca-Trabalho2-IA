from networkx.algorithms.operators.product import tensor_product
from networkx.classes.function import non_edges
import graph
import plot
import GraphSearch as gs
import numpy as np
import time

# Test case = [(n_nodes, n_edges), ...]
tests_mtx = [[(200, 3), (200, 5), (200,7)],
             [(400, 3), (400, 5), (400,7)],
             [(800, 3), (800, 5), (800,7)]]
tests = [item for sublist in tests_mtx for item in sublist ]

iter_times = 100

graph_time = []
time_mtx = []
len_mtx = []

labels = ['Breadth', 'Depth']

for i in range(len(tests)):

    
    n_nodes = tests[i][0]
    n_edges = tests[i][1]

    t = time.time()
    G, points = graph.makeGraph(n_nodes, n_edges)
    t_graph = time.time() - t

    print("Test " + str(i) + " - Nodes: " + str(n_nodes) + " , Edges: " + str(n_edges) + ": ")
    print("Made graph. Time taken: " + str(t_graph))
    
    # objective = [[np.random.randint(n_nodes), np.random.randint(n_nodes)] for i in range(iter_times)]
    objective = [[0, 77] for i in range(iter_times)]
    
    t_breadth_aux = []
    t_depth_aux = []
    for j in range(iter_times):

        t = time.time()
        breadth_way_str = gs.Breadth(G, objective[j][0], objective[j][1])
        t_breadth = time.time() - t
        breadth_way = breadth_way_str.split(' ')
        len_breadth = len(breadth_way)
        t_breadth_aux.append(t_breadth)
        
        t = time.time()
        depth_way_str = gs.Depth(G, objective[j][0], objective[j][1])
        t_depth = time.time() - t
        depth_way = depth_way_str.split(' ')
        len_depth =  len(depth_way)
        t_depth_aux.append(t_depth)
    
    t_breadth_mean = np.mean(t_breadth_aux)
    t_depth_mean = np.mean(t_depth_aux)
    
    print("------Breadth------")
    if breadth_way_str == '-1' :
        print("Not found!")
    else :
        # print("Found! The Breadth way is " + breadth_way_str)
        print('Found!')
    print("Time taken: " + str(t_breadth_mean))
    
    print("-------Depth-------")
    if depth_way_str == '-1' :
        print("Not found!")
    else :
        # print("Found! The Depth way is " + depth_way_str)
        print('Found!')
    print("Time taken: " + str(t_depth_mean))

    print("-------------------" + '\n')
    graph_time.append(t_graph)
    time_mtx.append([t_breadth_mean, t_depth_mean])
    # len_mtx.append([len_breadth, len_depth])

plot.plotNodesResults(tests_mtx, time_mtx, len_mtx, labels)