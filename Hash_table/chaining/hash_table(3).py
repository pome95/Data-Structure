#!/usr/bin/env python
# coding: utf-8

# ## 해시 테이블 (Hash Table)

# ### 해시 테이블 충돌 해결 (Chaining)

hash_table=list([0 for i in range(8)]) # list comprehension 사용 => 8칸 테이블 생성

# 키값을 가져오는 함수
def get_key(data):
    return hash(data)

# 해싱 함수 => Division법 %8 사용
def hash_function(key):
    return key % 8
    
def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address]!=0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key,value])
    else:
        hash_table[hash_address] = [[index_key,value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address]!=0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
               return hash_table[hash_address][index][1]
        return None
    else:
        return None

# 중복된 곳에 값을 넣기 위해 임의의 값 출력해서 같은 값이 나오는 두 데이터를 찾아보기                                         
print (hash('Dave') % 8)
print (hash('Dd') % 8)
print (hash('Data') % 8)
                                         
# Result => 0 5 5
# 나누기 결과 5로 같은 결과가 나오는 것을 확인                                         
                                         
save_data('Dd', '1201023010')
save_data('Data', '3301023010')
read_data('Dd')
                            
# Result => '1201023010'
                                         
hash_table
                                         
# Result => [0,0,0,0,0,[[5532289232361108405, '1201023010'], [872982679201566045, '3301023010']],0,0]                                      
