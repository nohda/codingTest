#python 소수점 표현
# aa = 1.2

# print(format(aa, ".2f")) # 1.20

# f = format(aa, '.2f') # 1.20 >> float 형태에서 string 타입으로 변경됩니다.
# https://code-code.tistory.com/10


#python eval 
#eval("1+2") -> 3

t = int(input())

for i in range(t):
    m = input().split()
    n = eval(m[0])
    for j in m[1:]:
        if j == '@' :  n *=3
        elif j == '%': n += 5
        elif j == '#': n -= 7
    # print(format(m[0],".2f"))
    print(f"{n:.2f}")
    
    