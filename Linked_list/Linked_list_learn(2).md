## 배열 (Array)
### Using python Class Node

**Node 구현(Class)**
```python
# Node Class 생성
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
# Node add 함수 생성    
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

# 첫 노드 1 입력, 헤드 지정
node1 = Node(1)
head = node1

# 2~9까지 데이터 넣기
for index in range(2,10):
    add(index)
```
**Node 사이에 데이터 추가하기**
```python
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
```
```python
# 출력 부분
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
