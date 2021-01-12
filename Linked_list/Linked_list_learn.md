## 배열 (Array)
### Using python Class Node

**Node 구현(Class)**
```python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
```
or
```python
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
```
---

**Node 구현 + Node 데이터 추가**
```python
# Node Class 생성
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# Node 추가 함수        
def add(data):
    node = head
    while node.next:
         node = node.next
    node.next = Node(data)

# 첫 노드 1 넣고 헤드 지정
node1 = Node(1)
head = node1

# 2~9까지 데이터 넣기
for index in range(2,10):
    add(index)

#출력 부분
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
```

Result = 1,2,3,4,5,6,7,8,9