#!/usr/bin/env python
# coding: utf-8

# 파이썬 객체지향 프로그래밍 연결 리스트 구현

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

# 첫 노드에 0을 넣고 전체 노드 출력하기
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# Result => 0
# 첫 노드에 0 입력 확인 후 

for data in range(1,10):
    linkedlist1.add(data)
linkedlist1.desc()

# Result => 0 1 2 3 4 5 6 7 8 9

