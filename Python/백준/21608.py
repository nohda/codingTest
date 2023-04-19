n = int(input())
n,m = map(int,input().split())

my_list = [list(map(int,input().split())) for _ in range(n)]
print(my_list)

print(f"#{test_case} {count}")
print("#{} {}".format(n,m))