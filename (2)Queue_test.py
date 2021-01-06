#!/usr/bin/env python
# coding: utf-8

# ## 큐 만들기 Queue() 사용

import queue

data_queue = queue.Queue()


# #### Queue()에서 put => enqueue,  get => dequeue


data_queue.put("funcoding")
data_queue.put(1)
data_queue.qsize()

# =>  2


data_queue.put("nojamcoding")
data_queue.qsize()

# => 3




# ### LifoQueue() 사용

import queue
data_queue = queue.LifoQueue()

data_queue.put("funcoding")
data_queue.put(1)
data_queue.qsize()


# => 2


data_queue.get()

# => 1
# ##### Last in First out에 맞게 나중에 넣은 것이 먼저 나온다 => 스택구조




# ### PriorityQueue() 사용

import queue
data_queue = queue.PriorityQueue()


# ###### 튜플형태로 (())
# ##### 앞이 우선순위 숫자 (낮을 수록 먼저 나옴)

data_queue.put((1,"Korea"))
data_queue.put((2,"USA"))
data_queue.put((5,"China"))
data_queue.put((4,"Canada"))
data_queue.put((6,"Japan"))

data_queue.qsize()

# => 5

data_queue.get()

# => (1, 'Korea')

data_queue.get()

# => (2, 'USA')

data_queue.get()

# => (4, 'Canada')





# ## Enqueue Dequeue 기능 구현하기

queue_list = list()

def enqueue(data):
    queue_list.append(data)
    
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for data in range(10):
    enqueue(data)

len(queue_list)

# => 10

dequeue()

# => 0

dequeue()

# => 1

dequeue()

# => 2

# ## Enqueue로 데이터를 넣고 Dequeue로 데이터를 뼤고