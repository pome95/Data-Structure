#!/usr/bin/env python
# coding: utf-8

# ## 스택

# ## 파이썬 리스트 기능으로 스택 구현


data_stack = list()

for data in range(3):
    data_stack.append(data)
data_stack

# => [0,1,2]

data_stack.pop()

# => 2

# #### 1,2,3의 순서로 쌓았기 때문에 마지막에 쌓은 3이 먼저 출력




#  ### push()와 pop() 함수 사용없이 직접 구현하기

stack_list = list()

def push(data):
    stack_list.append(data)
    
def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)
    
len(stack_list)

# => 10

pop()

# => 9

pop()

# => 8

# #### push는 append를 통해 data를 입력 => 반복문으로 10개의 숫자를 자동입력
# #### pop은 stack_list(생성된 스택)의 마지막을 출력하고 삭제
# #### [0]인 경우 맨처음 [-1]인 경우 무조건 맨 마지막
# #### 큐의 반대 방법으로 구현
# ####  큐    <==>   스택
# #### FIFO <==> LIFO