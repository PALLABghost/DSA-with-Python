from time import sleep


class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
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
    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result =result + str(curr.data) + '->'
            curr = curr.next
        return result [:-2]
    def append(self,value):
        new_node = Node(value)
        if self.head == None:       # if node is empty
            self.head = new_node
            self.n = self.n + 1
            return                  # if condition matched next code no need to execute
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1

#    def insert_after(self,after,value):
 #       new_node = Node(value)
 #       curr = self.head
 #       # Traverse until we find 'after' or reach end
 #       while curr != None:
  #          if curr.data == after:
  #              break
  #          curr = curr.next
   #     if curr != None:
  #          new_node.next = curr.next
  #          curr.next = new_node
  #          self.n = self.n + 1
  #      else :
   #         print("item not found")

#better version of insert after
    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head
        while curr is not None and curr.data != after:  # This ensures you don’t accidentally access .data on a None object.
            curr = curr.next
        if curr is None:
            print("item not found")
        new_node.next = curr.next  # connecting after-> next of current
        curr.next = new_node  # connecting current -> after
        self.n = self.n + 1


L = LinkedList()
L.insert_head(4)
L.insert_head(3)
L.insert_head(2)
L.insert_head(1)
L.append(5)
L.insert_after(2,100)
print(L)





    
