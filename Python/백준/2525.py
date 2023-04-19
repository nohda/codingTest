h,m = map(int,input().split())
t = int(input())

m = m+t

if m >= 60:
    while(m>=60):
        h += 1
        m -= 60
if h >= 24:
    while(h>=24):
        h-=24
print(h,m)
