class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.size = 0
        self.cache = dict()
        self.LRU = Queue()
        self.cap = capacity

    def get(self, key):
        if self.LRU.contains(key):
            self.LRU.push(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            return
        
        if self.size >= self.cap:
            self.LRU.pop()
            self.LRU.push(key)
            self.cache[key] = value
        else:
            self.LRU.push(key)
            self.cache[key] = value
            self.size += 1
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
            self.size += 1
    
    def pop(value):
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return self.head.value
        else:
            prev = self.head
            temp = self.head.next

            while temp.next != None:
                if temp.value == value:
                    prev.next = temp.next
                    return temp.value
                else:
                    prev = temp
                    temp = temp.next
            return -1

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self,value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = self.head
            if self.head.value == value:
                self.head = self.head.next
                self.tail.next = Node(value)
                self.tail = self.tail.next
                return
            while node.next is not None:
                if node.next.value == value:
                    node.next = node.next.next
                    self.tail.next = Node(value)
                    self.tail = self.tail.next
                    return
                node = node.next
            self.tail.next = Node(value)
            self.tail = self.tail.next
    
    def pop(self):
        if self.head == None:
            return
        else:
            v = self.head.value
            self.head = self.head.next
            return v
    
    def print_(self):
        node = self.head
        s = ""
        while node is not None:
            s = s + str(node.value)
            node = node.next
        print("QUEUE ->" ,s)
            
    def contains(self,key):
        node = self.head
        while node is not None:
            if node.value == key:
                return True
            node = node.next
        return False
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4) 

print(our_cache.get(1) )      # returns 1
print(our_cache.get(2) )      # returns 2
print(our_cache.get(9)     ) # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
 
