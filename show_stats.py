import numpy as np
import plot
import os

def plotMemory():
    with open(os.path.join('data','memory-data.npy'), 'rb') as f:
        memory_usage = np.load(f)

    plot.showMemoryUsage(memory_usage)
    plot.Show()

def plotLen():
    with open(os.path.join('data','len-100x.npy'), 'rb') as f:
        len_full = np.load(f)

    tests_mtx = [[(500, 3), (500,5), (500, 7)],
                [(5000, 3), (5000, 5), (5000, 7)],
                [(10000,3), (10000, 5), (10000, 7)]]

    labels = ['Largura', 'Profundidade', 'Best First', 'A', 'A*']
    plot.plotLenResults(tests_mtx, len_full[:,:,0], len_full[:,:,2], labels)
    plot.Show()
    
def plotTime():
    with open(os.path.join('data','time-100x.npy'), 'rb') as f:
        t_full = np.load(f)

    tests_mtx = [[(500, 3), (500,5), (500, 7)],
                    [(5000, 3), (5000, 5), (5000, 7)],
                    [(10000,3), (10000, 5), (10000, 7)]]

    labels = ['Largura', 'Profundidade', 'Best First', 'A', 'A*']

    plot.plotTimeResults(tests_mtx, t_full[:,:,0], t_full[:,:,2], labels)
    plot.Show()

def plotDist():
    with open(os.path.join('data','dist-100x.npy'), 'rb') as f:
        dist_full = np.load(f)

    tests_mtx = [[(500, 3), (500,5), (500, 7)],
                        [(5000, 3), (5000, 5), (5000, 7)],
                        [(10000,3), (10000, 5), (10000, 7)]]

    labels = ['Largura', 'Profundidade', 'Best First', 'A', 'A*']

    plot.plotDistResults(tests_mtx, dist_full[:,:,0], dist_full[:,:,2], labels)
    plot.Show()

print("Type 'q' to move to next plot!")
plotTime()
plotDist()
plotLen()
plotMemory()

