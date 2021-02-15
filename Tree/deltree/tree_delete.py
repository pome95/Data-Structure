#!/usr/bin/env python
# coding: utf-8

# 기본 베이스
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
    
    ## 이후부터 case를 분리
    
    # 1. 삭제할 Node가 leaf node인 경우
    # self.current_node가 삭제할 Node
    # self.parent는 삭제할 Node의 parent Node인 상태
    
    if self.current_node.left == None and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left = None
        else:
            self.parent.right = None
        del self.current_node
        
    # 2. 삭제할 Node가 Chile Node를 한 개 가지고 있을 경우
    
    # 1) 왼쪽에 Child Node가 있을경우
    
    if self.current_node.left!=None and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left = self.current_node.left
        else:
            self.parent.left = self.current_node.right
    # 2) 오른쪽에 Child Node가 있을 경우
    
    if self.current_node.left == None and self.current_node.right!=None:
        if value < self.parent.value:
            self.parent.left = self.current_node.right
        else:
            self.parent.right = self.current_node.right
            
            
    # 3. 삭제할 Node가 Child Node를 두 개 가지고 있을 경우
    # 삭제할 Node의 오른쪽 자식 중 가장 작은 값을 삭제할 
    # Node의 Parent Node가 가리키도록 한다
    
    # 3.1 삭제할 Node가 Parent Node 왼쪽에 있을 경우
    # case 3
    if self.current_node.left!=None and self.current_node.right!=None:
        # case 3.1
        if value < self.parent.value:
            self.change_node = self.current.node.right
            self.change_node_parent = self.current_node.right
            # case 3.1.1 오른쪽 자식중 가장 작은 값의 Node에 chile가 없을때
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
            
    # 3.2 삭제할 Node가 Parent Node 오른쪽에 있을 경우
        # case 3.2
        else:
            self.change_node = self.current.node.right
            self.change_node_parent = self.current_node.right
            # case 3.2.1 오른쪽 자식중 가장 작은 값의 Node에 chile가 없을때
            while self.change_node.left!=None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            # case 3.2.2 오른쪽 자식중 가장 작은 값의 Node에 오른쪽 child    
            if self.change_node.right!=None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parnet.left =None
                
            self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right
            
            # 세부 case의 이유
            # 가장 작은 값을 가진 Node의 왼쪽 Child는 존재 할 수 없음

