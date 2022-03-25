from sys import stdin

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
G = int(stdin.readline())
P = int(stdin.readline())
gate = [0 for _ in range(P)]
parent = [i for i in range(G+1)]
docking = [False for _ in range(G+1)]
for i in range(P):
    gate[i] = int(stdin.readline())
    
count = 0
for i in range(P):
    j = find_parent(gate[i])    
    if j == 0:
        break
    if docking[j] == False:
        docking[j] = True
        count += 1
        flag = True
        parent[j] = parent[j-1]
print(count)
