import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Plota o grafo
def plotGraph(graph):
    
    plt.plot()
    
    nx.draw(graph, with_labels=True, font_weight='bold')

    plt.show()

# Plota todos os pontos de um grafo
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

# Desenha um caminho sobre os pontos de um certo caminho
def plotPath(ax, path, points, animate, color = 'red', linewidth=3, wait = 0.001):
    
    max_i =len(path)-1

    x = points[path[0]][0]
    y = points[path[0]][1]
    plt.scatter(x,y,color = 'red')

    x = points[path[len(path)-1]][0]
    y = points[path[len(path)-1]][1]
    plt.scatter(x,y,color = 'green')

    for i in range(max_i):
        x_vec = [points[path[i]][0], points[path[i+1]][0]]
        y_vec = [points[path[i]][1], points[path[i+1]][1]]
        
        ax.plot(x_vec, y_vec, color = color, linewidth=linewidth)
        if animate:
            plt.show(block=False)
            plt.pause(wait=wait)
        
    return ax

# Grafica os comparativos de tempo
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
                            alpha=0.7, ecolor='black', capsize=5, color = 'blue')
                axs[i][j].set_xticks(x)
                if j==0:
                    axs[i][j].set_ylabel('Tempo médio (ms)', fontsize=7)
                axs[i][j].set_xticklabels(labels)
                axs[i][j].set_title('v = {}, a = {}'.format(tests_mtx[i][j][0], tests_mtx[i][j][1]), fontsize=7)
                axs[i][j].set_ylim([0, ylim])
                for k in range(nmethods):
                    axs[i][j].text(x[k] + 0.05, time_mtx_mean[ntest][k]*1000 + 1.1, str(round(time_mtx_mean[ntest][k]*1000,0)))
            
            else:
                axs[ntest].bar(x, np.array(time_mtx_mean[ntest])*1000, 0.2, yerr = np.array(time_mtx_std[ntest])*1000, align='center',
                            alpha=0.7, ecolor='black', capsize=5, color = 'blue')
                axs[ntest].set_xticks(x)                
                axs[ntest].set_ylabel('Tempo médio (ms)', fontsize=7)
                axs[ntest].set_xticklabels(labels)
                axs[ntest].set_title('v = {}, a = {}'.format(tests_mtx[i][j][0], tests_mtx[i][j][1]), fontsize=7)
                axs[ntest].set_ylim([0, ylim])
                for k in range(nmethods):
                    axs[ntest].text(x[k] + 0.05, time_mtx_mean[ntest][k]*1000 + 1.1, str(round(time_mtx_mean[ntest][k]*1000,0)))
            ntest += 1 
    # set the spacing between subplots
    # figT.tight_layout()

# Grafica os comparativos de distância em vértices 
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
                            alpha=0.7, ecolor='black', capsize=5, color = 'red')
                axs[i][j].set_xticks(x)
                if j==0:
                    axs[i][j].set_ylabel('Tamanho médio (vértices)', fontsize = 7)
                axs[i][j].set_xticklabels(labels)
                axs[i][j].set_title('v = {}, a = {}'.format(tests_mtx[i][j][0], tests_mtx[i][j][1]), fontsize=7)
                axs[i][j].set_ylim([0, ylim])
                for k in range(nmethods):
                    axs[i][j].text(x[k] + 0.05,len_mtx_mean[ntest][k] + 1.1, str(round(len_mtx_mean[ntest][k],0)))
            else:
                axs[ntest].bar(x, np.array(len_mtx_mean[ntest]), 0.2, yerr = np.array(len_mtx_std[ntest]), align='center',
                            alpha=0.7, ecolor='black', capsize=5, color = 'red')
                axs[ntest].set_xticks(x)                
                axs[ntest].set_ylabel('Tamanho médio (vértices)', fontsize = 7)
                axs[ntest].set_xticklabels(labels)
                axs[ntest].set_title('v = {}, a = {}'.format(tests_mtx[i][j][0], tests_mtx[i][j][1]), fontsize=7)
                axs[ntest].set_ylim([0, ylim])
                for k in range(nmethods):
                    axs[ntest].text(x[k] + 0.05,len_mtx_mean[ntest][k] + 1.1, str(round(len_mtx_mean[ntest][k],0)))
            ntest += 1 

