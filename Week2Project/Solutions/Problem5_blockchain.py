import hashlib

def calc_hash(data, time):
      sha = hashlib.sha256()

      hash_str = data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.previous = None
      self.hash = calc_hash(data,0)

import datetime

class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size_ = 0

    def add(self, data):
        data = str(data) 
        if self.head == None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)
            self.tail = self.head
            self._size_ += 1
        else:
            temp = self.tail
            self.tail = Block(datetime.datetime.utcnow(), data, self.tail.hash)
            self.tail.previous = temp
            self._size_ += 1

    def size(self):
       return self._size_
    
    def display(self):
        h = self.tail
        block_num = 1
        while h != None:
            print("BLOCK ", block_num)
            print("TIMESTAMP: ",h.timestamp)
            print("DATA: ", h.data)
            print("HASH: ",h.hash)
            print("PREV_HASH: ", h.previous_hash)
            print("\n")
            h = h.previous
            block_num += 1
        print("CHAIN SIZE: ",self.size())
# TEST 1
print("TEST 1")

test1 = BlockChain()
test1.add("item1")
test1.add("item2")
test1.add("item3")
test1.display()

"""
TEST 1
BLOCK  1
TIMESTAMP:  2021-07-11 15:58:07.578921
DATA:  item3
HASH:  279de9cfc4036787ae07c4dbb60a8d5bb8f1a93acaf4104ae7139ecfcee38539     
PREV_HASH:  df850e4100f3bb071324fc2113a4366bd83e7172ff8ec098a5ab4ec16a80ddf5


BLOCK  2
TIMESTAMP:  2021-07-11 15:58:07.578921
DATA:  item2
HASH:  df850e4100f3bb071324fc2113a4366bd83e7172ff8ec098a5ab4ec16a80ddf5     
PREV_HASH:  0de45cf24f12763c4f4c1731462ef092c3e1a83839439220becaf59518b2c10d


BLOCK  3
TIMESTAMP:  2021-07-11 15:58:07.578921
DATA:  item1
HASH:  0de45cf24f12763c4f4c1731462ef092c3e1a83839439220becaf59518b2c10d
PREV_HASH:  0


CHAIN SIZE:  3
"""

# TEST 2
print("TEST 2")

test1 = BlockChain()
test1.add("item1")
test1.add("")
test1.add("")
test1.display()

"""
TEST 2
BLOCK  1
TIMESTAMP:  2021-07-11 15:58:07.583154
DATA:
HASH:  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
PREV_HASH:  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855


BLOCK  2
TIMESTAMP:  2021-07-11 15:58:07.583154
DATA:
HASH:  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
PREV_HASH:  0de45cf24f12763c4f4c1731462ef092c3e1a83839439220becaf59518b2c10d


BLOCK  3
TIMESTAMP:  2021-07-11 15:58:07.582158
DATA:  item1
HASH:  0de45cf24f12763c4f4c1731462ef092c3e1a83839439220becaf59518b2c10d
PREV_HASH:  0


CHAIN SIZE:  3
"""

# TEST 3
print("TEST 3")

test1 = BlockChain()
test1.add("item1")
test1.add(0)
test1.add(None)
test1.display()

"""
TEST 3
BLOCK  1
TIMESTAMP:  2021-07-11 15:58:07.588138
DATA:  None
HASH:  dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91
PREV_HASH:  5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9


BLOCK  2
TIMESTAMP:  2021-07-11 15:58:07.588138
DATA:  0
HASH:  5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9
PREV_HASH:  0de45cf24f12763c4f4c1731462ef092c3e1a83839439220becaf59518b2c10d


BLOCK  3
TIMESTAMP:  2021-07-11 15:58:07.588138
DATA:  item1
HASH:  0de45cf24f12763c4f4c1731462ef092c3e1a83839439220becaf59518b2c10d
PREV_HASH:  0


CHAIN SIZE:  3
"""