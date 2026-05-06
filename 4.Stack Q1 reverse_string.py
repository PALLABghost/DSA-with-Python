#reverse a string using stack, In place reversal
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0
    def size(self):
        return self.n
    def is_empty(self):
        return self.top is None     #if top is none is_empty will return true, either it will return false

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.n = self.n + 1

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
        if self.top is None:
            return "Stack Empty"
        else:
            data = self.top.data
            self.top = self.top.next
            self.n = self.n -1
            return data

#reverse a string using stack
def reverse_string(text):
    s1 = Stack()
    for i in text:
        s1.push(i)
    res = ''
    while not (s1.is_empty()):
        res = res + s1.pop()
    print(res)



reverse_string("Hello")