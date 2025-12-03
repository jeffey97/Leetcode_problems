graph = {
       'A':['B','C'],
       'B':['D','E'],
       'C':['F'],
       'D':[],
       'E':[],
       'F':[]
       }


def dfs_iterative (graph,start):
    visited = set()
    stack = [start]

    while stack: 

        node = stack.pop()

        if node not in visited:
            print(node)
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)

dfs_iterative(graph,'A')


