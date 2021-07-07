from networkx.algorithms.operators.product import tensor_product
from networkx.classes.function import non_edges
import graph_maker as graph
import plot
import graph_search as gs
import numpy as np
import time
import os

def getLoadedGraph(n_nodes, n_edges):
    file = "graphs/" + str(n_nodes) + '-' + str(n_edges) + '.npy'
    return graph.loadNodesAndMakeGraph(file)

# Test case = [(n_nodes, n_edges), ...]
# tests_mtx = [[(200, 3), (200, 5), (200,7)],
#              [(400, 3), (400, 5), (400,7)],
#              [(800, 3), (800, 5), (800,7)]]
# tests_mtx = [[(200, 3), (200, 5), (200,7)],
#              [(400, 3), (400, 5), (400,7)]]
# tests_mtx = [[(500, 3)],
#              [(1000, 3)],
#              [(2000,3)]]
tests_mtx = [[(500, 3), (500,5), (500, 7)],
             [(5000, 3), (5000, 5), (5000, 7)],
             [(10000,3), (10000, 5), (10000, 7)]]

tests = [item for sublist in tests_mtx for item in sublist ]

iter_times = 50

graph_time = []

t_mtx_stat = []

len_mtx_stat = []

for i in range(len(tests)):

    n_nodes = tests[i][0]
    n_edges = tests[i][1]

    # t = time.time()
    # G, points = graph.makeGraph(n_nodes, n_edges)
    # t_graph = time.time() - 
    
    G, points = getLoadedGraph(n_nodes, n_edges)

    # print("Test " + str(i) + " - Nodes: " + str(n_nodes) + " , Edges: " + str(n_edges) + ": ")
    # print("Made graph. Time taken: " + str(t_graph))C
    
    objective = [[np.random.randint(n_nodes), np.random.randint(n_nodes)] for i in range(iter_times)]
    # objective = [[0, 77] for i in range(iter_times)]
    
    # Time aux for each method
    t_breadth_aux = []
    t_depth_aux = []
    t_bestf_aux = []
    t_A_aux = []
    t_Astar_aux = []
    
    # Len aux for each method
    len_breadth_aux = []
    len_depth_aux = []
    len_bestf_aux = []
    len_A_aux = []
    len_Astar_aux = []
    
    t_test = time.time()
    # Do search for each algorithm iter_times 
    for j in range(iter_times):

        os.system("clear")
        print("Teste: " + str(i) + ": " + str(j*100/iter_times) + "%")

        # -----Breadth-----
        t = time.time()
        breadth_way = gs.Breadth(G, objective[j][0], objective[j][1])
        t_breadth_aux.append(time.time() - t)
        
        if len(breadth_way) >= 1:
            len_breadth_aux.append(len(breadth_way))
        
        # -----Depth-----
        t = time.time()
        depth_way = gs.Depth(G, objective[j][0], objective[j][1])
        t_depth_aux.append(time.time() - t)
        
        if len(depth_way) >= 1:
            len_depth_aux.append(len(depth_way))
        
        # -----Best First-----
        t = time.time()
        bestf_way = gs.BestFirst(G, points, objective[j][0], objective[j][1])
        t_bestf_aux.append(time.time() - t)
        
        if len(bestf_way) >= 1:
            len_bestf_aux.append(len(bestf_way))
        
        # -----A-----
        t = time.time()
        A_way = gs.ASearch(G, points, objective[j][0], objective[j][1])
        t_A_aux.append(time.time() - t)
        
        if len(A_way) >= 1:
            len_A_aux.append(len(A_way))
        
        # -----Astar-----
        t = time.time()
        Astar_way = gs.Asterix(G, points, objective[j][0], objective[j][1])
        t_Astar_aux.append(time.time() - t)
        
        if len(Astar_way) >= 1:
            len_Astar_aux.append(len(Astar_way))
    
    # Time array for each method that agroups all tests cases    
    t_breadth_stat = np.array([np.mean(t_breadth_aux), np.var(t_breadth_aux), np.std(t_breadth_aux)])
    t_depth_stat = np.array([np.mean(t_depth_aux), np.var(t_depth_aux), np.std(t_depth_aux)])
    t_bestf_stat =  np.array([np.mean(t_bestf_aux), np.var(t_bestf_aux), np.std(t_bestf_aux)])
    t_A_stat =  np.array([np.mean(t_A_aux), np.var(t_A_aux), np.std(t_A_aux)])
    t_Astar_stat =  np.array([np.mean(t_Astar_aux), np.var(t_Astar_aux), np.std(t_Astar_aux)])
    
    # Len array for each method that agroups all tests cases
    len_breadth_stat = np.array([np.mean(len_breadth_aux), np.var(len_breadth_aux), np.std(len_breadth_aux)])
    len_depth_stat = np.array([np.mean(len_depth_aux), np.var(len_depth_aux), np.std(len_depth_aux)])
    len_bestf_stat =  np.array([np.mean(len_bestf_aux), np.var(len_bestf_aux), np.std(len_bestf_aux)])
    len_A_stat =  np.array([np.mean(len_A_aux), np.var(len_A_aux), np.std(len_A_aux)])
    len_Astar_stat =  np.array([np.mean(len_Astar_aux), np.var(len_Astar_aux), np.std(len_Astar_aux)])
    
    
    t_test = time.time() - t_test
    # print("Done!")
    # print(f"Test time taken: {t_test}")
    # print("-------------------" + '\n')
    
    # graph_time.append(t_graph)
    
    t_mtx_stat.append([t_breadth_stat, t_depth_stat, t_bestf_stat, t_A_stat, t_Astar_stat])
    
    len_mtx_stat.append([len_breadth_stat, len_depth_stat, len_bestf_stat, len_A_stat, len_Astar_stat])

t_mtx_stat = np.array(t_mtx_stat)
len_mtx_stat = np.array(len_mtx_stat)

print(np.array(t_mtx_stat))

print(np.array(len_mtx_stat))

labels = ['Largura', 'Profundidade', 'Best First', 'A', 'A*']

plot.plotTimeResults(tests_mtx, t_mtx_stat[:,:,0], t_mtx_stat[:,:,2], labels)
plot.plotLenResults(tests_mtx, len_mtx_stat[:,:,0], len_mtx_stat[:,:,2], labels)
plot.Show()
