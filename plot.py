import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def plotGraph(graph):
    
    plt.plot()
    
    nx.draw(graph, with_labels=True, font_weight='bold')

    plt.show()

def plotXY(graph, points, label_u = False):
    
    edges = list(graph.edges)
    figG = plt.figure()
    ax = plt.axes()
    
    for edge in edges:
        x_vec = [points[edge[0]][0], points[edge[1]][0]]
        y_vec = [points[edge[0]][1], points[edge[1]][1]]
        ax.plot(x_vec, y_vec, color = 'dimgray', linewidth=1)
        
    ax.scatter(points[:,0], points[:,1], color = 'black', s=5)
    
    if len(points)>=100:
        label = False
    
    label = label_u
    
    if label:
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            label = "{}".format(i)

            ax.annotate(label, # this is the text
                        (x,y), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,5), # distance from text to points (x,y)
                        ha='center', fontsize = 7) # horizontal alignment can be left, right or center

    return figG, ax 

def plotPath(ax, path, points, color = 'red', wait = 3):
    
    max_i =len(path)-2
    
    for i in range(max_i):
        x_vec = [points[path[i]][0], points[path[i+1]][0]]
        y_vec = [points[path[i]][1], points[path[i+1]][1]]
        
        ax.plot(x_vec, y_vec, color = color)
        plt.show(block=False)
        plt.pause(wait)
        
    return ax

def PlotVisitedNodes(ax, visited, color):
    
    # for i in range(len(visited)):
    #     ax.scatter()
    pass

def animate():
    
    plt.show(block=False)
    plt.pause(0.5)
    
    


def plotTimeResults(tests_mtx, time_mtx_mean, time_mtx_std, labels):
    
    nrows = len(tests_mtx)
    ncols = len(tests_mtx[0])
    nmethods = len(time_mtx_mean[0])
    
    plt.style.use('ggplot')
    plt.rcParams.update({'font.size': 7})
    
    if ncols != 1:
        figT, axs = plt.subplots(nrows, ncols, constrained_layout = True)
    else:
        figT, axs = plt.subplots(nrows)
    
    figT.tight_layout(pad=3.0)
    
    print("Making a {},{} graphic.".format(nrows, ncols))
    
    x = np.arange(nmethods)/2
    
    ntest = 0
    for i in range(nrows):
        
        time_mtx_mean = np.array(time_mtx_mean)
        time_mtx_std = np.array(time_mtx_std)
        ylim = np.max(time_mtx_mean[ntest:ntest+ncols,:]) + np.max(time_mtx_std[ntest:ntest+ncols,:])
        # print(ylim)
        ylim = 1.2*1000*ylim
        
        for j in range(ncols):
            
            if ncols != 1:
                axs[i][j].bar(x, np.array(time_mtx_mean[ntest])*1000, 0.2, yerr = np.array(time_mtx_std[ntest])*1000, align='center',
                            alpha=0.7, ecolor='black', capsize=10, color = 'blue')
                axs[i][j].set_xticks(x)
                if j==0:
                    axs[i][j].set_ylabel('Tempo médio (ms)', fontsize=7)
                axs[i][j].set_xticklabels(labels)
                axs[i][j].set_title('v = {}, a = {}'.format(tests_mtx[i][j][0], tests_mtx[i][j][1]), fontsize=7)
                axs[i][j].set_ylim([0, ylim])
            
            else:
                axs[ntest].bar(x, np.array(time_mtx_mean[ntest])*1000, 0.2, yerr = np.array(time_mtx_std[ntest])*1000, align='center',
                            alpha=0.7, ecolor='black', capsize=10, color = 'blue')
                axs[ntest].set_xticks(x)                
                axs[ntest].set_ylabel('Tempo médio (ms)', fontsize=7)
                axs[ntest].set_xticklabels(labels)
                axs[ntest].set_title('v = {}, a = {}'.format(tests_mtx[i][j][0], tests_mtx[i][j][1]), fontsize=7)
                axs[ntest].set_ylim([0, ylim])
            ntest += 1 
    # set the spacing between subplots
    # figT.tight_layout()
    
    
def plotLenResults(tests_mtx, len_mtx_mean, len_mtx_std, labels):
    
    nrows = len(tests_mtx)
    ncols = len(tests_mtx[0])
    nmethods = len(len_mtx_mean[0])
    
    plt.style.use('ggplot')
    plt.rcParams.update({'font.size': 7})
    
    if ncols != 1:
        figL, axs = plt.subplots(nrows, ncols, constrained_layout = True)
    else:
        figL, axs = plt.subplots(nrows)
    
    
    figL.tight_layout(pad=3.0)
        
    print("Making a {},{} graphic.".format(nrows, ncols))
    
    x = np.arange(nmethods)/2
    
    ntest = 0
    for i in range(nrows):
        
        len_mtx_mean = np.array(len_mtx_mean)
        len_mtx_std = np.array(len_mtx_std)
        ylim = np.max(len_mtx_mean[ntest:ntest+ncols,:]) + np.max(len_mtx_std[ntest:ntest+ncols,:])
        # print(ylim)
        ylim = ylim*1.2
        # print(ylim)
        
        for j in range(ncols):
            
            if ncols != 1:
                axs[i][j].bar(x, np.array(len_mtx_mean[ntest]), 0.2, yerr = np.array(len_mtx_std[ntest]), align='center',
                            alpha=0.7, ecolor='black', capsize=10, color = 'red')
                axs[i][j].set_xticks(x)
                if j==0:
                    axs[i][j].set_ylabel('Tamanho médio (vértices)', fontsize = 7)
                axs[i][j].set_xticklabels(labels)
                axs[i][j].set_title('v = {}, a = {}'.format(tests_mtx[i][j][0], tests_mtx[i][j][1]), fontsize=7)
                axs[i][j].set_ylim([0, ylim])
            
            else:
                axs[ntest].bar(x, np.array(len_mtx_mean[ntest]), 0.2, yerr = np.array(len_mtx_std[ntest]), align='center',
                            alpha=0.7, ecolor='black', capsize=5, color = 'red')
                axs[ntest].set_xticks(x)                
                axs[ntest].set_ylabel('Tamanho médio (vértices)', fontsize = 7)
                axs[ntest].set_xticklabels(labels)
                axs[ntest].set_title('v = {}, a = {}'.format(tests_mtx[i][j][0], tests_mtx[i][j][1]), fontsize=7)
                axs[ntest].set_ylim([0, ylim])
            ntest += 1 
    
def Show():
    plt.show()
    