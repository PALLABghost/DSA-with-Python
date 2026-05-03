#3.What is the output of following function when head node of following lint is passed as input?
# 1->2->3->4->5
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def fun(head):
    if (head == None):
        return
    if head.next.next != None:
        print(head.data,"",end='')
        fun(head.next)              #recursion
    print(head.data,"",end='')

# Create nodes
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

fun(head)



