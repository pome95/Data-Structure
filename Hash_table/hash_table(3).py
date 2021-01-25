#!/usr/bin/env python
# coding: utf-8

# ## 해시 테이블 (Hash Table)

# ### 해시 테이블 충돌

hash_table=list([0 for i in range(8)]) # list comprehension 사용 => 8칸 테이블 생성

# 키값을 가져오는 함수
def get_key(data):
    return hash(data)

# 해싱 함수 => Division법 %8 사용
def hash_function(key):
    return key % 8
    
def save_data(data,value):
