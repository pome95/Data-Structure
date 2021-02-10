#!/usr/bin/env python
# coding: utf-8

# ## 해시 테이블 (Hash Table)

# ### 해시 테이블 구현해보기

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
