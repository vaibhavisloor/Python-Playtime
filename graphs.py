nodes = ["A", "B", "C", "D", "E"]

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "E"),
    ("D", "E")
]

# def adjacency_list(edges):
#     adl = {}

#     for key,value in edges:
#         if key not in adl:
#             adl[key] = []
#         if value not in adl:
#             adl[value] = []

#         adl[key].append(value)
#         adl[value].append(key)

#     print(adl)


def adjacency_matrix():
    nodes = set()
    for key,value in edges:
        nodes.add(key)
        nodes.add(value)
    nodes = list(nodes)   
    indexes = { nodes[i] : i for i in range(len(nodes))}
    matrix = [[0]*len(nodes) for _ in range(len(nodes))]


    for key, value in edges:
        row = indexes[key]
        col = indexes[value]
        
        matrix[row][col] = 1
        matrix[col][row] = 1

    print(matrix)
    print(indexes)



adjacency_matrix()