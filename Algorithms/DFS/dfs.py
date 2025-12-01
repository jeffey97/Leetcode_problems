graph = {
       'A':['B','C'],
       'B':['D','E'],
       'C':['F'],
       'D':[],
       'E':[],
       'F':[]
       }


#Recursive method

def dfs(node,visited = None):
    if visited is None: 
     visited=set()

    print(node)
    visited.add(node)

    for neighbour in graph[node]:
       if neighbour not in visited:
          dfs(neighbour,visited)


dfs('A')


#Iterative method

