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
            return
        new_node.next = curr.next  # connecting after-> next of current
        curr.next = new_node  # connecting current -> after
        self.n = self.n + 1
    def clear(self): # empty LL
        self.head = None
        self.n = 0
    def delete_head(self):
        if self.head is None:
            print ("Empty LL")
            return
        self.head = self.head.next
        self.n = self.n -1
    def pop(self):   #delete from tail
        if self.head is None:           #if LL is empty
            print("Empty LL")
            return
        if self.head.next is None:           #if one item in LL
            return self.delete_head()
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        self.n = self.n -1
    def remove(self,value):
        if self.head is None:        #if LL is empty
            print("Empty LL")
            return
        if self.head.data == value:      # if need to delete head
            return self.delete_head()
        curr = self.head
        # Traverse until we find the node before the target
        while curr.next is not None and curr.next.data != value:
            curr = curr.next
        if curr.next is None:           #seacrhing completed and it reach to last node
            print("Item not found")     # so item is not found
        else:
            curr.next = curr.next.next      #find the value in next node so skip the next node and store the value of curr.next.next node
            self.n = self.n - 1


    def remove_duplicate_also(self,value):
        # Step 1: Handle duplicates at the head
        while self.head is not None and self.head.data == value:
            self.head = self.head.next
            self.n = self.n -1

        # Step 2: Traverse the rest of the list
        # Use curr.next is not None when you’re looking ahead (like deleting the next node or stopping before the tail)
        #If you’re deleting the next node (like in remove), you only need to check curr.next. That’s why while curr.next is not None works — you stop at the node before the tail.
        # Use curr is not None when you need to process every node, including the tail itself.
        #If you’re deleting all duplicates, including at the tail, you must check every node. That’s why while curr is not None is needed — otherwise the last node is skipped.
        curr = self.head
        while curr is not None and curr.next is not None:   #
            if curr.next.data == value:
                curr.next = curr.next.next       # Found a duplicate → bypass it
                self.n = self.n -1
            else:
                curr =  curr.next        # Move forward



L = LinkedList()
L.insert_head(2)
L.insert_head(3)
L.insert_head(2)
L.insert_head(1)
L.append(5)
L.insert_after(2,100)
print(L)
L.remove_duplicate_also(2)
print(L)





    
