#-*- encoding: utf-8 -*-
T = int(input())

#오른쪽 아래쪽 왼쪽 위쪽
def direction(dir):
    if dir == "r": dir = "d"
    elif dir=="d": dir = "l"
    elif dir =="l": dir = "u"
    elif dir == "u": dir = "r"
    return dir

def adj_dir(dir,x,y):
    if dir == "r": 
        y +=1
    elif dir == "d": 
        x +=1
    elif dir == "l": 
        y-=1
    elif dir == "u": 
        x-=1
    return x,y
def printarr(arr,n):
    #출력
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ") #print 끝에 end 붙이면 개행 없이 출력, ""안에 넣으면 됨
        print("")

for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0 for j in range(n)] for i in range(n)] #배열선언
    dir = "r"
    x = 0
    y = 0
    for i in range(n*n):
        # print("value 1 : ",i+1," ",dir," ",x," ",y," arr[x][y] : ",arr[x][y])
        if (dir == "r" and y+1 == n) and arr[x][y] == 0:
            dir = direction(dir)
        elif (dir == "l" and x-1 == 0)and arr[x][y] == 0: 
            dir = direction(dir)
        elif (dir == "u" and y-1 == 0) and arr[x][y] == 0:
            dir = direction(dir)
        elif (dir == "d" and x+1 == n )and arr[x][y] == 0:
            dir = direction(dir)
        if arr[x][y] !=0:
            dir = direction(dir)
            if x < 0:
                x=0
            elif y < 0:
                y=0
            x,y = adj_dir(dir,x,y)
            arr[x][y] = i+1

        elif arr[x][y] == 0:
            arr[x][y] = i+1
            x,y = adj_dir(dir,x,y)

    printarr(arr,n)
    print("#{} {}".format(test_case,n))
    

# arr = [[0 for j in range(n)] for i in range(n)]
# print(arr)