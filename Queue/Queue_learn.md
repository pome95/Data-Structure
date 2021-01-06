## 큐 (Queue)
### Using python Queue()

```c
import queue
data_queue = queue.Queue()
```
---------------------

### Queue에 데이터 넣기
**put** 사용
```c
import queue
data_queue = queue.Queue()

data.queue.put("funcoding")
data_queue.put(1)
data_queue.put("korea")
data_queue.qsize()
```
3

--------------------
### Queue에 데이터 빼기**
**get** 사용

```c
import queue
data_queue = queue.Queue()

data.queue.put("funcoding")
data_queue.put(1)
data_queue.put("korea")
data_queue.get()
```

funcoding

#### FIFO(First In First Out) 방식으로 가장 먼저 넣은 것이 먼저 나온다.

----------------------

### Using python LifoQueue()
```c
import queue
data_queue = queue.LifoQueue()
```
------------------------

### LifoQueue에 데이터 넣기
**put** 사용
```c
import queue
data_queue = queue.LifoQueue()

data.queue.put("funcoding")
data_queue.put(1)
data_queue.put("korea")
data_queue.qsize()
```
3

--------------------
### Queue에 데이터 빼기
**get** 사용

```c
import queue
data_queue = queue.Queue()

data.queue.put("funcoding")
data_queue.put(1)
data_queue.put("korea")
data_queue.get()
```

korea

#### LIFO(Last In First Out) 방식으로 가장 먼저 넣은 것이 가장 나중에 나온다 - 스택 구조

--------------------

