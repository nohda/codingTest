#최소공배수 구하기
from fractions import gcd

def solution(arr):
    while len(arr) > 1:
        n, m = arr.pop(), arr.pop()
        arr.append(n*m // gcd(n, m))
    return arr.pop()

#최대공약수 구하기
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def solution(n, m):
    return [gcd(a, b), n*m // gcd(a, b)]
