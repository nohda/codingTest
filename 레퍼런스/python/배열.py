#2차원 배열 선언
rows = 3
cols = 4

arr = [[0 for j in range(cols)] for i in range(rows)]

print(arr) #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

rows = 3
cols = 4

arr = [[(i + 1)*(j + 1) for j in range(cols)] for i in range(rows)]

print(arr) #[[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]

#https://codechacha.com/ko/python-2dimentional-array/