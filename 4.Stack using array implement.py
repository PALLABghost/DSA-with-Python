class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size     # so by mistake we can call stack thats why we can make it private variable
                                        #by adding self.__stack =.........
        self.top = -1       # when stack is empty, if we put 0 then we need to store value in 0 index
    def push(self,value):
        if self.top == self.size - 1:    # suppose size is 3 , so index or top max can reach to 0,1,2
            print("overflow")               # if top value reach more than 2 then overflow
            return
        else:
            self.top += 1
            self.stack[self.top] = value    # store the value in top index -1 +1 = 0 index for first push

    def pop(self):
        if self.top == -1:      #checking if stack is empty or not
            print("Empty")
            return
        else:
            data = self.stack[self.top]
            self.top -= 1
            print(data)

    def traverse(self):
        for i in range(self.top + 1):       # empty stack top value is -1 +1 = 0 index value
            print(self.stack[i], end=' ')

s= Stack(3)
print(s.stack)
s.push(3)
s.push(4)
s.push(5)
print(s.stack)
s.pop()
print(s.stack)
s.traverse()
# after pop also showing the same value, because we are using list,
# while pop we are just changing top , not deleting the top,
#  so while print it print the whole stack items as it is python lists
#so thats why we need to use traverse for print 0 to top, not the whole items store in stack
