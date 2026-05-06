#find the celebrity who doest know anyone, but everyone knows him.
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

def find_the_celeb(matrix):
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


L = [
    [0,0,1,1],
    [0,0,1,0],
    [1,0,0,0],
    [0,0,1,0]
    ]

find_the_celeb(L)