t = int(input())
for i in range(t):
    a,s = input().split()
    for j in s:
        print((lambda a,x: a*x)(int(a),j),end='')
    print()