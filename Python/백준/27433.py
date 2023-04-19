N = int(input())

if N == 0: 
    print(1)
else:    
    ans = 1
    for i in range(1,N+1):
        ans *=i
    print(ans)


# N = int(input())

# if N == 0 :
#     print(1)
# else :
#     result = 1
#     for i in range(2, N+1) :
#         result *= i
#     print(result)