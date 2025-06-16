#%%
import random
import matplotlib.pyplot as plt
import numpy as np
import time

#%% Node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None 

#%% KDTree
class KDTree:
    def __init__(self, keys):
        self.root = self.buildKDTree(keys)

    def buildKDTree(self, keys, depth=0):
        if not keys:
            return None
        axis = depth % 2
        keys.sort(key=lambda key: key[axis])
        med = len(keys) // 2
        node = Node(keys[med])
        node.left = self.buildKDTree(keys[:med], depth + 1)
        node.right = self.buildKDTree(keys[med + 1:], depth + 1)
        return node

    def search(self, keys):
        start = time.perf_counter()
        for key in keys:
            self._search(self.root, key, 0)
        end = time.perf_counter()
        return end - start

    def _search(self, root, key, depth):
        if not root:
            return
        if root.key == key:
            return
        axis = depth % 2
        if key[axis] < root.key[axis]:
            self._search(root.left, key, depth + 1)
        else:
            self._search(root.right, key, depth + 1)
            
    def printTree(self):
        self._printTree(self.root, "", True)
    
    def _printTree(self, node, prefix, isTail):
        if node.right:
            newPrefix = prefix + ("│   " if isTail else "    ")
            self._printTree(node.right, newPrefix, False)
        print(prefix + ("└──" if isTail else "┌──") + f"{node.key[0]},{node.key[1]}")
        if node.left:
            newPrefix = prefix + ("    " if isTail else "│   ")
            self._printTree(node.left, newPrefix, True)

#%%            
nKeys = list(range(10000, 100000, 10000))
speed = []

for n in nKeys:
    tests = []
    for _ in range(10):
        keys = [(random.randint(0, 99), random.randint(0, 99)) for _ in range(n)]
        tree = KDTree(keys)
        tests.append(tree.search(keys))
    speed.append(tests)

speed = np.array(speed)
np.savetxt("speed.txt", speed, fmt="%.5f", delimiter=',')

for i, n in enumerate(nKeys):
    for t in speed[i]:
        plt.scatter(n, t*1000, color=(0, 0, 0.502), s=5)

avgSpeed = speed.mean(axis=1)
coef = np.polyfit(nKeys, avgSpeed, 2)
func = np.poly1d(coef)
xFit = np.linspace(min(nKeys), max(nKeys), 100)
plt.plot(xFit, func(xFit)*1000, color=(0, 0, 0.502))


# Título e labels
plt.title("Tempo de Busca x Tamanho da Entrada")
plt.xlabel("Quantidade de Entradas")
plt.ylabel("Tempo de Execução (ms)")
plt.grid(True)

# Salvar imagem
plt.savefig("grafico_kdtree.png", dpi=300)