## 스택 (Stack)
### Using python list


## 파이썬 리스트로 스택 구현
```python
data_stack = list()

for data in range(3):
    data_stack.append(data)
data_stack
```
Result = [1,2,3]

```python
data_stack.pop()
```
Result = 3 <br/>

#### 1,2,3의 순서로 쌓았기 때문에 마지막에 넣은 3이 먼저 출력
---------------------

## push()와 pop()함수 없이 직접 구현

```python
stack_list = list()

def push(data):
    stack_list.append(data)
    
def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for data in range(10):
    push(data)
```
```python
len(stack_list)
```
Result = 10

---------------------


