def solution(n, computers):
    answer = []
    parent = [i for i in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i!=j and computers[i][j]==1:
                unionParent(parent, i, j)
    
    for k in range(len(parent)):
        answer.append(findParent(parent, parent[k]))
        
    answer = list(set(answer))
    return len(answer)
                
                
def findParent(parent, node):
    if parent[node] != node:
        parent[node] = findParent(parent, parent[node])
    return parent[node]

def unionParent(parent, node1, node2):
    node1 = findParent(parent, node1)
    node2 = findParent(parent, node2)
    
    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2
