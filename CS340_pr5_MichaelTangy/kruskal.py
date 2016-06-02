class Disjoint_Set():

    def __init__(self): #constructor for set 
        self.parent = {}  # Initialize set as empty dictionary 
        self.rank = {} 
    
    def Make_Set(self,s):	
        self.parent[s] = s
        self.rank[s] = 0
    
    def Union(self,x,y):             # union implemented with union-by-depth
        s1 = self.Find_Set(x)
        s2 = self.Find_Set(y)
        if self.rank[s1] > self.rank[s2]:
            self.parent[s2] = s1
        else:
            self.parent[s1] = s2
            if self.rank[s1] is self.rank[s2]:
                self.rank[s2] += 1
    
    def Find_Set(self,s):             
        if s is not self.parent[s]:
            self.parent[s] = self.Find_Set(self.parent[s])
        return self.parent[s]

def kruskal(G,num): 

    A = []                        #initialize disjoint set and graph range along with mst container
    G_V = range(num)
    DS = Disjoint_Set()
	
    for v in G_V:
        DS.Make_Set(v)
		
    G.sort(key = getWeight) # sort edges in non-decreasing order by weight 
    for E in G:
        (u,v), _ = E
        if DS.Find_Set(u) is not DS.Find_Set(v):
            A.append((u,v))               #add edges to mst
            DS.Union(u,v)                   
           
    return A

def getWeight(item):                 
    return item[1]

def main():
    from math import floor,ceil

    graphin_w_ud_txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr5_MichaelTangy/graphin_w_ud.txt')
    graphin_w_ud = []

    i = 1
    
    for line in graphin_w_ud_txt:                       #Open file 
        ele = line.split()[1:] 	                         #Parse line from space to get elements 
        #print(ele,len(ele))
        for u in range(0, floor( len(ele)+1/2 )):
            #print(u)
            if u in [0,2,4]:
                #print([[i,int(ele[u])],int(ele[u+1])],"\n")
                graphin_w_ud.append([[i,int(ele[u])],int(ele[u+1])])   #populate dictionary
        i+=1

    mst = []
    num = len(graphin_w_ud)
	
    print ('\nG:', graphin_w_ud)
    #print("\n# of nodes", num)
    mst = kruskal(graphin_w_ud,num)
    print ('\nMST:', mst)
	

    kruskal_out_file = open("kruskalout.txt", 'w')
	
    i = 1                                                                                                       #Writing SCC to file
    for vl in mst:    
        #kruskal_out_file.write(str(i) + ": ") 
        for v in vl:
            kruskal_out_file.write(str(v)+" ")
        kruskal_out_file.write("\n")
        i+=1    	
    	
	
if __name__ == "__main__": main()	