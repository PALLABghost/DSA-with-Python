class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        #empty link list
        self.head = None
        self.n = 0
def __len__(self):
    return self.n
def insert_head(self,value):
    #new node
    new_node = Node(value)
    #create connection
    new_node.next = self.head
    #reassihn head
    self.head  = new_node
    self.n = self.n + 1

    




print(len(L))