#!/usr/bin/env python
# coding: utf-8

# ## 배열 기본 연습

# ### 파이썬 리스트 활용


# 1차원 배열: 리스트로 구현시
data = [1,2,3,4,5]
print(data)

# => [1,2,3,4,5]



# 2차원 배열: 리스트로 구현시
data = [[1,2,3],[4,5,6],[7,8,9]]
print(data)

# => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(data[0])

# => [1,2,3]


print(data[0][0])
print(data[0][1])
print(data[0][2])
print(data[1][0])
print(data[1][1])
print(data[1][2])
print(data[2][0])
print(data[2][1])
print(data[2][2])

# => 1 2 3 4 5 6 7 8 9




# #4X4 배열 만들고 출력하기 (반복문)
data = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j]

# => 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
              
# ## i는 len(data)만큼 -> data의 길이만큼(4)
# ## j는 len(data[i])만큼 -> 반복된 i안의 요소 길이 만큼 (4) -> 4x4 행렬
              
              
              

dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']
m_count=0
for data in dataset:
    for index in range(len(data)):
        if data[index]=='i':
            m_count +=1
print(m_count)

# => 44



country = 'US'
print(country)

# => US

country = country + 'A'
print(country)

# => USA




