## 해시 테이블 (Hash_table)
### Using python list comprehension

## 해시 테이블 충돌 해결 (Chaining)

### 해시 테이블 생성
```python
hash_table=list([0 for i in range(8)])
```
list comprehension 사용 -> 8칸의 테이블 생성  

<br/>

### 키값을 가져오는 함수
```python
def get_key(data):
    return hash(data)
```

### 해싱 함수 -> Division법 % 8 사용
```python
def hash_function(key):
    return key % 8
```

### 데이터 입력 함수
```python
def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address]!=0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index[1] == value
                return
        hash_table[hash_address].append([index_key,value])
    else:
        hash_table[hash_address] = [[index_key,value]]
```

### 데이터 출력 함수
```python
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address]!=0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
               return hash_table[hash_adress][index][1]
        return None
    else:
        return None
```

동일한 주소값에 데이터를 2개 넣기 위해 미리 계산해서 찾아보았다.
(주소 값은 매번 변경이 된다)
```python
print (hash('Dave') % 8)
print (hash('Dd') % 8)
print (hash('Data') % 8)
```

Result => 0 5 5
나누기 결과 5로 같은 결과가 나오는 것을 확인                                         
      
#### 데이터 넣기
```python
save_data('Dd', '1201023010')
save_data('Data', '3301023010')
read_data('Dd')
```
Result => '1201023010'
정상적으로 데이터가 입력되어 출력됨을 확인

#### 해시 테이블 출력
```python
hash_table
```

Result => [0,0,0,0,0,[[5532289232361108405, '1201023010'], [872982679201566045, '3301023010']],0,0]
출력된 값이 9칸으로 보이지만 사실 5번주소에 2개의 데이터가 연결 리스트로 삽
