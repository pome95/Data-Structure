## 해시 테이블 (Hash_table)
### Using python list comprehension  \
<br/>

## 해시 테이블 충돌 해결 (Linear Probing))  
<br/>

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
  <br/>

### 해싱 함수 -> Division법 % 8 사용
```python
def hash_function(key):
    return key % 8
```  
<br/>

### 데이터 입력 함수
```python
def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address]!=0:
        for index in range(hash_address,len(hash_table)):
            if hash_table[index]==0:
                hash_table[index] = [index_key,value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address]=[index_key,value]
```
  
  <br/>
  
### 데이터 출력 함수
```python
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address]!=0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index]==0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None
```  
<br/>

동일한 주소값에 데이터를 2개 넣기 위해 미리 계산해서 찾아보았다.
(주소 값은 매번 변경이 된다)
```python
print (hash('Dave') % 8)
print (hash('Dd') % 8)
print (hash('Data') % 8)
```

Result => 0 5 5
나누기 결과 5로 같은 결과가 나오는 것을 확인                                           
<br/>

#### 데이터 넣기
```python
save_data('Dd', '1201023010')
save_data('Data', '3301023010')
read_data('Dd')
```
Result => '1201023010'
정상적으로 데이터가 입력되어 출력됨을 확인  
<br/>

#### 해시 테이블 출력
```python
hash_table
```

Result => [0,0,0,0,0,[5532289232361108405, '1201023010'], [872982679201566045, '3301023010'],0]  
'Dd'의 값이 5번째 테이블에 들어가고 'Data' 값이 5번째가 아닌 그 다음번째에 들어간 것 확인   
