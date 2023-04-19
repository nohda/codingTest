#-*- coding: utf-8 -*-
from itertools import combinations

def solution(number,k):
    my_list = list(combinations(list(number), len(number)-k))
    tmp = []
    for i in my_list:
        tmp.append("".join(str(j) for j in i)) #for 문 한줄로 만들기
    
    print(sorted(tmp,reverse=True)[0])

    return sorted(tmp,reverse=True)[0]

# def solution(number,k):
#     print(number,k)

'''
    number	k	return
    "1924"	2	"94"
    "1231234"	3	"3234"
    "4177252841"	4	"775841"

'''
number = "4177252841"
k = 4
solution(number,k)



'''
    for문 한줄로 만들기
    v = list(range(10))
    print(v)
    [0,1,2,3,4,5,6,7,8,9]


    1. for i in v: print(i)
    2. [i for i in v]

    print("".join(str(i) for i in v))

'''