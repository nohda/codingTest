def solution(a, b):
    if a == b:
        answer = a

    else:
        answer = 0
        if a > b:
            a, b = b, a

        while a <= b:
            answer = answer + a
            a = a + 1

    return answer


print(solution(3, 5))
