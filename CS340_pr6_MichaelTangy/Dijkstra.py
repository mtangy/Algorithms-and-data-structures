from math import floor	
                                          #heap implementation
def push(heap, item):

    heap.append(item)
    shift_down(heap, 0, len(heap)-1)
   
def pop(heap):

    lastelt = heap.pop()    
    if heap:
        node = heap[0]
        heap[0] = lastelt
        shift_up(heap, 0)
        return node
    return lastelt

def shift_down(heap, startpos, pos):
    newNode = heap[pos] 
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newNode < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newNode
	
def shift_up(heap, pos):
    endpos = len(heap)
    startpos = pos
    newNode = heap[pos] 
    childpos = 2*pos + 1   
    while childpos < endpos: 
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos 
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    heap[pos] = newNode
    shift_down(heap, startpos, pos)	

def shortest_Path(G):

    query = ""
    key = []
    pi = []
    path = []
    weight = 0
    query = input("\nPlease enter a start vertex: ")
    start = int(query)
    path,weight = dijkstras(G,start,100)
    print("Shortest path rooted at "+str(start)+" is: ",path[1:]) 
    print("Path length: ",len(path[1:]))
    print("Path weigth: ", weight)
    while(True):    
        weight = 0
        query = input("Please enter an end vertex: ")		
        if(query == "exit"): break    		
        end = int(query)
        path,weight = dijkstras(G,start,end)
        
        print("Shortest path from "+str(start)+" to "+str(end)+" is: ",path[1:]) 
        print("Path length: ",len(path[1:]))
        print("Path weigth: ", weight)
        print("\ntype 'exit' to exit program\n")
	   
def dijkstras(G,start,end):
    weight = 0
    V = range(len(G)+1)           # initialize vertex list for input graph 
    key = [1000] * (len(V))       # initialize vertex key list with max key value 
    visited = [False]*(len(V))
    pi = [None] * len(V)	
    key[start] = 0
    Q = []
    mst = []
    shortestPath = []
    push(Q, (key[start], start))    #adding root edge to the min-priority que
    par = 0
    while len(Q) > 0:	
        _, u = pop(Q)                          #extract next unvisited vertice  
        if visited[u] is False :                   #verify its unvisted 		
            if pi[u] not in shortestPath: shortestPath.append(pi[u]) 
            if end is 100:
                if u not in shortestPath: shortestPath.append(u) 
            
            visited[u] = True                      #mark vertice as visted 
            if(u is end):
                shortestPath.append(u)
                break 
            for (v, w) in G[u]:                    #iterate through all edges of that vertex until you find one that connects a unvisited vertex
                if visited[v] is False:            
                    if key[v] > key[u]+w:                 
                        key[v] = key[u]+w                            						
                        weight+=floor(w/2)
                        pi[v] = u
                        push(Q, (key[v], v))     #add edge to the min-priority que 
    return shortestPath,weight	
	
def main():

	# File IO  
    graphin_w_ud_txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr6_MichaelTangy/graphin_w_ud.txt')  #Open file
    graphIn = {}
    edges = []
    j = 1
	
    for line in graphin_w_ud_txt:                           #Populate Graph from input FIle                
        ele = line.split()[1:] 	                            #Parse line from space to get elements 
        for u in range(0,floor(len(ele)+1/2)):
            if u in [0,2,4,6]:
                edges.append((int(ele[u]),int(ele[u+1])))   #create edge pair's at each vertex 
        graphIn[j] = edges                                     #combine edge lists 
        j+=1
        edges = []

    shortest_Path(graphIn)	
    print("PROGRAM TERMINATED")
	
if __name__ == "__main__": main()	                       #call main upon program execution 	