def solution(n,a,b):
    answer = 3
    answer = process(n,a,b)
    print(answer)
    return answer

def process(n,a,b):
    answer = 0
    for i in range(n):

        if a%2 == 1:
            re_a = (a + 1 )/2
        else:
            re_a = a/2

        if b%2 == 1:
            re_b = (b + 1 )/2
        else:
            re_b = b/2

        print("TEST :",re_a,re_b)

    return answer

solution(8,4,7)
