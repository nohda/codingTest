h,m,s = map(int,input().split())
t = int(input())
print((h+((m+(s+t)//60)//60))%24,(m+(s+t)//60)%60,(s+t)%60)