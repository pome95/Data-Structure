#!/usr/bin/env python
# coding: utf-8

# 해당 Node 삭제 하기

# Node 클래스 생성
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# Node 관리 클래스 생성
class NodeMgmt:
    def __init__ (self,data):
        self.head = Node(data)
    
    # Node 값 추가 함수
    def add(self,data):
        if self.head == '':
            self.head == Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    
    # Node 값 출력 함수
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # Node 값 삭제    
    def delete(self,data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next =  node.next.next
                    del temp
                    return
                else:
                    node = node.next

linkedlist1 = NodeMgmt(0)
for data in range(1,10):
    linkedlist1.add(data)
linkedlist1.desc()

# Result => 0 1 2 3 4 5 6 7 8 9

linkedlist1.delete(3)
linkedlist1.desc()

# Result => 0 1 2 4 5 6 7 8 9
# delete()로 지정한 3 노드 삭제