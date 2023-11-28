import ctypes

class DynamicArray(object):

    #Retrieval Item: O(1)
    #Insert: worst case: we'll have to resize array AND insert at the beginning O(N) + O(N) = O(2N) = O(N)
    #RemoveAt: O(N) in the worst case
    #Delete: O(1)
    #Append: worst case: resize + append O(N), otherwise, O(1)

    def __init__(self):
        self.n = 0 #num elements
        self.capacity = 1 #default capacity
        self.A = self.make_array(self.capacity) #array

    def __len__(self): #we use double underscore to avoid naming conflicts
        return self.n
    
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError("Index out of bounds")
        return self.A[k]
    
    def append(self, element):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        self.A[self.n] = element
        self.n +=1 
    
    def insertAt(self, item, index):
        if index < 0 or index > self.n:
            return IndexError("Index out of bounds")
        
        if self.n == self.capacity:
            self.__resize(2 * self.capacity)

        for i in range(self.n-1, index-1, -1):
            self.A[i+1] = self.A[i]
        
        self.A[index] = item
        self.n += 1

    def delete(self):
        if self.n == 0:
            print("Array is empty.")
            return

        self.A[self.n-1] = None
        self.n -= 1
    
    def removeAt(self, index):
        if self.n == 0:
            print("Array is empty.")
            return
        
        if index < 0 or index >= self.n:
            return IndexError("Index out of bounds")
        
        if index == self.n-1:
            self.A[index] = 0
            self.n -= 1
            return
        
        for i in range(index, self.n-1):
            self.A[i] = self.A[i+1]

        self.A[self.n-1] = None
        self.n -= 1

    def _resize(self, new_capacity):
        new_array = self.make_array(new_capacity)

        for i in range(self.n):
            new_array[i] = self.A[i]

        self.A = new_array
        self.capacity = new_capacity

    def make_array(self, array_capacity):
        return (array_capacity * ctypes.py_object)() 



'''
# Instantiate
arr = DynamicArray()

# append the new elements
arr.append(1)
arr.append(2)
arr.append(3)
 
# length of the given append in array
print(len(arr))
 
# access the given append in array
print(arr[1])
print(arr[2])
 
# remove the given the array
arr.removeAt(2)
 
# length of the array
print(len(arr))
 
# index of the array
print(arr[1])
'''
