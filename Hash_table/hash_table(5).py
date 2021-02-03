
#import hashlib
#
#data='test'.encode() # 문자열 encode() -> byte 형태 
#hash_object = hashlib.sha1() # test 값의 SHA1 함수를 사용하여 변환
#hash_object.update(b'test')
#hex_dig = hash_object.hexdigest() # 16진수 함수 .hexdigest()
#print(hex_dig)

#import hashlib

#data='test'.encode() # 문자열 encode() -> byte 형태
#hash_object = hashlib.sha256() # test 값의 SHA256 함수를 사용하여 변환
#hash_object.update(b'test')
#hex_dig = hash_object.hexdigest() # 16진수 함수 .hexdigest()
#print(hex_dig)


import hashlib
hash_table = list([0 for i in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig,16)

def hash_function(key):
    return key % 8

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


print(get_key('db')%8)
print(get_key('da')%8)
print(get_key('dh')%8)


save_data('db','01011112222')
save_data('da','01022223333')
save_data('dh','01033334444')


hash_table


# #### 시간복잡도
# * 일반적인 경우 (Collision X) O(1)
# * 최악의 경우 (Collision O (모두 발생하는 경우)) O(n)
# > 해시 테이블의 경우, 일반적인 경우를 기대하고 만듬 -> O(1)
# 
# #### 검색에서 해시 테이블
# * 16개의 배열에 데이터를 저장, 검색할 때 O(n)
# * 16개의 데이터 공간에 해시 테이블을 저장, 검색할 때 O(1)