import ctypes  #using c array
from wsgiref.util import application_uri


class MeraList:
    def __init__(self):
        self.size = 1  #array size is 1 because no item self.n is present
        self.n = 0
        #create a c type array with size self.size
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        ##create a c type array(static, referential) with size capacity
        return (capacity * ctypes.py_object)()
    def __len__(self):
        return self.n
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size * 2)
        #for Append
        self.A[self.n] = item
        self.n = self.n + 1     #revalue of self.n for adding the extra item
    def __resize(self,new_capacity):
        #ceate a new array with a size of new_capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity  # revalue of self.size as size is double
        #copy the content of self.A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign the list B as self.A
        self.A = B      #staore all the content of B with new capacity in self.A

    def __str__(self):      #for printing of list
        #print[1,2,3]
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return "[" + result[:-1] + "]"

L = MeraList()
L.append(10)
L.append(20)
L.append(30)
print(L)