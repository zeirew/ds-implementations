#Separate Chaining Approach

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def set_next(self, next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value 
    
    def __str__(self):
        return "Key: " + str(self.key) + " Value: " + str(self.value)

#Space Complexity: O(N)
class HashTable:
    def __init__(self, starting_capacity):
        self.capacity = starting_capacity
        self.size = 0
        self.buckets =  [None] * self.capacity
    
    ##O(N) in worst case, where all nodes are present in the same bucket and this node will be added to the same bucket 
    def add(self, key, value):
        index = self.get_hash(key)
        self.size +=1
        if(self.buckets[index] is None):
            self.buckets[index] = Node(key, value)
        else:
            new_node = Node(key, value)
            curr_node = self.buckets[index]
            while(curr_node.get_next() is not None):
                curr_node = curr_node.get_next()
            curr_node.set_next(new_node)

    # O(N) in worst case, where all nodes are present in the same bucket and the desired node is at the very end
    def get(self, key):
        index = self.get_hash(key)
        curr_node = self.buckets[index]

        while(curr_node is not None):
            if(curr_node.get_key() == key):
                return curr_node.get_value()
            curr_node = curr_node.get_next()
        return None
    
    # O(N) in worst case, where all nodes are present in the same bucket and the node to be deleted is at the very end
    def remove(self, key):
        index = self.get_hash(key)
        curr_node = self.buckets[index]

        #Case 1: key is at start of list
        if(curr_node.get_key() == key):
            self.buckets[index] = curr_node.get_next()
            val = curr_node.get_value()
            curr_node = None
            return val

        #Case 2: key is in middle/end of list
        prev = None
        while(curr_node is not None and (curr_node.get_key() != key)):
            prev = curr_node
            curr_node = curr_node.get_next()

        if(curr_node is not None):
            prev.set_next(curr_node.get_next())
            val = curr_node.get_value()
            curr_node = None
            return val

        #Case 3: key is not in list
        return None

    def get_hash(self, key):
        total = 0
        for i, c in enumerate(key): 
            total += i * hash(c)
        return total % (self.capacity)

    def __str__(self):
        for i, b in enumerate(self.buckets):
            print("\nBucket # " + str(i))
            curr_node = b
            while(curr_node is not None):
                print("\t" + curr_node.__str__())
                curr_node = curr_node.get_next()
'''
ht = HashTable(6)
ht.add("Wendy", "30")
ht.add("Wendy", "50")
ht.add("Thomas", "76")
ht.add("Wendy", "75")
ht.add("Billington", "21")
print(ht.get("Wendy"))
print(ht.__str__())
ht.remove("Wendy")
print(ht.__str__())
'''
