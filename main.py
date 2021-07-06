from networkx.algorithms.operators.product import tensor_product
from networkx.classes.function import non_edges
import graph
import plot
import GraphSearch as gs
import numpy as np
import time

# Test case = [(n_nodes, n_edges), ...]
# tests_mtx = [[(200, 3), (200, 5), (200,7)],
#              [(400, 3), (400, 5), (400,7)],
#              [(800, 3), (800, 5), (800,7)]]
# tests_mtx = [[(200, 3), (200, 5), (200,7)],
#              [(400, 3), (400, 5), (400,7)]]
# tests_mtx = [[(500, 3)],
#              [(1000, 3)],
#              [(2000,3)]]
tests_mtx = [[(50, 3)],
             [(100, 3)],
             [(200,3)]]
tests = [item for sublist in tests_mtx for item in sublist ]

iter_times = 100

graph_time = []

time_mtx_mean = []
time_mtx_var = []
time_mtx_std = []

len_mtx_mean = []
len_mtx_var = []
len_mtx_std = []

labels = ['Breadth', 'Depth']

for i in range(len(tests)):

    n_nodes = tests[i][0]
    n_edges = tests[i][1]

    t = time.time()
    G, points = graph.makeGraph(n_nodes, n_edges)
    t_graph = time.time() - t

    print("Test " + str(i) + " - Nodes: " + str(n_nodes) + " , Edges: " + str(n_edges) + ": ")
    print("Made graph. Time taken: " + str(t_graph))
    
    objective = [[np.random.randint(n_nodes), np.random.randint(n_nodes)] for i in range(iter_times)]
    # objective = [[0, 77] for i in range(iter_times)]
    
    t_breadth_aux = []
    t_depth_aux = []
    len_breadth_aux = []
    len_depth_aux = []
    for j in range(iter_times):

        t = time.time()
        breadth_way_str = gs.Breadth(G, objective[j][0], objective[j][1])
        t_breadth = time.time() - t
        
        t_breadth_aux.append(t_breadth)
        
        breadth_way = breadth_way_str.split(' ')
        len_breadth = len(breadth_way)
        if len_breadth>=1:
            len_breadth_aux.append(len_breadth)
        
        t = time.time()
        depth_way_str = gs.Depth(G, objective[j][0], objective[j][1])
        t_depth = time.time() - t

        t_depth_aux.append(t_depth)
        
        depth_way = depth_way_str.split(' ')
        len_depth = len(depth_way)
        if len_depth>=1:
            len_depth_aux.append(len_depth)
            
    t_breadth_mean = np.mean(t_breadth_aux)
    t_breadth_var = np.var(t_breadth_aux)
    t_breadth_std = np.std(t_breadth_aux)
    
    t_depth_mean = np.mean(t_depth_aux)
    t_depth_var = np.var(t_depth_aux)
    t_depth_std = np.std(t_depth_aux)
    max_td = max(t_breadth_aux)
    
    len_breadth_mean = np.mean(len_breadth_aux)
    len_breadth_var = np.var(len_breadth_aux)
    len_breadth_std = np.std(len_breadth_aux)
    
    len_depth_mean = np.mean(len_depth_aux)
    len_depth_var = np.var(len_depth_aux)
    len_depth_std = np.std(len_depth_aux)
    
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
    print(max_td)
    
    graph_time.append(t_graph)
    time_mtx_mean.append([t_breadth_mean, t_depth_mean])
    time_mtx_var.append([t_breadth_var, t_depth_var])
    time_mtx_std.append([t_breadth_std, t_depth_std])
    
    len_mtx_mean.append([len_breadth_mean, len_depth_mean])
    len_mtx_var.append([len_breadth_var, len_depth_var])
    len_mtx_std.append([len_breadth_std, len_depth_std])
    # len_mtx.append([len_breadth, len_depth])

print(f'Time mean: {np.array(time_mtx_mean)}')
print(f'Time var: {np.array(time_mtx_var)}')
print(f'Time std: {np.array(time_mtx_std)}')

print(f'Len mean: {np.array(len_mtx_mean)}')
print(f'Len var: {np.array(len_mtx_var)}')
print(f'Len std: {np.array(len_mtx_std)}')

plot.plotTimeResults(tests_mtx, time_mtx_mean, time_mtx_std, labels)
plot.plotLenResults(tests_mtx, len_mtx_mean, len_mtx_std, labels)