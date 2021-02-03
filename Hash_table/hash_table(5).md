## 해시 테이블 (Hash_table)
### Using python Hashlib()
<br/>

## 해시 테이블 구현 (Hashlib)  
<br/>

### 해시 라이브러리 사용 예시
SHA 함수 사용 => Secure Hash Algorithm
어떤 데이터도 고정된 크기의 고정 값을 리턴한다. => 해시 함수로 유용하게 활용

---

#### SHA1
```python
import hashlib

data='test'.encode() # 문자열 encode() -> byte 형태 
hash_object = hashlib.sha1() # test 값의 SHA1 함수를 사용하여 변환
hash_object.update(b'test')
hex_dig = hash_object.hexdigest() # 16진수 함수 .hexdigest()
print(hex_dig)
```
Result => a94a8fe5ccb19ba61c4c0873d391e987982fbbd3

#### SHA256
```python
import hashlib

data='test'.encode() # 문자열 encode() -> byte 형태
hash_object = hashlib.sha256() # test 값의 SHA256 함수를 사용하여 변환
hash_object.update(b'test')
hex_dig = hash_object.hexdigest() # 16진수 함수 .hexdigest()
print(hex_dig)
```
Result => 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08

---


### 해시 테이블 생성
Linear Probing 기법에 해시 라이브러리를 사용하여 구현

#### 해시 라이브러리 사용
```python
import hashlib
hash_table = list([0 for i in range(8)])
```
#### 해시 라이브러리 사용 키가져오기
```python
def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig,16)
```

#### 해싱 함수 (Division법 사용)
```python
def hash_function(key):
    return key % 8
```

#### 데이터 저장 함수
```python
def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address]!=0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index]==0:
                hash_table[index]=[index_key,value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address]=[index_key,value]
```

#### 데이터 출력 함수
```python
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address]!=0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None
```

##### 값 찾기
```python
print(get_key('db')%8)
print(get_key('da')%8)
print(get_key('dh')%8)
```

Result => 1 2 2

##### 값 출력
```python
save_data('db','01011112222')
save_data('da','01022223333')
save_data('dh','01033334444')
```

##### 해시 테이블 확인
```python
hash_table
```
[0,[56023447740326973930934189836995694929976025384421001605890631798736143110161, '01011112222'], [77049896039817716104633086125973601665927154587286664305423403838091909979274,  '01022223333'], [25902807790238191969936164090115518991880572428612380032453909518048593055890,  '01033334444'], 0, 0, 0, 0]

1번째 테이블에 'db'값이 들어가고 2번에 'da'값이 들어가고 'dh는 2번이지만 Linear Probing 기법에 의해 그 다음인 비어있는 3번에 저장이 된다.

#### 시간복잡도
 * 일반적인 경우 (Collision X) O(1)
 * 최악의 경우 (Collision O (모두 발생하는 경우)) O(n)
 > 해시 테이블의 경우, 일반적인 경우를 기대하고 만듬 -> O(1)
 
#### 검색에서 해시 테이블
 * 16개의 배열에 데이터를 저장, 검색할 때 O(n)
 * 16개의 데이터 공간에 해시 테이블을 저장, 검색할 때 O(1)