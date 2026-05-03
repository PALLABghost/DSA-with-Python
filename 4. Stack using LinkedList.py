#stack isempty, push ,peak,pop ,traverse,

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None     #if top is none is_empty will return true, either it will return false

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def traverse(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def peak(self):
        if (self.is_empty()):
            return "Stack Empty"
        else:
            return self.top.data
    def pop(self):
        if (self.is_empty()):
            return "Stack Empty"
        else:
            self.top = self.top.next


s= Stack()
print(s.is_empty())
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.is_empty())
#s.traverse()
print(s.peak())
s.pop()
print(s.peak())