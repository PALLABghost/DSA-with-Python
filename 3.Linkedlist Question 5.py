#Given a linked list of characters.write a python function to return a new string that is created by
#appending all characters given in the link as per rules given below

#Rule ->
#Replace '*' or '/' by a single space
#In case of two consecutive occurrences of '*' or '/' , replace those two occurrences by a single space and
#convert the next character to upper case

#Assume that->
#There will ot be more than two consecutive of '*' or '/'
#The linked list will always end with an alphabet

#Sample input
#A,n,*,/,a,p,p,l,e,*,a,/,day,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,A,w,a,y

#Expected Output
#An Apple a day keeps A Doctor Away


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # empty link list
        self.head = None
        self.n = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:  # if node is empty
            self.head = new_node
            self.n = self.n + 1
            return  # if condition matched next code no need to execute
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1
    def __str__(self):
        curr = self.head
        result = ''
        while curr is not None:
            result =result + str(curr.data)
            curr = curr.next
        return result
    def change_sent(self):
        temp = self.head
        while temp is not None:
            if temp.data == '*' or temp.data == '/':
                temp.data = ' '         #for create space for * or /
                if temp.next.data == '*' or temp.next.data == '/':
                    temp.next.next.data = temp.next.next.data.upper()
                    temp.next = temp.next.next      #for skipping the second * or / number
            temp = temp.next

L = LinkedList()
L.append('A')
L.append('n')
L.append('*')
L.append('/')
L.append('a')
L.append('p')
L.append('p')
L.append('l')
L.append('e')
L.append('*')
L.append('a')
L.append('/')
L.append('d')
L.append('a')
L.append('y')
L.append('*')
L.append('*')
L.append('k')
L.append('e')
L.append('e')
L.append('p')
L.append('s')
L.append('/')
L.append('*')
L.append('a')
L.append('/')
L.append('/')
L.append('d')
L.append('o')
L.append('c')
L.append('t')
L.append('o')
L.append('r')
L.append('*')
L.append('A')
L.append('w')
L.append('a')
L.append('y')
print(L)
L.change_sent()
print(L)