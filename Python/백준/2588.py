a = int(input())
b = input()

# a= 472
# b="385"
c = b[::-1] #문자열 뒤집기 https://blockdmask.tistory.com/581

for i in c:
    print(a*int(i))
print(a*int(b))
