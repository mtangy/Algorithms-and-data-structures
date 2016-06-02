
#-------------------------------
#File IO and graph population procedures 

graphin_DAG_txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr4_MichaelTangy/graphin-DAG.txt')  
graphin_directed_txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr4_MichaelTangy/graphin-directed.txt')
SCC_graph_txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr4_MichaelTangy/graphin-MT.txt')

graphin_DAG = []
graphin_directed = []
SCC_graph = {}
vertice_list = []
i = 1

for line in graphin_DAG_txt:                            #Open file 
    vertice_line = line.split()[1:] 	                #Parse line from space to get elements 
    for u in vertice_line:
	    vertice_list.append(int(u))   
    graphin_DAG.append(vertice_list)                       #populate dictionary 
    vertice_list = []
    i+=1
i = 1
vertice_list = []	
line = ""
u = ""
vertice_line = ""
for line in graphin_directed_txt:                       #Open file 
    vertice_line = line.split()[1:] 	                #Parse line from space to get elements 
    for u in vertice_line:
	    vertice_list.append(int(u))   
    graphin_directed.append(vertice_list)                             #populate dictionary 
    vertice_list = []
    i+=1	
i = 1
vertice_list = []
line = ""
u = ""
vertice_line = ""
for line in SCC_graph_txt:                              #Open file 
    vertice_line = line.split()[1:] 	                #Parse line from space to get elements 
    for u in vertice_line:
	    vertice_list.append(int(u))   
    #SCC_graph.append(vertice_list)                              #populate dictionary 
    SCC_graph[i] = vertice_list
    vertice_list = []
    i+=1	


class graph():

    def __init__(self,G,V=None):
	
        self.G = G
        self.time = 0                                                  # Initializing graph lists and variables 
        if V == None:
            self.V = range(1, len(self.G)) 
        else:
            self.V = V #range(1,len(V))
        self.d = [0]*(len(self.G))
        self.color = ["WHITE"]*(len(self.G)+1)
        self.sortedList = []
        self.pi= [0]*(len(self.G))
        self.f = [0]*(len(self.G))
        self.cyclic = False
        self.tree_num = 0
        self.forests = []
        #print("\n d len",len(self.d),"\n c[8]",self.color[8],"\n")
		
    def DFS(self):                 #DFS function (not used in program)

        for u in self.V:
            if self.color[u] == "WHITE":
                self.tree_num += 1
                self.forests.append([])
                self.forests[-1].append(u)
                self.DFS_Visit(u)      

    def DFS_Visit(self,u):        #explores the adjacent Vertices of the current vertex u
        self.time += 1
        self.color[u] = "GRAY"                                          #assigns current vertex gray since it has been explored  

        for v in self.G[u]: 		#iterate through adjacent vertices                             
            
            if self.color[v] == "WHITE":
                self.forests[-1].append(v)
                if v:
                    self.DFS_Visit(v)    
				
        self.sortedList.insert(0,u)
        #self.color[u] = "BLACK"                                         # assign color black when finished with vertex and record finish time 
        self.time += 1
        #self.f[u] = self.time
        #sortedList.append(u)                                        # add current vertex to sorted list
        
	
    def DFS_topsort(self):                    

        for u in self.G:                                                #iterate through adjacency list until white vertex is discovered then vist 
                                                                #that vertex	until list is empty 
            if self.color[u] == "WHITE":                              
                self.DFS_Visit(u,color,d,G,time,sortedList,pi,f,cyclic)    
            if self.cyclic:                                             #break loop is cycle is detected   
                break 

        if self.cyclic is True: 	
            return self.sortedList                               	    #Graph is not acyclic so return back edges
        else:    
            self.sortedList.reverse()                                   #Graph is acyclic so reverse order to properly sort and return sorted values             	
            return self.sortedList                     
	
    def G_T(self):
        Gt = {}
        i = 1
        for u in self.G:
            Gt[i] = []
            i += 1

        for u in self.V:
            for v in self.G[u]:
                
                Gt[v].append(u)
   
        return Gt

def SCC(G):                                                              # finds SCC's in given graph
 
    Gn = graph(G)
    Gn.DFS()
    sortedG = Gn.sortedList

    Gtn = Gn.G_T()
    V_Gtn = graph(Gtn,sortedG)
    V_Gtn.DFS()

    V_F = [V_Gtn.forests, Gtn]

    return V_F


def DAG(Forests,Gtn,G):                                              # makes top sorted DAG of SCC's
	
    V_DAG=range(len(Forests))
    SCC_DAG = []
	
    for i in V_DAG: 
        SCC_DAG.append([])
    s=[None]*(len(G)+1) 
	
    for i in V_DAG:
        for u in Forests[i]:
            s[u]=i
    
    for i in V_DAG:
        for u in Forests[i]:
            for v in Gtn[u]:
                if SCC_DAG[s[v]]==[] or SCC_DAG[s[v]][-1] != i:
                    if s[v]!=i:
                        SCC_DAG[s[v]].append(i) 
    return SCC_DAG



def main():

    scc_file = open("sccout.txt", 'w')                                                                         # open file
    dag_file = open("dagout.txt", 'w')
	
    scc = []
    scc_dag = []

   
    print ('G:', SCC_graph)
    scc = SCC(SCC_graph)
    print ('SCC:', scc[0])
    
	
	
    i = 1                                                                                                       #Writing SCC to file
    for vl in scc[0]:    
        scc_file.write(str(i) + ": ") 
        for v in vl:
            scc_file.write(str(v)+" ")
        scc_file.write("\n")
        i+=1    
	
	
    scc_dag = DAG(scc[0],scc[1],SCC_graph)
    print('SCC DAG:',scc_dag)
	
    i = 1                                                                                                       #Writing DAG to file
    for l in scc_dag:    
        dag_file.write("s"+str(i) + ": ") 
        for v in l:
            dag_file.write(str(v+1)+" ")
        dag_file.write("\n")
        i+=1
	

	

if __name__ == "__main__": main()	