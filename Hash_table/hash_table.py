#!/usr/bin/env python
# coding: utf-8

# ## 해쉬 테이블 (Hash Table)

# ### 기본 해쉬 테이블 생성과 데이터 입력 및 출력해보기
# #### 파이썬 list comprehension 사용

hash_table = list([0 for i in range(10)])

def hash_func(key):
  return key % 5
  
data1='Andy'
data2='Dave'
data3='Trump'

print(ord(data1[0]),ord(data2[0]),ord(data3[0]))

# Return => 65 68 84 
