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
      self.hash = calc_hash(data,0)

import datetime

class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size_ = 0

    def add(self, data):
        if self.head == None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)
            self.tail = self.head
            self._size_ += 1
        else:
            self.tail = Block(datetime.datetime.utcnow(), data, self.tail.hash)
            self._size_ += 1

    def size(self):
        return self._size_
