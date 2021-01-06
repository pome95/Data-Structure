## 큐 (Queue)
### Using python Queue()

```c
import queue
data_queue = queue.Queue()
```
---------------------

**Queue에 데이터 넣기**
**put** 
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
**Queue에 데이터 빼기**
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

----------------------


2차원 배열: 리스트로 구현시
```c
data = [[1,2,3],[4,5,6],[7,8,9]]
print(data)
```
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

---------------------

2차원 배열 출력하기
```c
data = [[1,2,3],[4,5,6],[7,8,9]]
print(data[0])
```
[1,2,3]

---------------------

2차원 배열 전부 출력하기
```c
print(data[0][0],data[0][1],data[0][2],data[1][0],data[1][1],data[1][2],data[2][0],data[2][1],data[2][2])
```
1 2 3 4 5 6 7 8 9

---------------------

4X4 배열 만들고 출력하기 (반복문)
```c
data = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j]
```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
              
##### i는 len(data)만큼 -> data의 길이만큼(4)
##### j는 len(data[i])만큼 -> 반복된 i안의 요소 길이 만큼 (4) -> 4x4 행렬
