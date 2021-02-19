class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class NodeMgmt:
    def __init__(self,head):
        self.head = head
    
    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left!=None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
                    
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
    
    def delete(self,value):
        
        searched = False
        self.current_node = self.head
        self.parent = self.head
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
        
        if self.current_node.left == None and self.current_node.righte == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
                
        elif self.current_node.left!=None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.left = self.current_node.right
        
        elif self.current_node.left == None and self.current_node.right!=None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
                
        else:
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
                    # case 3.2
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                # case 3.2.1 오른쪽 자식중 가장 작은 값의 Node에 child가 없을때
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