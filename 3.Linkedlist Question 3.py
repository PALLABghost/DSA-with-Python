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
        while curr is not None:
            result =result + str(curr.data) + '->'
            curr = curr.next
        return result [:-2]
    def sum_odd_node(self):
        temp = self.head
        counter = 0
        result = 0
        while temp is not None:
            if counter % 2 != 0:
                result = result + temp.data
            temp = temp.next
            counter += 1
        return result

L = LinkedList()
L.insert_head(4)
L.insert_head(3)
L.insert_head(2)
L.insert_head(1)
print(L)
print(L.sum_odd_node())