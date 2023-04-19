# a = int(input())

# i = 1
# while(a>1):
#     print(a,i)
#     a-=i
#     i+=1
# print(i-2)

s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)