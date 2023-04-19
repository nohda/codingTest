#-*- coding: utf-8 -*-
from itertools import permutations
# 모든 경우의 수 조합
def solution(numbers):
    answer = ''
    my_list = list(permutations(numbers, len(numbers)))

    tmp = []
    # print(my_list,type(my_list))
    for i in my_list:
        tmp.append("".join(str(j) for j in i)) #for 문 한줄로 만들기
    print(sorted(tmp,reverse=True)[0])
    
    return sorted(tmp,reverse=True)[0]

#정렬
def solution(numbers):
    numbers = [str(x) for x in numbers] #['3', '30', '34', '5', '9']
    numbers.sort(key=lambda x : (x * 4)[:4],reverse=True) #['9', '5', '34', '3', '30']
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer

numbers=[3,30,34,5,9]

solution(numbers)

'''
    for문 한줄로 만들기
    v = list(range(10))
    print(v)
    [0,1,2,3,4,5,6,7,8,9]


    1. for i in v: print(i)
    2. [i for i in v]

    print("".join(str(i) for i in v))

'''