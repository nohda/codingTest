# 삭제 관련 list function
clear() : 모든 item 삭제
pop() : index 로 item을 가져오면서 삭제
remove() : value 로 item 삭제
# python function
del : index 로 삭제

1. clear()
my_list = [0,1,2,3,4,5]
my_list.clear()

print(my_list)
# []
 

2. pop()
my_list = ['a', 'b', 'c', 'd', 'e']

one = my_list.pop(2) # index 2 의 값을 빼옴
print(one) # c

print(my_list) # ['a', 'b', 'd', 'e']

# 뒤에서 인덱스
two = my_list.pop(-1) # 뒤부터 index 1 의 값을 빼옴
print(two) # e

print(my_list) # ['a', 'b', 'd']
- index 가 없다면 IndexError: pop index out of range

 

3. remove()
my_list = ['a', 'b', 'c', 'd', 'd', 'e', 'd']

my_list.remove('d')  # 앞에서 부터 찾은 1개만 삭제

print(my_list) 
# ['a', 'b', 'c', 'e', 'd']
- value 가 없다면 ValueError: list.remove(x): x not in list

 

4. del
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

del my_list[0]  # index 0 삭제

# ['b', 'c', 'd', 'e', 'f', 'g']

del my_list[-2]  # 뒤에서 두번째 삭제

# ['b', 'c', 'd', 'e', 'g']

del my_list[2:4]  # 2~3 삭제 (= index 4 이전까지)

# ['b', 'c', 'g']

del my_list[:]  # 모두 삭제

# []
- index 가 없다면 IndexError: list index out of range

 