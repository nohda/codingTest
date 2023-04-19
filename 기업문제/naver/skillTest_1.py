def solution(n):
    answer = 0
    lis = list(str(n))
    for i in range(len(lis)):
        answer += int(lis[i])
    return answer

# n = 123
# print(solution(n))


def process(s,n):
    answer = ''
    up = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
    down = ['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    for i in range(len(s)):
        print(i,s[i])
        if s[i] == " ":
            answer += " "
        else:
            if s[i].isupper == True:
                text_num = up.index(s[i])
                answer += up[text_num + n]
            elif s[i].isupper == False:
                text_num = down.index(s[i])
                answer += down[text_num + n]
    print(answer)


s = 'ab'
n =	1
# process(s,n)


def solution(n):
    answer = ''
    text_n = list(str(n))
    text_n.sort(reverse=True)

    for i in range(len(text_n)):
        answer += text_n[i]

    return int(answer)

n = 118372
# solution(n)

from itertools import combinations

numbers = [2,1,3,4,1]
# numbers = list(map(str,numbers))
numbers.sort()
# print(numbers)
com = combinations(numbers,2)
# print(list(com))

# for i in range(len(numbers)):
#     # print(list(map(''.join, combinations(numbers, i))))
#     print(i,numbers[i],combinations(numbers,2))
#

def solution(numbers):
    answer = []
    return answer
