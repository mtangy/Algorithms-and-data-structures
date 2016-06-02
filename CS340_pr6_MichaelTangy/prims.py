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

def Prims(G,r):
    
    V = range(len(G)+1)           # initialize vertex list for input graph 
    key = [1000] * (len(V))       # initialize vertex key list with max key value 
    visited = [False]*(len(V))
    pi = [None] * len(V)	
    key[r] = 0
    Q = []
    mst = []
    mstEdges = []
    push(Q, (key[r], r))    #adding root edge to the min-priority que
	
    while len(Q) > 0:	
        _, u = pop(Q)             #extract next unvisited vertex 
        if visited[u] is False:       #verify its unvisited 		
            mstEdges.append((pi[u],u))             #add that vertex as the next element in the mst 
            mst.append(u) 
            visited[u] = True                   #mark vertices as visited 
            for (v, w) in G[u]:                    #iterate through all edges of that vertex until you find one that connects a unvisited vertex
                if visited[v] is False:            
                    if key[v] > w:                 
                        key[v] = w                   #assign vertex's weight          						
                        pi[v] = u
                        push(Q, (key[v], v))     #add edge to the min-priority que 
    return [mst,mstEdges]	
	
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


    #print(graphIn)
    mst = []
    mst = Prims(graphIn,1)
    mstEdges = mst[1]
    print("\nMST vertices rooted at '1':\n",mst[0],"\n")   #output data to standard out 
    print("MST edges found in order:\n",mstEdges[1:])      
    print("\nPopulating primout.txt with MST.....")
	
    prim_out_file = open("primout.txt", 'w')
	
	                                                        #Writing mst edges to file
    mstEdges = mst[1]
    for E in range(1,len(mstEdges)):    
        prim_out_file.write(str(mstEdges[E])+"\n")

    print("\nFile population complete")
	
if __name__ == "__main__": main()	                       #call main upon program execution 	