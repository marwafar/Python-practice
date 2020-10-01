class Vertex:

    def __init__(self,value):
        self.value=value
        self.edges={}
    
    def add_edges(self,vertex,weight=0):
        self.edges[vertex]=weight
    
class Graph:

    def __init__(self,directed=False):
        self.graph_dict={}
        self.directed=directed
    
    def add_vertex(self,vertex):
        self.graph_dict[vertex.value]=vertex
    
    def add_edges(self,from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edges(to_vertex.value,weight)
        if self.directed:
            self.graph_dict[to_vertex.value].add_edges(from_vertex.value,weight)
    
#----------------------------------------
def DFS(adj_list):
    for node in adj_list:
        cur_vertex=node
        visited=[]
        DFS_rec(adj_list,cur_vertex,visited)
        print(visited)

def DFS_rec(adj_list,cur_vertex,visited):
    visited.append(cur_vertex)
    for node in adj_list[cur_vertex]:
        if node not in visited:
            DFS_rec(adj_list,node,visited)

#---------------------------------------------
def BFS(adj_list):
    for node in adj_list:
        cur_vertex=node
        queue=[node]
        path=[]
        seen={}
        seen[node]=True
        while queue:
            cur_node=queue.pop(0)
            path.append(cur_node)
            for neighbor in adj_list[cur_node]:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen[neighbor]=True
        print(path)
#------------------------------
def is_cycle(my_cycle):
    visited={}
    explore={}
    for node in my_cycle:
        if node not in visited:
            cycle=detect_cycle(my_cycle,node,visited,explore)
            print(visited)
            print(explore)
            print(node)
            if cycle==True:
                return True
    return False
#-----------------------------
def detect_cycle(my_cycle,node,visited,explore):
    visited[node]=True
    explore[node]=True
    for vertex in my_cycle[node]:
        if vertex not in visited:
            if detect_cycle(my_cycle,vertex,visited,explore)==True:
                return True
        elif explore[vertex]==True:
            return True

    print(explore)
    explore[node]=False
    print(explore)
    return False
#-----------------------------
def cycle_un(graph_undirect):
    visited={}
    
    for vertex in graph_undirect:
        if vertex not in visited:
            if is_cycle_un(graph_undirect,vertex,visited,-1):
                return True
    return False
#--------------
def is_cycle_un(graph_undirect,vertex,visited,parent):
    visited[vertex]=True

    for edge in graph_undirect[vertex]:
        if edge not in visited:
            if is_cycle_un(graph_undirect,edge,visited,vertex):
                return True
            elif parent != edge:
                return True
    return False
#-----------------------------
def topological_sorting(my_cycle):
    visited={}
    stack=[]
    for vertex in my_cycle:
        if vertex not in visited:
            DFS_sort(my_cycle,vertex,visited,stack)
    return stack
#------------------
def DFS_sort(my_cycle,vertex,visited,stack):
    visited[vertex]=True
    for edge in my_cycle[vertex]:
        if edge not in visited:
            DFS_sort(my_cycle,edge,visited,stack)
    stack.append(vertex)
#------------------------------
a=Vertex('a')
b=Vertex('b')
c=Vertex('c')
d=Vertex('d')
e=Vertex('e')

g=Graph(True)
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)

g.add_edges(a,b)
g.add_edges(a,d)
g.add_edges(a,c)
g.add_edges(b,a)
g.add_edges(b,d)
g.add_edges(b,e)
g.add_edges(c,a)
g.add_edges(c,d)
g.add_edges(d,c)
g.add_edges(d,a)
g.add_edges(d,b)
g.add_edges(e,b)
g.add_edges(e,d)

#print(g.graph_dict.keys())
#print(e.edges.keys())

adj_list={'a':['b','c','d'], 'b':['a','d','e'], 'c':['a','d'],'d':['b','c','e'],'e':[]}

DFS(adj_list)
BFS(adj_list)

my_cycle={1:[2,4], 2:[3], 3:[], 4:[3,5], 5:[6], 6:[4]}
print(is_cycle(my_cycle))
print(topological_sorting(my_cycle))
graph_undirect={0:[1,2],1:[0],2:[0,3,4],3:[2,4],4:[2,3]}
print(cycle_un(graph_undirect))

        

