#!/usr/bin/env python
# coding: utf-8

# ## 해쉬 테이블 (Hash Table)

# ### 기본 해쉬 테이블 간단 구현해보기


# 파이썬 list comprehension 사용

# 파이썬 list()를 사용하여 10칸의 테이블을 생성
hash_table = list([0 for i in range(10)])

# 데이터 입력
data1='Andy'
data2='Dave'
data3='Trump'

# 데이터 출력
print(ord(data1[0]),ord(data2[0]),ord(data3[0]))

# ord() => 문자의 ASCII 코드를 리턴해주는 함수
 
# Return => 65 68 84 
# 이런 방식으로 가능
# -----------------------------------------

# 해쉬 테이블 작성해보기

hash_table = list(0 for i in range(10))

# 해싱 함수 생성
def hash_func(key):
 return key % 5

# 데이터 저장하기
def storage_data(data,value):
 key = ord(data[0])
 hash_address = hash_func(key)
 hash_table[hash_address]=value

# 데이터 꺼내기
def get_data(data):
 key = ord(data[0])
 hash_address = hash_func(key)
 return hash_table[hash_address]

storage_data('Andy','01011112222')
storage_data('Dave','01033334444')
storage_data('Trump','01055556666')

get_data('Andy')

# Result => '01011112222'
# Andy에 해당하는 데이터가 출력됨을 확인

# --------------------------------------

# 코드 간결하게 
hash_table=list([0 for i in range(8)]) # list comprehension 사용 => 8칸 테이블 생성

# 키값을 가져오는 함수
def get_key(data):
    return hash(data)

# 해싱 함수 => Division법 %8 사용
def hash_function(key):
    return key % 8

# 데이터 저장 부분
def save_data(data,value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

# 데이터 출력 부분   
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]
  

save_data('Dave','0102030200')
save_data('Andy','01033232200')

read_data('Dave')
# Result => '0102030200'
# 데이터가 테이블에 들어간 것을 확인가능

hash_table

# Result => [0, 0, 0, '0102030200', 0, 0, 0, '01033232200']
# 해당 데이터가 Division(나머지) 연산에 의해 자리에 들어간 것 확인 가능



