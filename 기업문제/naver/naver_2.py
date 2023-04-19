def solution(n,p,c):
    answer = ''
    d = [100,50,25]
    da = 0
    i = 0
    total = 0.00
    remain = 0
    last_toal = 0.00
    day_count = 0
    total_ave = 0.00

    while i < n:
        p[i] = p[i] + remain
        if p[i] >= c[i]:
            total = d[da] * c[i]
            remain = p[i] - c[i]
            da = 0
            last_toal = last_toal + total
            day_count += 1
            total_ave = last_toal/day_count

        else:
            remain = p[i]
            day_count += 1
            total_ave = last_toal/day_count
            if da < 2:
                da += 1
            else:
                break;
        i += 1
        # a=float(total_ave)
    return total_ave

n = 7
p = [6,2,1,0,2,4,3]
c = [3,6,6,2,3,7,6]


a=solution(n,p,c)
print(a)
# print('%.2f' % a)
