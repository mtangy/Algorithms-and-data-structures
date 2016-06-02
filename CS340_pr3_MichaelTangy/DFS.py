"""
graphin_DAG = {                                                # graphs defined 

	1: [2],
	2: [3,8],
	3: [4],
	4: [5],
	5: [9],
	6: [4,7],
	7: [3,8],
	8: [9],
	9: []
	
}

graphin_directed = {  
    
    1: [2],
    2: [3,8],
    3: [4],
    4: [5],
    5: [3],
    6: [7],
    7: [3,6,8],
    8: [1,9],
	9: [1]
	
}

G = {                                                          #used for testing

    1: [4,5],
    2: [5],
    3: [1,2,6,7],
    4: [5,6],
    5: [6],
    6: [8],
    7: []
	
}
"""

# File IO and dictionary Population for graphs 

graphin_DAG_txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr4_MichaelTangy/graphin-DAG.txt')  
graphin_directed_txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr4_MichaelTangy/graphin-directed.txt')

graphin_DAG = {}
graphin_directed = {}
 
for line in graphin_DAG_txt:                              #Open file 
    vertices = line.split()[1:] 	                      #Parse line from space to get elements 
    graphin_DAG[line.split(":")[0]] = vertices                     #populate dictionary 

for line in graphin_directed_txt:                              #Open file 
    vertices = line.split()[1:] 	                      #Parse line from space to get elements 
    graphin_directed[line.split(":")[0]] = vertices

def DFS(G,V, color, d, time,sortedList,pi,f):                 #DFS function (not used in program)
    """
    for u in V:
        color[u] = ""WHITE"
        pi[u] = []		
	time = 0
    """
    for u in V:
        if color[u] == "WHITE":
            DFS_visit(u,color,d,G, time,sortedList,pi,f)

	
def DFS_visit(u,color,d,G,time,sortedList,pi,f,cyclic):        #explores the adjacent Vertices of the current vertex u
    
    color[u] = "GRAY"                                          #assigns current vertex gray since it has been explored 
    time += 1 
    d[u] = time                                                #record discover time
    
    for v in (G[u]):                                             #iterate through adjacent vertices                       
        if color[v] == "GRAY":
            cyclic = True                                      #if adjacent vertex is gray then cycle found
            return
	
        if color[v] == "WHITE":                                #if white then record parent and recursively call that vertex 
            pi[v] = u
            DFS_visit(v,color,d,G,time,sortedList,pi,f,cyclic)
    		
    color[u] = "BLACK"                                         # assign color black when finished with vertex and record finish time 
    time += 1
    f[u] = time
    sortedList.append(u)                                        # add current vertex to sorted list
	
def DFS_topsort(G,d,time,pi,f,color,cyclic,V):                    
       
    sortedList = [] 	#instantiate sorted list 
    for u in V:
        color[u] = "WHITE"	
	
    for u in G:                                                #iterate through adjacency list until white vertex is discovered then vist                                                               #that vertex	until list is empty 
        if color[u] == "WHITE":                              
            DFS_visit(u,color,d,G,time,sortedList,pi,f,cyclic)
        if cyclic:                                             #break loop is cycle is detected   
            break
 
    if cyclic is True:     
	
	
        return sortedList                               	   #Graph is not acyclic so return back edges
    
    else:
    
        sortedList.reverse()                                   #Graph is acyclic so reverse order to properly sort and return sorted values             
	
        return sortedList                     
	
    
def main():

                                                               #file IO
    """                                                     
    graphin_DAG_txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr3_MichaelTangy/graphin-DAG.txt')  
    graphin_directed_txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr3_MichaelTangy/graphin-directed.txt')
    global time
	
    G = {}                                                    # empty dictionary data structure to represent graph
    adjVertexs = ''
    for line in graphin_DAG_txt:                              #open file 
        linelist = line.strip().split()[1:]                   #remove newline chars and parse line from colon       
        print(linelist)                                       #used to debug              
        number = int(linelist[0])                             #vertex number                      
        adjVertexs = linelist[1]                              #adjacent vertexes
        G['%i' % number/2] = (adjVertexs, linelist[1])        #populate graph 
		
	for line in graphin_directed_txt:                         #open file 
        linelist = line.strip().split()[1:]                   #remove newline chars and parse line from colon       
        print(linelist)                                       #used to debug              
        number = int(linelist[0])                             #vertex number                      
        adjVertexs = linelist[1]                              #adjacent vertexes
        G['%i' % number/2] = (adjVertexs, linelist[1])        #populate graph 	
    """

    color = {}
    time = 0                                                  # Initializing graph lists and variables 
    V = range(len(graphin_DAG))
    d = [0]*(len(graphin_DAG)+1)
    #sortedList = [0]*(len(graphin_DAG))
    pi= [0]*(len(graphin_DAG)+1)
    f = [0]*(len(graphin_DAG)+1)
    topSortedList = [] 
    cyclic = False
	
	
    topSortedList = DFS_topsort(graphin_DAG,d,time,pi,f,color,cyclic,V)    #Sorting lists and determining if they are Acyclic as well as outputing 
	                                                                               #their coresponding values
	
    print("testing graphin_DAG")
	
    if cyclic is True:
        print("Graph is not Acyclic")
        print("Back edges:")
        print(topSortedList)
        print("\n")
        print ('pi:', pi)
        print ('d:', d)
        print ('f:', f)		

    else:
        print("Graph is Acyclic")
        print("Topologically Sorted list:")
        print(topSortedList)
        print("\n")
        print ('pi:', pi)
        print ('d:', d)
        print ('f:', f)		
		
		
    print("\n")
	
    time = 0
    V= range(len(graphin_directed))                                              # Initializing graph lists and variables 
    d= [0]*(len(graphin_directed)+1)
    color = ["WHITE"]*(len(graphin_directed)+1)
    #sortedList = [0]*(len(graphin_directed))
    pi= [0]*(len(graphin_directed)+1)
    f = [0]*(len(graphin_directed)+1)
    topSortedList = [] 
    cyclic = False

    topSortedList = DFS_topsort(graphin_directed,d,time,pi,f,color,cyclic,V)         #Sorting lists and determining if they are Acyclic as well as outputing 
	                                                                               #their coresponding values
    print("testing graphin_directed")
	
    if cyclic is True:
        print("Graph is not Acyclic")
        print("Back edges:")
        print(topSortedList)
        print("\n")
        print ('pi:', pi)
        print ('d:', d)
        print ('f:', f)		

    else:
        print("Graph is Acyclic")
        print("Topologically Sorted list:")
        print(topSortedList)
        print("\n")
        print ('pi:', pi)
        print ('d:', d)
        print ('f:', f)	   


if __name__ == "__main__": main()	