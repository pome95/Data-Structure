#!/usr/bin/env python
# coding: utf-8

# ## 해쉬 테이블 (Hash Table)

# ### 기본 해쉬 테이블 생성과 데이터 입력 및 출력해보기
# #### 파이썬 list comprehension 사용

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
