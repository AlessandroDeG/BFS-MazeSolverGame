from graphviz import Digraph
"""
graph = {
    'A': ['C', 'D', 'E'],
    'B': ['C', 'D', 'F'],
    'C': ['A', 'B', 'I', 'G'],
    'D': ['A', 'B', 'H'],
    'E': ['A', 'F', 'H'],
    'F': ['B', 'E'],
    'G': ['C', 'I'],
    'H': ['D', 'E'],
    'I': ['C', 'G']
}

g1 = {
    'A': ['B','G'],
    'B': ['A', 'C', 'F'],
    'C': ['B', 'D', 'E'],
    'D': ['C', 'G', 'H'],
    'E': ['C'],
    'F': ['B'],
    'G': ['A', 'D'],
    'H': ['D'],
}

g2 = {
    'A': ['G', 'E'],
    'B': ['D'],
    'C': ['F', 'G'],
    'D': ['B'],
    'E': ['A'],
    'F': ['C'],
    'G': ['A', 'C'],
}

g3 = {
    'A': ['C', 'F', 'G', 'E'],
    'B': ['A', 'C', 'D', 'F'],
    'C': ['A', 'B', 'D', 'G', 'E'],
    'D': ['C', 'A', 'B', 'E', 'G'],
    'E': ['C', 'A', 'F', 'G', 'D'],
    'F': ['A', 'B', 'E', 'G'],
    'G': ['F', 'A', 'C', 'D', 'E'],
}

bipartite = {
    'A' : ['B', 'D'],
    'B' : ['A', 'C'],
    'C' : ['B', 'D'],
    'D' : ['A', 'C'],
}   
"""


visited = []  
queue = []  
red = []
blue = []

pred={}
cicloInOrdine=[]


"""
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    red.append(node)
    print("Visit: ")
    while queue:
        s = queue.pop(0)
        print(f'{s}', end=" --> ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                pred[neighbour]=s
                # add neighbour in the opposite color of s
                blue.append(neighbour) if s in red else red.append(neighbour)
            if (s in red and neighbour in red) or (s in blue and neighbour in blue):
                print("not bipartite, odd cicle:")
                while(s != neighbour):
                    cicloInOrdine.insert(0,s)
                    cicloInOrdine.append(neighbour) #prepend
                    s=pred[s]
                    neighbour=pred[neighbour]
                cicloInOrdine.insert(0,s)
                print("in ordine ez piz")
                print(cicloInOrdine)
                    

                exit()
"""


 






def bfs(N,ij,start,end):
    discovered = []  
    queue = [] 
    pred = {}
    discovered.append(start)
    queue.append(start)
    neighbours={}
    path=[]
    #red.append(start)
    #print("Visit: ")
    while queue:
        s = queue.pop(0)
        #print(f'{s}', end=" --> ")
        neighbours[s]=[]
        si=s[0]
        sj=s[1]
        print(f'neighbours of {s}',end= " : ")

        #find neighbours of s
        for i in range(si-1,0,-1):#up
            if((i,sj) not in discovered and (i,sj) not in ij):
                neighbours[s].append((i,sj))
            else:
                break

        for j in range(sj-1,0,-1):#left
            if((si,j) not in discovered and (si,j) not in ij):
                neighbours[s].append((si,j))
            else:
                    break
        
        print("  ",end="")
        for i in range(si+1,N):#down
            if((i,sj) not in discovered and (i,sj) not in ij):
                neighbours[s].append((i,sj))
            else:
                break

        for j in range(sj+1,N):#right
            if((si,j) not in discovered and (si,j) not in ij):
                neighbours[s].append((si,j))
            else:
                    break
 
        print(f'{neighbours[s]}')

        for neighbour in neighbours[s]:
            if neighbour not in discovered:
                if(neighbour == end):
                    print(neighbour)
                    path.append(neighbour)
                    print(s)
                    path.append(s)
                    while(s != start):
                        s=pred[s]
                        print(s)
                        path.append(s)
                    return len(path)-1
                else:
                    discovered.append(neighbour)
                    queue.append(neighbour)
                    pred[neighbour]=s
                    print(f'visiting neighbour: {neighbour}')
   


#in slides
#N=8
#ij=[(0,0),(0,2),(0,5),(1,0),(1,7),(2,1),(2,4),(2,6),(3,3),(4,1),(4,3),(4,6),(5,2),(5,6),(5,7),(6,1),(6,5),(7,1)]
#s=(3,0)
#t=(7,7)

#test
N=4
ij=[]
s=(0,0)
t=(3,3)


print(bfs(N,ij,s,t))