nodes = ["A", "B", "C", "D", "E"]

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "E"),
    ("D", "E")
]

adl = {}
def adjacency_list(edges):
    global adl 
    for key,value in edges:
        if key not in adl:
            adl[key] = []
        if value not in adl:
            adl[value] = []

        adl[key].append(value)
        # adl[value].append(key)

    print(adl)

adjacency_list(edges)

def bfs(node,visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return
     
    queue = [node]
    visited.add(node)
    while queue:
        popped = queue.pop(0)
        print(popped)
        for neighbours in adl[popped]:
            if neighbours not in visited:
                visited.add(neighbours)
                queue.append(neighbours)

bfs('A')

# def dfs(node,adl,visited=None):
#     if visited is None:
#         visited = set()

#     if node in visited:
#         return
    
#     visited.add(node)
#     print(node)

#     for neighbours in adl[node]:
#         dfs(node, adl, visited)

    


# dfs('A',adl)


# dfs('B',adl)
# def adjacency_matrix():
#     nodes = set()
#     for key,value in edges:
#         nodes.add(key)
#         nodes.add(value)
#     nodes = list(nodes)   
#     indexes = { nodes[i] : i for i in range(len(nodes))}
#     matrix = [[0]*len(nodes) for _ in range(len(nodes))]


#     for key, value in edges:
#         row = indexes[key]
#         col = indexes[value]
        
#         matrix[row][col] = 1
#         matrix[col][row] = 1

#     print(matrix)
#     print(indexes)



# adjacency_matrix()


