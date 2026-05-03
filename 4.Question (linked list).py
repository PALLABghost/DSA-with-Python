#Write a python program to reverse a linklist containing integer data
#without creating new link list

class Node:
    def __init__(self,value):
        self.data = value
        self.n = 0

class LinkedList:
    def __init__(self):
        # empty link list
        self.head = None
        self.n = 0
    def insert_head(self,value):
        #new node
        new_node = Node(value)
        #create connection
        new_node.next = self.head
        #reassihn head
        self.head  = new_node
        self.n = self.n + 1
    def __str__(self):
        curr = self.head
        result = ''
        while curr is not None:
            result =result + str(curr.data) + '->'
            curr = curr.next
        return result [:-2]
    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node      #reverse the connection from next node to previous node
            prev_node = curr_node           # now move 1 step
            curr_node = next_node           # build curr node connection to next node
        self.head = prev_node              # make tail node as head node, so last None will be removed
                                    #as after completing the loop Last None is the curr and tail node is the prev

L = LinkedList()
L.insert_head(4)
L.insert_head(3)
L.insert_head(2)
L.insert_head(1)
print(L)
L.reverse()
print(L)
