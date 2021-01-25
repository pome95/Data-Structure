## 해시 테이블 (Hash_table)
### Using python list comprehension

## 해시 테이블 형태

### 파이썬 list()를 사용하여 10칸의 테이블을 생성
```python
hash_table = list([0 for i in range(10)])
```

### 데이터 입력
```python
data1='Andy'
data2='Dave'
data3='Trump'
```

### 데이터 출력
```python
print(ord(data1[0]),ord(data2[0]),ord(data3[0]))
```

ord() => 문자의 ASCII 코드를 리턴해주는 함수 <br/>
Return => 65 68 84 

---

## 함수 생성으로 해시 테이블 작성해보기
```python
hash_table = list(0 for i in range(10))
```

### 해싱 함수 생성
```python
def hash_func(key):
 return key % 5
```

### 데이터 입력 함수 생성
```python
def storage_data(data,value):
 key = ord(data[0])
 hash_address = hash_func(key)
 hash_table[hash_address]=value
```

### 데이터 출력 함수 생성
```python
def get_data(data):
 key = ord(data[0])
 hash_address = hash_func(key)
 return hash_table[hash_address]
```

### 데이터 입력
```python
storage_data('Andy','01011112222')
storage_data('Dave','01033334444')
storage_data('Trump','01055556666')
```

### 데이터 출력
```python
get_data('Andy')
```
Result => '01011112222' <br/>
Andy에 해당하는 데이터가 출력됨을 확인

---



