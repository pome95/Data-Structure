## 이진 트리 삭제(Binary Tree)

### Using python Class Node

#### Node Class 생성
```python
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
```

#### Node 관리 Class 생성
```python
class NodeMgmt:
    def __init__(self,head):
        self.head = head
```

#### Node 추가 함수 생성
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
```

#### Node 탐색 함수 생성
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

#### Node 삭제 함수 생성
```python
    def delete(self,value):    
        searched = False
        self.current_node = self.head
        self.parent = self.head

        # 삭제할 Node 찾기
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            return False
        
        # Case 1 삭제할 Node가 leaf node인 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        # Case 2 삭제할 Node가 Child Node를 한개 가지고 있을 경우 - 2가지 경우로 나뉜다.

        # Case 2.1 삭제할 Node의 Child Node가 왼쪽인 경우        
        elif self.current_node.left!=None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.left = self.current_node.right

        # Case 2.2 삭제할 Node의 Child Node가 오른쪽인 경우
        elif self.current_node.left == None and self.current_node.right!=None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # Case 3 삭제할 Node가 Child Node를 두개 가지고 있을 경우 - 2가지 경우와 각각의 2가지 경우로 또 나뉜다.
        else:

            # Case 3.1 삭제할 Node가 Parent(삭제할 Node의) 왼쪽인 경우
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                
                # case 3.1.1 오른쪽 자식중 가장 작은 값의 Node에 child가 없을때
                while self.change_node.left!=None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left

                # case 3.1.2 오른쪽 자식중 가장 작은 값의 node에 오른쪽 child
                if self.change_node.right!=None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None

                self.parent.left = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
                    
            # Case 3.2 삭제할 Node가 Parent(삭제할 Node의) 오른쪽인 경우
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                # case 3.2.1 오른쪽 자식중 가장 작은 값의 Node에 chile가 없을때
                while self.change_node.left!=None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left

                # case 3.2.2 오른쪽 자식중 가장 작은 값의 Node에 오른쪽 child    
                if self.change_node.right!=None:
                    self.change_node_parent.left = self.change_node.righ
                else:
                    self.change_node_parent.left =None

                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
        return True
```