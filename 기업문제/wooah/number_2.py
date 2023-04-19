grades = ["A+","D+","F","C0"]
s = "1234"
op = "+"
# print(grades[:3])
# print(grades[3:])

def process(s,op):
    list_s = list(s)
    temp = []
    j = 1
    while j < len(list_s):
        left = list_s[:j]
        left_total = process_number(left)
        right = list_s[j:]
        right_total = process_number(right)
        answer = process_answer(left_total,op,right_total)
        temp.append(answer)
        j +=1
    return temp

def process_number(list_number):
    answer = 0
    for i in range(len(list_number)):
        answer = (answer * 10) + int(list_number[i])
    return answer

def process_answer(left_total,op,right_total):
    answer = 0
    if op == "+":
        answer = left_total + right_total
    elif op == "-":
        answer = left_total - right_total
    elif op == "*":
        answer = left_total * right_total
    elif op == "/":
        answer = left_total / right_total
    return answer

def solution(s, op):
    answer = []
    answer = process(s,op)
    return answer

print(solution(s,op))
