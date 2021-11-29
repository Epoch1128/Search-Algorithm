"""
Config:
graph: [1, 2, 3, 
        8, 0, 4,
        7, 6, 5]
"""
import numpy as np

adj = np.zeros(shape=(9, 9), dtype=np.int)
for i in range(1, 8):
    adj[i][i+1] = 1

for j in [2, 4, 6, 8]:
    adj[0][j] = 1

adj[1][8] = 1

adj += np.transpose(adj)

max_epoch = 1000
