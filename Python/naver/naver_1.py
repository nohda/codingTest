def solution(n,p,c):
    answer = ''
    d = [100,50,25]
    da = 0
    i = 0
    total = 0
    remain = 0
    last_toal = 0
    day_count = 0
    total_ave = 0

    while i < n:
        p[i] = p[i] + remain
        if p[i] >= c[i]:
            total = d[da] * c[i]
            remain = p[i] - c[i]
            da = 0
            print("1 : ", total)
            last_toal = last_toal + total
            print("total : ", last_toal)
            day_count += 1
            print("da : ",da)
            print("day_count : ", day_count)
            total_ave = last_toal/day_count
            print("avera : ", total_ave)

        else:
            remain = p[i]
            day_count += 1
            print("day_count1 : ", day_count)
            total_ave = last_toal/day_count
            print("avera : ", total_ave)
            if da < 2:
                da += 1
                print("da : ",da)
            else:
                print("no")
                break;
        i += 1

    print(total_ave)
    return total_ave

# n = 6
# p = [5,4,7,2,0,6]
# c = [4,6,4,9,2,3]

n = 7
p = [6,2,1,0,2,4,3]
c = [3,6,6,2,3,7,6]
solution(n,p,c)
