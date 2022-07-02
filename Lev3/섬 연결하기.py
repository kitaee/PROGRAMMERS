def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])
    
    for cost in costs:
        if find_Parent(parent, cost[0]) != find_Parent(parent, cost[1]):
            union_Parent(parent, cost[0], cost[1])
            answer+=cost[2]
    return answer

def find_Parent(parent, n):
    if parent[n] != n:
        parent[n] = find_Parent(parent, parent[n])
    return parent[n]
    
def union_Parent(parent, a, b):
    a = find_Parent(parent, a)
    b = find_Parent(parent, b)
    
    if a>b:
        parent[a] = b
    else:
        parent[b] = a
