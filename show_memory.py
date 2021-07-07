import numpy as np
import plot

with open("memory-data.npy", 'rb') as f:
    memory_usage = np.load(f)
    
print(memory_usage)

plot.showMemoryUsage(memory_usage)
plot.Show()