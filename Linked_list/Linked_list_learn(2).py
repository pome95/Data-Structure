#!/usr/bin/env python
# coding: utf-8

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1

for index in range(2,10):
    add(index)

# 1뒤에 1.5 노드 추가하기
node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next
node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)




