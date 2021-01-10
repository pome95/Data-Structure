## 큐 (Queue)
### Using python Queue()

```python
import queue
data_queue = queue.Queue()
```
----------------------
#### Queue에 데이터 넣기
**put** 사용
```python
import queue
data_queue = queue.Queue()

data.queue.put("funcoding")
data_queue.put(1)
data_queue.put("korea")
data_queue.qsize()
```
Result = 3

----------------------
#### Queue에 데이터 빼기
**get** 사용

```python
import queue
data_queue = queue.Queue()

data.queue.put("funcoding")
data_queue.put(1)
data_queue.put("korea")
data_queue.get()
```

Result = funcoding

#### FIFO(First In First Out) 방식으로 가장 먼저 넣은 것이 먼저 나온다.

----------------------

### Using python LifoQueue()
```python
import queue
data_queue = queue.LifoQueue()
```
------------------------

#### LifoQueue에 데이터 넣기
**put** 사용
```python
import queue
data_queue = queue.LifoQueue()

data.queue.put("funcoding")
data_queue.put(1)
data_queue.put("korea")
data_queue.qsize()
```
Result = 3

--------------------
#### LifoQueue에 데이터 빼기
**get** 사용

```python
import queue
data_queue = queue.LifoQueue()

data.queue.put("funcoding")
data_queue.put(1)
data_queue.put("korea")
data_queue.get()
```

Result = korea

#### LIFO(Last In First Out) 방식으로 가장 먼저 넣은 것이 가장 나중에 나온다 - 스택 구조

--------------------

### Using python PriorityQueue()
```python
import queue
data_queue = queue.PriorityQueue()
```
------------------------

#### PrioirtyQueue에 데이터 넣기 / 튜플 형태 사용
**put** 사용
```python
import queue
data_queue = queue.PriorityQueue()

data_queue.put((1,"Korea"))
data_queue.put((2,"USA"))
data_queue.put((5,"China"))
data_queue.put((4,"Canada"))
data_queue.put((6,"Japan"))
```

--------------------
#### PriorityQueue에 데이터 빼기
**get** 사용

```python
data_queue.get()
```
Result = (1, 'Korea')

```python
data_queue.get()
```

Result = (2, 'USA')

#### Priority(우선순위) 방식으로 지정된 우선 순위에 따라 출력한다

--------------------


