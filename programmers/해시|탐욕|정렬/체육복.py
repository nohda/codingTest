#-*- coding: utf-8 -*-

#방법 1
def solution(n, lost, reserve):
    u = [1] * (n+2)
    for i in reserve:
        u[i] +=1
    for i in lost:
        u[i] -=1
    for i in range(1,n+1):
        if u[i-1] == 0 and u[i] == 2:
            u[i-1:i+1] = [1,1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1,1]

    return len([x for x in u[1:-1] if x>0])

# def solution(n, lost, reserve):
def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost)-s
    r = set(reserve) - s
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    return n -len(l)

print(solution(5,[2, 4],[1, 3, 5]))    
'''
    입출력 예
    n	lost	reserve	return
    5	[2, 4]	[1, 3, 5]	5
    5	[2, 4]	[3]	4
    3	[3]	[1]	2
'''    