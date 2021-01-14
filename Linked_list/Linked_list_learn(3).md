## 연결 리스트 (Linked_list)
### Using python Class Node

### 파이썬 객체 지향 프로그래밍 연결 리스트 구현

**Node 구현(Class)**
```python
# Node Class 생성
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
        if self.head == '': # 헤드 값이 없는 경우
            self.head == Node(data) # 넣은 데이터를 헤드로 지정
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
```

### 첫 노드에 0을 넣고 전체 노드 출력하기
```python
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
```
0이 정상 출력되고
```python
for data in range(1,10):
    linkedlist1.add(data)
linkedlist1.desc()
```
### Result => 0 1 2 3 4 5 6 7 8 9