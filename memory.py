import graph_maker as gm
import graph_search as gs
import plot
import numpy as np
import os

import tracemalloc

tests = [[100, 3], [100, 5], [100, 7], [500, 3], [500, 5], [500, 7], [5000, 3], [5000, 5], [5000, 7], [10000, 3], [10000, 5], [10000, 7]]
critical_points = [[45, 83], [34, 63], [15, 24], [136, 318], [285, 98], [28, 133], [553, 1780], [179, 1722], [1978, 4043], [5157, 6698], [2106, 417], [377, 2880]]

# tests = [[10000,7]]
# critical_points = [[377, 2880]]

memory_usage = []

# Itera para cada test na lista
for i in range(len(tests)):
    
    test = tests[i]
    n_nodes = test[0]
    n_edges = test[1]
    
    # Carrega o grafo
    file = os.path.join('graphs', str(n_nodes) + '-' + str(n_edges) + '.npy')
    G, points = gm.loadNodesAndMakeGraph(file)

    # Set ponto inicial e objetivo
    origin = critical_points[i][0]
    target = critical_points[i][1]
    
    # Inicia a analise
    print(f"Test {i} - Nodes: {n_nodes}, Edges: {n_edges} - Critical point: ({origin},{target})")
    # ------------------Breadth
    tracemalloc.clear_traces()
    tracemalloc.start()

    way = gs.Breadth(G, origin, target)

    size, peak_Breadth = tracemalloc.get_traced_memory()

    print(f"Breadth: Size: {size}, Peak: {peak_Breadth}")

    # ------------------Depth
    tracemalloc.clear_traces()
    tracemalloc.start()

    way = gs.Depth(G, origin, target)

    size, peak_Depth = tracemalloc.get_traced_memory()

    print(f"Depth: Size: {size}, Peak: {peak_Depth}")

    # ------------------Best First
    tracemalloc.clear_traces()
    tracemalloc.start()

    way = gs.BestFirst(G, points, origin, target)

    size, peak_Bestf = tracemalloc.get_traced_memory()

    print(f"Best First: Size: {size}, Peak: {peak_Bestf}")

    # ------------------A
    tracemalloc.clear_traces()
    tracemalloc.start()

    way = gs.ASearch(G, points, origin, target)

    size, peak_A = tracemalloc.get_traced_memory()

    print(f"A: Size: {size}, Peak: {peak_A}")

    # --------------------------Astar
    tracemalloc.clear_traces()
    tracemalloc.start()

    way = gs.Asterix(G, points, origin, target)

    size, peak_Astar = tracemalloc.get_traced_memory()

    print(f"Astar: Size: {size}, Peak: {peak_Astar}")

    memory_usage.append([peak_Breadth, peak_Depth, peak_Bestf, peak_A, peak_Astar])

## Save memory usage
# with open("memory-data.npy", 'wb') as f:
#     np.save(f, memory_usage)

print("Complete. Showing results!")
plot.showMemoryUsage(memory_usage)
plot.Show()
        
    # snapshot = tracemalloc.take_snapshot()
    # filtr = tracemalloc.DomainFilter(inclusive=False, domain=0)
    # snapshot = snapshot.filter_traces(filters=[filtr])

    # for stat in snapshot.statistics("lineno"):
    #     print(stat.traceback.format())
    #     print(stat)