
def switch_grade(grade):
    answer = 0
    if grade == "A+":
        answer = 10
    elif grade == "A0":
        answer = 9
    elif grade == "B+":
        answer = 8
    elif grade == "B0":
        answer = 7
    elif grade == "C+":
        answer = 6
    elif grade == "C0":
        answer = 5
    elif grade == "D+":
        answer = 4
    elif grade == "D0":
        answer = 3
    elif grade == "F":
        answer = 0
    return answer

def count_grade(grades, weights):
    total = 0
    x = 0
    for i in grades:
        temp = switch_grade(i)
        total += temp * weights[x]
        x +=1
    return total

def solution(grades, weights, threshold):
    total = count_grade(grades, weights)
    answer = total - threshold
    return answer

grades = ["A+","D+","F","C0"]
weights = [2,5,10,3]
threshold = 50


solution(grades, weights, threshold)
