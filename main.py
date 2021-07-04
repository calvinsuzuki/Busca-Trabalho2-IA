from networkx.algorithms.operators.product import tensor_product
from networkx.classes.function import non_edges
import graph
import plot
import GraphSearch as gs
import time

# Test case = [(n_nodes, n_edges), ...]
tests_mtx = [[(100, 3), (200, 3), (300,3)],
             [(100, 5), (200, 5), (300,5)],
             [(100, 7), (200, 7), (300,7)]]
tests = [item for sublist in tests_mtx for item in sublist ]

graph_time = []
time_mtx = []
len_mtx = []


for i in range(len(tests)):

    n_nodes = tests[i][0]
    n_edges = tests[i][1]

    t = time.time()
    G, points = graph.makeGraph(n_nodes, n_edges)
    t_graph = time.time() - t

    print("Made graph. Time taken: " + str(t_graph) + '\n')

    t = time.time()
    breadth_way_str = gs.Breadth(G, 0, 10)
    t_breadth = time.time() - t
    breadth_way = breadth_way_str.split(' ')
    len_breadth = len(breadth_way)
    
    if breadth_way_str == '-1' :
        print("Not found!")
    else :
        print("Found! The Breadth way is " + breadth_way_str)
    print("Time taken: " + str(t_breadth) + "\n")
    print()

    t = time.time()
    depth_way_str = gs.Depth(G, 0, 10)
    t_depth = time.time() - t
    depth_way = depth_way_str.split(' ')
    len_depth =  len(depth_way)
    
    if depth_way_str == '-1' :
        print("Not found!")
    else :
        print("Found! The Depth way is " + depth_way_str)
    print("Time taken: " + str(t_depth))

    graph_time.append(t_graph)
    time_mtx.append([t_breadth, t_depth])
    len_mtx.append([len_breadth, len_depth])

plot.plotNodesResults(tests_mtx, time_mtx, len_mtx)