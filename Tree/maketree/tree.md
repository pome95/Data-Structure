## 이진 트리 (Binary Tree)

### Using python Class Node

### Node 클래스 생성
```python
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
```

### Node 관리 클래스 생성
```python
class NodeMgmt:
    def __init__(self,head):
        self.head = head
```

---

#### Tree Node 추가 함수
```python
    def insert(self,value):
        self.current_node = self.head

        while True:
            if value < self.current_node.value:
                if self.current_node.left!=None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break

            else:
                if self.current_node.right!=None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
```
1. head값을 현재 노드로 지정
2. 반복문 (값 비교)
3. 입력한 노드의 값이 현재 노드의 값보다 작은 경우 - Tree의 왼쪽으로
    * 왼쪽 노드 값(self.current_node.left)이 있는 경우
        * 왼쪽 노드를 현재 노드로 지정하고 다시 반복문 비교 시작
    * 왼쪽 노드 값(self.current_node.left)이 비어 있는 경우
        * 왼쪽 노드에 값을 저장하고 반복문 break  
  
4. 입력한 노드의 값이 현재 노드의 값보다 큰 경우 - Tree의 오른쪽으로
    * 오른쪽 노드 값(self.current_node.right)이 있는 경우
        * 오른쪽 노드를 현재 노드로 지정하고 다시 반복문 비교 시작
    * 오른쪽 노드 값(self.current_node.right)이 비어 있는 경우
        * 오른쪽 노드에 값을 저장하고 반복문 break

---

#### Tree Node 탐색 함수
```python
    def search(self,value):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
```
1. head값을 현재 노드로 지정
2. 반복문 (값 비교)
3. 찾는 노드의 값이 현재 노드의 값인 경우 True 출력
    * 찾는 노드의 값이 현재 노드의 값보다 작은 경우 - Tree의 왼쪽으로
        * 왼쪽 노드를 현재 노드로 지정하고 다시 반복문 비교 시작
    * 찾는 노드의 값이 현재 노드의 값보다 큰 경우 - Tree의 오른쪽으로
        * 오른쪽 노드를 현재 노드로 지정하고 다시 반복문 비교 시작  
  
4. 값이 없는 경우 False 출력

---

##### Node에 값 추가하기
```python
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)
```

##### Node에 값 탐색하기
```python
BST.search(8)
```
Result => True

```python
BST.search(5)
```
Result => False