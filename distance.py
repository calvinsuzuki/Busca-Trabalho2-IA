import graph_maker as gm
import graph_search as gs
import plot
import numpy as np
import time
import os

def distance(way, points):
        
    dist = 0
    for i in range(len(way)-1):
        dist += np.sqrt((points[way[i+1]][0]-points[way[i]][0])**2+(points[way[i+1]][1]-points[way[i]][1])**2)
    return dist

tests_mtx = [[(500, 3), (500,5), (500, 7)],
             [(5000, 3), (5000, 5), (5000, 7)],
             [(10000,3), (10000, 5), (10000, 7)]]
# tests_mtx = [[(100, 3)],
#              [(100, 3)],
#              [(100,3)]]

tests = [item for sublist in tests_mtx for item in sublist ]

iter_times = 1

dist_mtx = []

row = 0
dist_breadth_stat, dist_depth_stat, dist_bestf_stat, dist_A_stat, dist_Astar_stat = [],[],[],[],[]
for i in range(len(tests)):
        
    test = tests[i]
    n_nodes = test[0]
    n_edges = test[1]
    
    file = os.path.join('graphs', str(n_nodes) + '-' + str(n_edges) + '.npy')
    G, points = gm.loadNodesAndMakeGraph(file)

    objective = [[np.random.randint(n_nodes), np.random.randint(n_nodes)] for i in range(iter_times)]

    t_test = time.time()
    dist_breadth_aux, dist_depth_aux, dist_bestf_aux, dist_A_aux, dist_Astar_aux = [], [], [], [], []
    for j in range(iter_times):
        os.system("clear")
        print("Teste: " + str(i) + ": " + str(j*100/iter_times) + "%")
        
        origin = objective[j][0]
        target = objective[j][1]
        
        way_breadth = gs.Breadth(G, origin, target)
        dist_breadth = distance(way_breadth, points)
        
        way_depth = gs.Depth(G, origin, target)
        dist_depth = distance(way_depth, points)

        way_bestf = gs.BestFirst(G, points, origin, target)
        dist_bestf = distance(way_bestf, points)

        way_A = gs.ASearch(G, points, origin, target)
        dist_A = distance(way_A, points)

        way_Astar = gs.Asterix(G, points, origin, target)
        dist_Astar = distance(way_Astar, points)
    
        dist_breadth_aux.append(dist_breadth)
        dist_depth_aux.append(dist_depth)
        dist_bestf_aux.append(dist_bestf)
        dist_A_aux.append(dist_A)
        dist_Astar_aux.append(dist_Astar)
    
    dist_breadth_stat = [np.mean(dist_breadth_aux), np.var(dist_breadth_aux), np.std(dist_breadth_aux)]    
    dist_depth_stat = [np.mean(dist_depth_aux), np.var(dist_depth_aux), np.std(dist_depth_aux)]
    dist_bestf_stat = [np.mean(dist_bestf_aux), np.var(dist_bestf_aux), np.std(dist_bestf_aux)]
    dist_A_stat = [np.mean(dist_A_aux), np.var(dist_A_aux), np.std(dist_A_aux)]
    dist_Astar_stat = [np.mean(dist_Astar_aux), np.var(dist_Astar_aux), np.std(dist_Astar_aux)]

    dist_mtx.append([dist_breadth_stat, dist_depth_stat, dist_bestf_stat, dist_A_stat, dist_Astar_stat])
    
    t_test = time.time() - t_test

dist_mtx = np.array(dist_mtx)

print(dist_mtx)

# num = 1
# file = 'dist-25' + str(num) + '.npy'
# with open(file, 'wb') as f:
#     np.save(f, dist_mtx)

labels = ['Largura', 'Profundidade', 'Best First', 'A', 'A*']

plot.plotDistResults(tests_mtx, dist_mtx[:,:,0], dist_mtx[:,:,2], labels)
plot.Show()

