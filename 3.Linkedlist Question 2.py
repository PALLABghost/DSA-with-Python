#Write a python program to find the maximum value in a linked list and replace with a given value.
#Assume that the linked list is populated with whole numbers and there is only one maximum value in the LL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        while curr != None:
            result =result + str(curr.data) + '->'
            curr = curr.next
        return result [:-2]

    def replace_max(self,value):
        temp = self.head
        maxi = temp
        while temp is not None:
            if maxi.data < temp.data:
                maxi = temp
            temp = temp.next
        maxi.data = value

L = LinkedList()
L.insert_head(4)
L.insert_head(3)
L.insert_head(2)
L.insert_head(1)
L.replace_max(8)
print(L)