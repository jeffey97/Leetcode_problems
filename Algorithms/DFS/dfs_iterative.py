graph = {
       'A':['B','C'],
       'B':['D','E'],
       'C':['F'],
       'D':[],
       'E':[],
       'F':[]
}

def dfs_iterative(graph, start):

    stack = [start]
    visited = set()

    while stack:

        node = stack.pop()

        if node not in visited:
            print(node) 
            visited.add(node)

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
               stack.append(neighbour)



dfs_iterative(graph,'A')

