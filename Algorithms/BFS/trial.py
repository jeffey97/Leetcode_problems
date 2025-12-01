graph={
    'A':['B','C'],
     'B':['D','E'],
     'C': ['F'],
     'D':['G','H'],
     'E':['I'],
     'F':['J','K'],
     'G':[],
     'H':['L'],
     'I': ['M','N'],
     'J':[],
     'K':[],
     'L':[],
     'M':[],
    'N':['O'],
    'O':[]
}

def dfs(node, visited=None):
    if visited is None:
       visited = set()

    print(node)
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour,visited)


dfs('A')