# import sys 
# L = []

# for i in range(100):
#   print(i,"hello",sys.getsizeof(L))
#   L.append(i)

import ctypes

class meralist:
    def __init__(self):
        self.size = 1
        self.n = 0 
        #create a ctype array with size = self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
      result = ''
      for i in range(self.n):
        result = result + str(self.A[i])+','
      return '[' + result[:-1] + ']'

    def append(self,item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)
        
        #append
        self.A[self.n] = item
        self.n = self.n + 1

    def __resize(self,new_capacity):
        #create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
            #resize a
        self.A = B

    def __make_array(self,capacity):
        #create a C type array(static,referential) with size capacity
        return (capacity*ctypes.py_object)()

L = meralist()
L.append(3.4)
L.append("hello")
L.append("f")

print(L)