# Grafica os comparativos de distância euclidiana percorrida
def plotDistResults(tests_mtx, dist_mtx_mean, dist_mtx_std, labels):
    
    nrows = len(tests_mtx)
    ncols = len(tests_mtx[0])
    nmethods = len(dist_mtx_mean[0])
    
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
        
        dist_mtx_mean = np.array(dist_mtx_mean)
        dist_mtx_std = np.array(dist_mtx_std)
        ylim = np.max(dist_mtx_mean[ntest:ntest+ncols,:]) + np.max(dist_mtx_std[ntest:ntest+ncols,:])
        # print(ylim)
        ylim = 1.2*ylim
        
        for j in range(ncols):
            
            if ncols != 1:
                axs[i][j].bar(x, dist_mtx_mean[ntest], 0.2, yerr = dist_mtx_std[ntest], align='center',
                            alpha=0.7, ecolor='black', capsize=5, color = 'cyan')
                axs[i][j].set_xticks(x)
                if j==0:
                    axs[i][j].set_ylabel('Distância média', fontsize=7)
                axs[i][j].set_xticklabels(labels)
                axs[i][j].set_title('v = {}, a = {}'.format(tests_mtx[i][j][0], tests_mtx[i][j][1]), fontsize=7)
                axs[i][j].set_ylim([0, ylim])
                for k in range(nmethods):
                    axs[i][j].text(x[k] + 0.05,dist_mtx_mean[ntest][k] + 1.1, str(round(dist_mtx_mean[ntest][k],0)))
            
            else:
                axs[ntest].bar(x, dist_mtx_mean[ntest], 0.2, yerr = dist_mtx_std[ntest], align='center',
                            alpha=0.7, ecolor='black', capsize=5, color = 'cyan')
                axs[ntest].set_xticks(x)                
                axs[ntest].set_ylabel('Distância média', fontsize=7)
                axs[ntest].set_xticklabels(labels)
                axs[ntest].set_title('v = {}, a = {}'.format(tests_mtx[i][j][0], tests_mtx[i][j][1]), fontsize=7)
                axs[ntest].set_ylim([0, ylim])
                
                for k in range(nmethods):
                    axs[ntest].text(x[k] + 0.05,dist_mtx_mean[ntest][k] + 1.1, str(round(dist_mtx_mean[ntest][k],0)))
            
            ntest += 1 
            
# Grafica os comparativos de uso de memória por algoritmo
def showMemoryUsage(memory_usage):
    
    memory_usage = np.array(memory_usage)
    
    xlabels = ['(100,3)','(100,7)','(100,7)','(500,3)','(500,5)','(500,7)','(5000,3)','(5000,5)','(5000,7)','(10000,3)','(10000,5)','(10000,7)']
    
    plt.style.use('ggplot')
    plt.rcParams.update({'font.size': 10})
    figM = plt.figure()
    ax = plt.axes()
    
    ax.set_xticks(np.arange(12))
    ax.set_xticklabels(xlabels)
    ax.set_xlabel('(Vértices, Arestas)')
    ax.set_ylabel('Alocação máxima (kB)')
    ax.set_ylim([0,800])
    
    colors = ['red', 'blue', 'darkorange', 'm', 'green']
    labels = ['Largura', 'Profundidade', 'Best First', 'A', 'A*']
    
    for i in range(len(memory_usage[0])):
        if i == 1:
            continue
        ax.plot(memory_usage[:,i]/1000, '-o', color = colors[i], label = labels[i])
    
    ax2 = ax.twinx()
    ax2.plot(memory_usage[:,1]/1000, marker=9, color='blue', linestyle = '--', label = 'Profundidade')
    ax2.set_yscale('log', base=10)
    ax2.tick_params(axis='y')
    ax2.set_ylabel('Alocação máxima em log. (kB) ')
    
    ax.legend(loc='center left', title = "Escala linear")
    ax2.legend(loc='upper left', title = "Escala log.")

def legends(handles):
    plt.legend(handles=handles)

def Show():
    plt.show()