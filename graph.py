import numpy as np
import networkx as nx

def makeGraph(n_nodes, n_edges):
    
    nodes = __makeNodes(n_nodes)
    
    close_nodes = __getCloseNodes(nodes)
    
    edges = __makeEdges(close_nodes, n_edges)
    
    G = nx.Graph()
    
    G.add_nodes_from(np.arange(n_nodes))
    
    G.add_edges_from(edges)
    
    return G, nodes

def __makeNodes(n_nodes):
    # number of vertices is the max permited value too
    x = np.array([np.random.randint(n_nodes) for i in range(n_nodes)])
    y = np.array([np.random.randint(n_nodes) for i in range(n_nodes)])
    
    nodes = np.array([x, y]).T

    return nodes

def __getCloseNodes(nodes):
    
    close_nodes = []
    
    for i in range(len(nodes)):
        node_and_dist = []
        node = nodes[i]
        x = node[0]
        y = node[1]
        
        for j in range(len(nodes)):
            
            adj = nodes[j]
            
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
            
            if (node, curr_node) in edges:
                continue
            
            edges.append((curr_node, node))
            n_edges_per_node[curr_node]+=1
            n_edges_per_node[node]+=1
        
    return edges

if __name__=='__main__':
    makeGraph(5,5)
    
    
    