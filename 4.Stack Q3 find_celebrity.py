#find the celebrity who doest know anyone, but everyone knows him.
#find the celebrity using stack,
#find the celebrity using two pointer
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

def find_the_celeb(L):
    s = Stack()
    for i in range(len(L)):
        s.push(i)       #pusing al the person in bucket
    while s.size() >= 2:
        i = s.pop()         
        j = s.pop()
        if L[i][j] == 0:        #person i doesnt know person j
            #j is not celebrity
            s.push(i)
        else:                   # L[i]L[j] == 1 #person i know person j
            # i is not celebrity
            s.push(j)
    celeb = s.pop()             #now one possible celebrity, but not guaranteed yet.
    for i in range(len(L)):
        if i != celeb:              #check all the posibilty with other,except not with himself
            if L[i][celeb] == 0 or L[celeb][i] == 1:    # everybody dont know celeb but celeb knows anyone
                print("No one is a celebrity")
                return
    print("The celebrity is", celeb)

def find_celeb_two_pointer(L):
    n = len(L)
    # Step 1: find a candidate
    celeb = 0       #assume person 0 is the initial candidate
    for i in range(1,n): #No need to compare 0 with itself,We only compare it with the rest of the people (1 → n-1)
        if L[celeb][i] == 1:   #if celeb know i then celeb is not celebrity, if celeb dont know i then loop not execute and we will find the person who is dont know anyone
            celeb = i           # loop execute so celeb know i and now we need to verify is i know anyone ? so celab = i again loop will run for checking if i knows anyone
    # Step 2: verify the candidate
    for i in range(n):  # now celeb value changes so we cant skip 0 position also
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:    # we are checking negative way, everybody dont know celeb but celeb knows anyone
                print("No one is a celebrity")
                return
    print("The celebrity is", celeb)


L = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
    ]

find_the_celeb(L)
find_celeb_two_pointer(L)