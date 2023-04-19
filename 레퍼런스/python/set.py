set은 집합으로 만들어주는 내적함수이다.(중복된 요소를 합쳐준다)
a = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7]
print(set(a))


{1, 2, 3, 4, 5, 6, 7}
1. 교집합
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])

print(set1 & set2)
print(set1.intersection(set2))


{3, 4, 5, 6}
{3, 4, 5, 6}
2. 합집합

set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])


print(set1 | set2)
print(set1.union(set2))


{1, 2, 3, 4, 5, 6, 8, 9}
{1, 2, 3, 4, 5, 6, 8, 9}
3. 차집합

set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])


print(set1 - set2)
print(set1.difference(set2))


{1, 2}
{1, 2}
4. 대칭 차집합( 교집합을 제외한 나머지의 합)
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])

print(set1 ^ set2)


{1, 2, 8, 9}
5. 집합 추가와 제거

set1 = set([1,2,3,4,5,6])
set1.update([7,8,9])         # update
print(set1)

set1.remove(9)               # remove
print(set1)

{1, 2, 3, 4, 5, 6, 7, 8, 9} {1, 2, 3, 4, 5, 6, 7, 8}
리스트에서 같은 값 찾기

A = [1, 3, 5, 7, 9]
B = [10, 5, 1, 2, 4]

C = set(A) & set(B)
D = [i for i in A if i in B]

print(C)
print(D)


print(C) ==>{1, 5} 
print(D) ==> [1, 5] 
리스트에서 다른 값 찾기
A = [1, 2, 7, 4, 5]
B = [1, 3, 8, 7, 9]

C = list(set(A) - set(B))
D = list(set(B) - set(A))


C ==> [2, 4, 5]
D ==> [8, 9, 3]
리스트값 비교
list1 = [[1, 3], [5, 7]]
list2 = [[1, 3], [5, 7]]
print(list1 == list2)

True



list3 = [[1, 3], [5, 7]]
list4 = [[1, 3], [5, 8]]
print(list3 == list4)

False
두 리스트 성분 비교
1. sorted()를 사용해서 정렬한 후 비교
크기순으로 정렬한 list의 길이가 같고 요소들이 같을 경우 True를, 그렇지 않은 경우 False를 반환

list1 = [1, 2, 3, 4, 5]
list2 = [2, 1, 4, 5, 3]
print(sorted(list1) == sorted(list2))


True
2. set()를 사용해서 정렬한 후 비교 [by, ==]
list1 = [1, 2, 3, 4, 2, 5, 1]
list2 = [2, 4, 1, 5, 3]
list3 = [1, 3, 2, 4, 1]

print(set(list1))
print(set(list2))
print(set(list3))
print(set(list1) == set(list2))
print(set(list1) == set(list3))


{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}
{1, 2, 3, 4}
True
False
3. np.array_equal() 사용하기
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])
print(np.array_equal(arr1, arr2))


True


arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[1, 2], [5, 4]])
print(np.array_equal(arr3, arr4))


False
4.np.equal() 사용하기
각각의 요소를 비교

import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 2, 1])

print(np.equal(a, b))


[False True False]
import numpy as np

a = np.array([0, 1, 3])
b = np.arange(3) # [0, 1, 2]

print(np.equal(a, b))
print(a == b)

[True True False]
[True True False]