import numpy as np
import plot 
import networkx as nx

def makeGraph(n_nodes, n_edges):
    
    points = __makePoints(n_nodes)
    
    close_nodes = __getCloseNodes(points)
    
    edges = __makeEdges(close_nodes, n_edges)
    
    G = nx.Graph()
    
    G.add_nodes_from(np.arange(n_nodes))
    
    G.add_edges_from(edges)
    
    return G, points

def savePointsAndEdges(file, n_nodes, n_edges):
    
    points = __makePoints(n_nodes)
    
    close_nodes = __getCloseNodes(points)
    
    edges = __makeEdges(close_nodes, n_edges)
    
    with open(file, 'wb') as f:
        np.save(f, points)
        np.save(f, edges)

def loadNodesAndMakeGraph(file_name):
    
    with open(file_name, 'rb') as f:
        points = np.load(f)
        edges = np.load(f)
    
    G = nx.Graph()
    
    G.add_nodes_from(np.arange(len(points)))
    
    G.add_edges_from(edges)
    
    return G, points
    

def __makePoints(n_nodes):
    
    # # number of vertices is the max permited value too
    # x = np.array([np.random.randint(n_nodes) for i in range(n_nodes)])
    # y = np.array([np.random.randint(n_nodes) for i in range(n_nodes)])
    
    points = []
    for i in range(n_nodes):
        points_aux = [np.random.randint(n_nodes), np.random.randint(n_nodes)]
        
        while True:
            if points_aux in points:
                points_aux = [np.random.randint(n_nodes), np.random.randint(n_nodes)]
                continue
            else:
                break

        points.append(points_aux)
    
    return np.array(points)

def __getCloseNodes(points):
    
    close_nodes = []
    
    for i in range(len(points)):
        node_and_dist = []
        curr = points[i]
        x = curr[0]
        y = curr[1]
        
        for j in range(len(points)):
            
            adj = points[j]
            
            if i == j:
                continue
            
            x_adj = adj[0]
            y_adj = adj[1]

            distance = np.sqrt((x-x_adj)**2+(y-y_adj)**2)
            node_and_dist.append([j, distance])
        
        # print(node_and_dist[node_and_dist[:, 1].argsort()])
        node_and_dist = np.array(node_and_dist)
        node_and_dist = node_and_dist[np.argsort(node_and_dist[:, 1])]     
        
        # filtered_nodes = node_and_dist[:n_edges,0]
        
        close_nodes.append(node_and_dist[:,0])
        
    return np.array(close_nodes, dtype="uint16")
        
def __makeEdges(close_nodes_mtx, n_edges):
    
    edges = []
    
    n_edges_per_node = [0]*len(close_nodes_mtx)
    
    for curr_node in range(len(close_nodes_mtx)):
            
        close_nodes = close_nodes_mtx[curr_node]
        for node in close_nodes:
            
            if n_edges_per_node[curr_node] >= n_edges:
                continue 
            
            # if n_edges_per_node[node] >= n_edges:
            #     continue 
            
            # if (node, curr_node) in edges:
            #     continue
            
            edges.append((curr_node, node))
            n_edges_per_node[curr_node]+=1
            # n_edges_per_node[node]+=1
        
    return edges

if __name__=='__main__':
    # G, points = makeGraph(20,3)
    # plot.plotXY(G, points)
    # plot.Show()
    
    
    # savePointsAndEdges("5000-3.npy", 5000, 3)
    
    path = [1,2,3,5,4,6,9,10]
    
    G, points = loadNodesAndMakeGraph('5000-3.npy')
    
    figG, ax = plot.plotXY(G, points)
    plot.plotPath(ax, path, points, color = 'red', time = 5)
    plot.Show()