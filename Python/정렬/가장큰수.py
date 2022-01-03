numbers = [3, 30, 34, 5, 9]
numbers = list(map(str,numbers))
result = list(map(lambda i: i* 2 , numbers))
print(result)
print(sorted(result))

def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    answer = sorted(numbers,key=lambda x: x*3,reverse = True)
    print(answer)
    return str(int(''.join(answer)))

solution(numbers)

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     print(numbers)
#     return str(int(''.join(numbers)))

# solution(numbers)
