import sys

data = []
result = []

#input
# n = int(sys.stdin.readline())
# for i in range(n):
#     data.append(list(map(int,sys.stdin.readline().split())))

search_ = []
n = 2
data = [[3,1,2],[4,3,1],[1,2,4],[2,5,6]]

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [i, x.index(v)]

def cal_position(x,y,val):
    # print(x,y,val)
    if (x-1) >= 0 and result[x-1][y] == 0: 
        print("위쪽") 
        result[x-1][y] = val
    elif (y-1) >= 0 and result[x][y-1] == 0: 
        print("왼쪽")
        result[x][y-1] = val
    elif (y+1) < n and result[x][y+1] == 0: 
        print("오른쪽")
        result[x][y+1] = val
    elif (x+1) < n  and result[x+1][y] == 0: 
        print("아래쪽")
        result[x+1][y] = val
    else: print("error")

def cal_position_(x,y):
    # print(x,y,val)
    if (x-1) >= 0 and result[x-1][y] == 0:  
        return [x-1,y]
    elif (y-1) >= 0 and result[x][y-1] == 0: 
        return [x,y-1]
    elif (y+1) < n and result[x][y+1] == 0: 
        return [x,y+1]
    elif (x+1) < n  and result[x+1][y] == 0: 
        return [x+1,y]
    else: return [0,0]

def min_position(val):
    for i in range(n):
        for j in range(n):
            if result[i][j] == 0: 
                result[i][j] = val
                return

#result 값 초기화
for i in range(n):
    result.append([]) # 새로운 내부 배열 선언
    for j in range(n):
        result[i].append(0) # 해당 내부 배열에 0이라는 값 추가

# result = [[0s,0,0],[0,0,0],[0,0,0]]

#solution
for d in range(len(data)):
    favorit = []
    answer = []
    print("data[i] ",data[d])
    if d == 0:
        if n%2 == 1: result[n//2][n//2] = data[0][0]
        else: result[(n//2)-1][(n//2)-1] = data[0][0]
    else:
        count = 0
        for id in data[d][1:]:
            print("id : ",id)
            if index_2d(result,id): 
                count +=1
                favorit.append([data[d][0],index_2d(result,id)])
                # cal_position(a[0],a[1],id)
        print("favorit",favorit)
        if count == 0:
            # print("행이 작은것을 찾는다.")
            min_position(data[d][0])
        elif count == 1:
            # print("count 0")
            cal_position(favorit[0][1][0],favorit[0][1][1],favorit[0][0]) 
        else:
            print("count more ",count)
            for cal in range(count):
                answer.append(cal_position_())
            # break
        count = 0
        # break
    for j in result:
        print(j)
    print("\n")
            
        
            
#print

# print("\n")

