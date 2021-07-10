As in an LRU Cache it has a limited size cache where the least recently used one is removed. I decided to use Queue to handle the least used part of the cache and, as a queue is a first in last out data structure. 
In the queue I made a modified push statement which makes it so if an item in the queue is pushed onto the queue it moves that item to the back of the queue and removes it from its original place. This makes it so the last used one will end up being at the front of the queue, the next one to be popped off.

Then I used a dictionary to handle the key value pairs.

The efficency of the get and set function in the LRU Cache is O(1) and space is O(k) where k is the size of the cache which is given by the user.