import math
import random
import time

def Wild_Card_lookup(tree):

    query = ""
    while (query != "exit"): 
	    
        query = input("what word would you like to find?:")
        print("type 'exit' to exit")
		
        max = query.replace("*","z")
        min = query.replace("*","a")
	
        print("Matching words: \n")
        tree.wcSearch(max, min) 
        print("# of matches: \n")
        print(wCount)
		
		
def word_search(tree):

    query = ""
    while(query != "exit"): 
        query = input("what word would you like to find?:")
        print("type 'exit' to exit")
        print("words found:")

        if(query != "exit"):
            	
            start = time.clock()
            result = tree.search_iterative(str(query))	
            print(result.key) 		
	
            end = time.clock()
            sortTime = end - start
            print("Search time : \n", sortTime)	        
            #query = "exit"
    
        
        print("\n")

class Node():

    def __init__(self,parent,key):
	
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
		
    def wcSearch(self, max, min):
	
        iter = self.root	    
	
        if iter.left.key <= min:
            iter.left.wcSearch(max, min)
			
        print (self.key) 
        wCount +=1 
		
        if iter.right.key >= max:
            iter.right.wcSearch(max, min)	
		

class BST():

    def __init__(self):
        self.root = None
		
		
    def search_iterative(self,word):
	
        iter = self.root
		
        while (iter != None) and (iter.key != word):
            if word < iter.key:
                iter = iter.left
            else:
                iter = iter.right
        return iter
		
    def insert(self,word): 
        
        iter =None
        tRoot = self.root
		
        while tRoot != None:
            iter = tRoot
            if word < tRoot.key:
                tRoot = tRoot.left
            else:
                tRoot = tRoot.right
				
        newNode = Node(iter,word)
		
        if iter == None:
            self.root = newNode
        else:
            if newNode.key < iter.key:
                iter.left = newNode
            else:
               iter.right = newNode
        
	
		
 
    def wcSearch(self, max, min):
	
        iter = self.root	    
	
        if iter.left.key <= min:
            self.wcSearch(max, min)
			
        print (self.key) 
        wCount +=1 
		
        if iter.right.key >= max:
            self.wcSearch(max, min)
			

    def search_iterative(self,word):
	
        iter = self.root
		
        while (iter != None) and (iter.key != word):
            if word < iter.key:
                iter = iter.left
            else:
                iter = iter.right
        return iter

	
def main():

	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Permuted_List/perm15K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()

	print("sorting list ... \n")
	start = time.clock()
	
	tree=BST()
	for i in range(0,len(words)-1):
		tree.insert((str(words[i]).lower()).rstrip()) 
			
	end = time.clock()
	sortTime = end - start
	print("Sorting time 15k: \n\n", sortTime)
	word_search(tree)
#----------------------------------------------------------------------	

	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Sorted_List/sorted15K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree=BST()
	for i in range(1,len(words)-2):
		tree.insert(words[i]) 
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time:", sortTime)

#----------------------------------------------------------------------------
	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Permuted_List/perm30K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree=BST()
	for i in range(1,len(words)-2):
		tree.insert((str(words[i]).lower()).rstrip()) 
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time 30k:", sortTime)
	#word_search(tree)
#-------------------------------------------------------------------------------	

	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Sorted_List/sorted30K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree=BST()
	for i in range(1,len(words)-2):
		tree.insert(words[i]) 
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time:", sortTime)


#----------------------------------------------------------------------------
	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Permuted_List/perm45K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree=BST()
	for i in range(1,len(words)-2):
		tree.insert((str(words[i]).lower()).rstrip())  
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time 45k:", sortTime)
	#word_search(tree)
#-------------------------------------------------------------------------------	
	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Sorted_List/sorted45K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree=BST()
	for i in range(1,len(words)-2):
		tree.insert((str(words[i]).lower()).rstrip())  
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time :", sortTime)

#-------------------------------------------------------------------------------	

	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Permuted_List/perm60K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree=BST()
	for i in range(1,len(words)-2):
		tree.insert((str(words[i]).lower()).rstrip())  
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time 60k:", sortTime)
	#word_search(tree)
#-------------------------------------------------------------------------------	
	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Sorted_List/sorted60K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree=BST()
	for i in range(1,len(words)-2):
		tree.insert(words[i]) 
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time :", sortTime)
	
#-------------------------------------------------------------------------------
	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Permuted_List/perm75K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree=BST()
	for i in range(1,len(words)-2):
		tree.insert((str(words[i]).lower()).rstrip())  
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time 75k:", sortTime)
	#word_search(tree)
#-------------------------------------------------------------------------------	
	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Sorted_List/sorted75K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree=BST()
	for i in range(1,len(words)-2):
		tree.insert((str(words[i]).lower()).rstrip())  
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time :", sortTime)
#-------------------------------------------------------------------------------


if __name__ == "__main__": main()
