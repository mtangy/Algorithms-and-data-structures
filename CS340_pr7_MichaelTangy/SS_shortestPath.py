from math import floor

def shortest_Path(G):

    query = ""
    DAG = ""
    path = []
    weight = 0
    query = input("\nPlease enter a source vertex: ")
    source = int(query)
    D = []
    V = range(len(G))
    print("\n")
    m = 0 #                                         # of edges
    x = {}                                          #initialize containers 
    y = {}
    w = {}
    for u in V: 
        for v, weight in G[u]:                      #parsing weight and edge values into dictionaries 
            x[m] = u
            y[m] = v
            w[m] = weight
            m += 1
    d = [10000] * (len(V)+1)
    print("Running Bellman Ford")
    d,D = bellman_ford(source-1,d,V,m,x,y,w,G)
    print("there were "+str(len(D))+" edge relaxations performed during the algorithm")            
    if "-Cycle" in d:
        print("a negative weight cycle exists\n")
        print("a negative weight cycle does not exists\n")           # user interface
    else:
        print("a negative weight cycle does not exists\n")
        print("a negative weight cycle does exists\n")		
    print("path weights: ", d,"\n")
    while(True):    
        query = input("Please enter an end vertex: ")		           #end vertex query loop
        if(query == "exit"): break    		
        end = int(query)          
        print("Shortest path from "+str(source)+" to "+str(end)+" is: ",d[end-1])
        print("\ntype 'exit' to exit program\n")
		
		
def dag_UI(G):
    query = ""
    DAG = ""
    path = []
    weight = 0
    query = input("\nPlease enter a source vertex: ")
    source = int(query)
    p = []
    print("Running DAG SP")
    d,p = Dag_SP(G,source-1)

    print("there were "+str(len(p))+" edge relaxations performed during the algorithm")
    if "-Cycle" in d:
        print("a negative weight cycle exists\n")
    else:
        print("a negative weight cycle does not exists\n")                   # user interface
        print("the graph is a DAG")		
    print("path weights: ", d,"\n")
    while(True):    
        query = input("Please enter an end vertex: ")		
        if(query == "exit"): break    		
        end = int(query)          
        print("Shortest path from "+str(source)+" to "+str(end)+" is: ",d[end-1])
        print("\ntype 'exit' to exit program\n")
		
		
        
	   
def bellman_ford(s,d,V,m,x,y,w,G):
    d[s] = 0
    D = [0]
    r = 0
    for i in range(len(V) - 1):                  #edge traversals 
        for e in  range(m):
            u = x[e]
            v = y[e]

            if d[v] > d[u] + w[e]:
                d[v] = d[u] + w[e]                      #edge relaxtions 
                D.append(d[u] + w[e])
    z = None
    for e in range(m):
        u = x[e]
        v = y[e]
        if d[v] > d[u] + w[e]:
            D.append(v)
            z = v
            break
    if z is not None:
        dfs(z,d,G)
    l=-1
    for k in d:
        l+=1                                 #edge traversals 
        if k>100:
            d[l] = "Infinity"

	
    return d,D
	
s = set()
def dfs(v,d,G):
    
    d[v] = '-Cycle'                             #checking for negative cycles 
    s.add(v)
    for u, _ in G[v]:
        if u not in s:
            dfs(u,d,G)
				
def Dag_SP(G,source):
    V = range(len(G))                                     # graph parameter initialization
    d = [1000] * (len(V)+1)
    d[source] = 0
    p = []

    for u in V:
        for v, w in G[u]:                                      #edge traversals 
            if d[v] > d[u] + w:                               #edge relaxations      
                d[v] = d[u] + w
                p.append(u)
    l=-1
    for k in d:
        l+=1
        if k>100:
            d[l] = "Infinity"
    return d,p


def main():

	# File IO  
    graphin_w_ud_txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr7_MichaelTangy/graphin-weighted-DAG.txt')  #Open file
    graphIn = {}
    edges = []
    j = 0
    Query = ""
    for line in graphin_w_ud_txt:                           #Populate Graph from input File                
        ele = line.split()[1:] 	                            #Parse line from space to get elements 
        for q in range(0,floor(len(ele)+1/2)):
            if q in [0,2,4,6]:
                edges.append((int(ele[q]),int(ele[q+1])))   #create edge pair's at each vertex 
        graphIn[j] = edges                                     #combine edge lists 
        j+=1
        edges = []

    print("What algorithm would you like to run?\n")
    Query = input("Type 'd' for DAG SP or 'b' for Bellman-Ford:")
    if Query is "d":
        dag_UI(graphIn)
    if Query is "b":    
        shortest_Path(graphIn)

    print("PROGRAM TERMINATED")
	
if __name__ == "__main__": main()	       