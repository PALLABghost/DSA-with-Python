#stack isempty, push ,peak,pop ,traverse,

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
#text editor using stack, undo and redo operation creation on string

def text_editor(text,pattern):
    u = Stack()
    r = Stack()
    for i in text:
        u.push(i)
    for i in pattern:
        if i == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)
    res = ''
    while not(u.is_empty()):
        res = u.pop() + res
    print(res)

L = [
    [0,0,1,1],
    [0,0,1,0],
    [1,0,0,0],
    [0,0,1,0]
    ]
def find_the_celeb(L):
    s = Stack()
    for i in range(len(L)):
        s.push(i)
    while s.size() >= 2:
        i = s.pop()
        j = s.pop()
        if L[i][j] == 0:
            #j is not celebrity
            s.push(i)
        else:
            # i is not celebrity
            s.push(j)
    celeb = s.pop()
    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                print("No one is a celebrity")
                return
    print("The celebrity is", celeb)


#s= Stack()
#print(s.is_empty())
#s.push(4)
#s.push(5)
#print(s.is_empty())
#s.traverse()
#print(s.peak())
#s.pop()
#print(s.peak())
#reverse_string("Hello")
#text_editor('kolkata','uuuruurr')
find_the_celeb(L)
