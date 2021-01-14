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
    
    # Node 값 삭제 함수
    def delete(self,data):
        if self.head == '': # 이미 삭제하거나 없는 코드 조회시
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data: # 맨 앞 노드 삭제시
            temp = self.head       # head를 temp로 지정 
            self.head = self.head.next # 다음 값을 head로 지정
            del temp # 기존 head (temp)삭제
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

### 노드 삭제하기
```python
linkedlist1.delete(3) # 예시 3
linkedlist1.desc()
``` 

### Result => 0 1 2 4 5 6 7 8 9