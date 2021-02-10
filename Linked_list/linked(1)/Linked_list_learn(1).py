#!/usr/bin/env python
# coding: utf-8
#----------
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
#-----------

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        
def add(data):
    node = head
    while node.next:
         node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1

for index in range(2,10):
    add(index)


node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

# => 1 2 3 4 5 6 7 8 9