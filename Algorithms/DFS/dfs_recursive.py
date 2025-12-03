graph = {
       'A':['B','C'],
       'B':['D','E'],
       'C':['F'],
       'D':[],
       'E':[],
       'F':[]
       }


graph_1={
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


#Recursive method_1

def dfs(node,visited = None):
    if visited is None: 
     visited=set()

    print(node)
    visited.add(node)

    for neighbour in graph[node]: #replace with graph_1 for the bigger tree
       if neighbour not in visited:
          dfs(neighbour,visited)


dfs('A')


#Iterative method

