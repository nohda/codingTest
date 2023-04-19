#-*- coding: utf-8 -*-

#lambda 매개변수 : 표현식

def hap(x, y):
  return x + y
  
hap(10, 20) #30

(lambda x,y: x + y)(10, 20) #30

print("lambda : ",(lambda A: (A * 4)[:4])('9'))

#map(함수, 리스트)
map(lambda x: x ** 2, range(5))             # 파이썬 2
#[0, 1, 4, 9, 16]  
print("map : ",list(map(lambda x: x ** 2, range(5))))    # 파이썬 2 및 파이썬 3
#[0, 1, 4, 9, 16]


#reduce(함수, 시퀀스)
from functools import reduce   # 파이썬 3에서는 써주셔야 해요  
print("reduce :", reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]) )
#10
print("reduce :",reduce(lambda x, y: y + x, 'abcde'))
#'edcba'

#filter(함수, 리스트)

print("filter : ",list(filter(lambda x: x < 5, range(10)))) # 파이썬 2 및 파이썬 3
#[0, 1, 2, 3, 4]
