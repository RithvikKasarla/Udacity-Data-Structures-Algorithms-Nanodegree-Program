class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    combinedsets = set()
    
    h = llist_1.head
    while h is not None:
        combinedsets.add(h.value)
        h=h.next

    h = llist_2.head
    while h is not None:
        combinedsets.add(h.value)
        h=h.next

    combined = LinkedList()

    for val in combinedsets:
        combined.append(val)
    if combined.size() == 0:
        return None
    return combined

    
def intersection(llist_1, llist_2):
    list1 = set()
    h = llist_1.head
    while h is not None:
        list1.add(h.value)
        h=h.next

    intersection = LinkedList()
    h = llist_2.head
    list2 = set()
    while h is not None:
        if h.value in list1:
            if h.value not in list2:
                intersection.append(h.value)
                list2.add(h.value)
        h=h.next
    if intersection.size() == 0:
        return None
    return intersection



# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_1,linked_list_2)) # 6 -> 4 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print (intersection(linked_list_3,linked_list_4)) # None

#Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # None
print (intersection(linked_list_3,linked_list_4)) #None
