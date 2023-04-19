#!/usr/bin/python

def solution(n, lost, reserve):
    answer = 0
    safe = []
    #exception 
    if lost != (set(lost) & set(reserve)): 
        tmp = list(set(lost) & set(reserve))
        for i in tmp: reserve.remove(i)

    for i in range(1,n+1):
        if (i not in lost) and (i not in reserve): 
            answer+=1
        elif i in lost:
            for j in reserve:
                if j+1 == i or j-1 == i: 
                    answer+=1
                    reserve.pop(0)
        elif i in reserve:
            answer+=1
        if len(lost) < len(reserve) and i == n: answer+=1
    return answer

n = 5
lost = [5]
reserve = [1]

print("answer is : ",solution(n,lost,reserve))