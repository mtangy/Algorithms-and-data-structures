import math
import random
import time
import collections

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
            result = tree.lookUp(str(query),Node(key='NIL'))
            print(result.key) 		
	
            end = time.clock()
            sortTime = end - start
            print("Search time : \n", sortTime)	
            query = "exit"		
    print("\n")


class Node():
    
    def __init__(self, parent = None, key = None, left = None, right = None, color = None):
        
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color
		
        if self.key == 'NIL':
            self.color = 'black'
            self.left = self
            self.right = self

			
    def lookUp(self,word,NIL):
        iter = self.root
        while iter != NIL and iter.key != word:
		
            if word < iter.key:
                iter = iter.left
            else:
                iter = iter.right
        return iter
		
class BST():
    def __init__(self):
        self.root = None
		
		
    def search_sorted_List(self, word):
	
        iter = self.root
		
        while (iter !=  None) and (iter.key != word):
            if word < iter.key:
                iter  =  iter.left
            else:
                iter  =  iter.right
        return iter

class RBTree(BST):


    def __init__(self):
        self.NIL = Node(key='NIL')
        self.root = self.NIL
		
    def leftRotate(self, node):
	
        rChild = node.right
        node.right = rChild.left
        node.right.parent = node
        rChild.parent = node.parent
		
        if rChild.parent ==  self.NIL:
            self.root = rChild
        else:
            if node.parent.left == node:
                node.parent.left = rChild
            else:
                node.parent.right = rChild
				
        rChild.left = node
        rChild.left.parent = rChild
		
    def rightRotate(self, node):
	
        leftChild = node.left
        node.left = leftChild.right
        node.left.parent = node
        leftChild.parent = node.parent
		
        if leftChild.parent ==  self.NIL:
            self.root = leftChild
        else:
            if node ==  node.parent.left:
                node.parent.left = leftChild
            else:
                node.parent.right = leftChild
				
        leftChild.right = node
        leftChild.right.parent = leftChild
		
    def rbInsert(self, word):
	
        dNode = self.NIL
        iter = self.root
		
        while iter != self.NIL:
            dNode = iter
            if word < dNode.key:
                iter = iter.left
            else:
                iter = iter.right        
		
        newNode = Node(key = word, parent = dNode, left = self.NIL, right = self.NIL, color = 'red')        
		
        if dNode ==  self.NIL:
            self.root = newNode
        else:
            if word < dNode.key:
                dNode.left = newNode
            else:
                dNode.right = newNode
				
        self.rbInsert_fixup(newNode)
		
    def rbInsert_fixup(self, newNode):
	
        while newNode.parent.color == 'red': 
          
            if newNode.parent ==  newNode.parent.parent.left:
		  
                iter = newNode.parent.parent.right
               
                if iter.color == 'red':
                    newNode.parent.color = 'black'
                    iter.color = 'black'
                    newNode.parent.parent.color = 'red'
                    newNode = newNode.parent.parent
                
                else:
				
                    if newNode ==  newNode.parent.right:
                        newNode = newNode.parent
                        self.leftRotate(newNode)
                    newNode.parent.color = 'black'
                    newNode.parent.parent.color = 'red'
                    self.rightRotate(newNode.parent.parent)
            
            else:
                iter = newNode.parent.parent.left
				
                if iter.color == 'red':
                    newNode.parent.color = 'black'
                    iter.color = 'black'
                    newNode.parent.parent.color = 'red'
                    newNode = newNode.parent.parent
                
                else:
				
                    if newNode ==  newNode.parent.left:
                        newNode = newNode.parent
                        self.rightRotate(newNode)
                    newNode.parent.color = 'black'
                    newNode.parent.parent.color = 'red'
                    self.leftRotate(newNode.parent.parent)
					
        self.root.color = 'black'
        
    def lookUp(self,word,NIL):
	
        iter = self.root
        while iter != NIL and iter.key != word:
		
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
	
	
	tree = RBTree()
	
	for i in range(0,len(words)-1):
		tree.rbInsert((str(words[i]).lower()).rstrip()) 
			
	end = time.clock()
	sortTime = end - start
	print("Sorting time 15k: \n\n", sortTime)
	word_search(tree)
#-----------------------------------------------------------------------


	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Sorted_List/sorted15K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree = RBTree()
	
	for i in range(1,len(words)-2):
		tree.rbInsert(words[i]) 
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time:", sortTime)
	word_search(tree)
#----------------------------------------------------------------------------
	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Permuted_List/perm30K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree = RBTree()
	for i in range(1,len(words)-2):
		tree.rbInsert(words[i]) 
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time 30k:", sortTime)
	word_search(tree)
#-------------------------------------------------------------------------------	

	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Sorted_List/sorted30K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree = RBTree()
	for i in range(1,len(words)-2):
		tree.rbInsert(words[i]) 
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time:", sortTime)
	word_search(tree)

#----------------------------------------------------------------------------
	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Permuted_List/perm45K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree = RBTree()
	for i in range(1,len(words)-2):
		tree.rbInsert(words[i]) 
		
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
	
	tree = RBTree()
	for i in range(1,len(words)-2):
		tree.rbInsert(words[i]) 
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time :", sortTime)
#	word_search(tree)
#-------------------------------------------------------------------------------	

	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Permuted_List/perm60K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree = RBTree()
	for i in range(1,len(words)-2):
		tree.rbInsert(words[i]) 
		
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
	
	tree = RBTree()
	for i in range(1,len(words)-2):
		tree.rbInsert(words[i]) 
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time :", sortTime)
#	word_search(tree)
#-------------------------------------------------------------------------------
	
	txt = open('C:/Users/tangy_000/Documents/CS 340/CS340_pr2_MichaelTangy/Permuted_List/perm75K.txt') 
	print("\n")
	print("Populating list with words in file... \n")
	words = txt.readlines()
	print("sorting list ... \n")
	start = time.clock()
	
	tree = RBTree()
	for i in range(1,len(words)-2):
		tree.rbInsert(words[i]) 
		
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
	
	tree = RBTree()
	for i in range(1,len(words)-2):
		tree.rbInsert((str(words[i]).lower()).rstrip())
		
	end = time.clock()
	sortTime = end - start
	print("Sorting time : ", sortTime)
#	word_search(tree)
#-------------------------------------------------------------------------------


	


if __name__ == "__main__": main()
