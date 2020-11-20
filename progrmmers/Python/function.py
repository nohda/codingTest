#-*- encoding: utf-8 -*-

# lambda 인수1, 인수2, ... : 인수를 이용한 표현식
sum = lambda a,b: a+b
print(sum(3,4))

#map(f, iterable)
li = [1, 2, 3]
result = list(map(lambda i: i ** 2 , li))
print(result)

#reduce
from functools import reduce
a = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print(a)


a = []
for x in range(0,5):
    a.append(x)
print(a)

# comprehension
a = [x for x in range(0,5)]
print(a)
