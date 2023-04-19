#-*- coding: utf-8 -*-

#내가 푼 코드 -> 정렬: O(N log N)
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            participant.pop(i)
            pass
    if answer == '': answer = participant[-1] 
    # print(answer)
    return answer

#강사가 푼 코드 -> 해시: O(1)
def solution(participant, completion):
    answer = ''
    d = {}
    for x in participant:
        d[x] = d.get(x,0) + 1
    print(d)
    for x in completion:
        d[x] -=1
    print(d)
    dnf = [k for k,v in d.items() if v > 0]
    answer = dnf[0]
    
    print(answer)
    return answer

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

participant = ["mislav", "stanko", "mislav","ana"]
completion = ["stanko","ana", "mislav"]

solution(participant, completion)