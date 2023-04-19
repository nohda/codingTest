#input()
T = int(input())
##1차원 배열
my_list = list(map(int,input().split()))
##2차원 배얄
n,m = map(int,input().split())
my_list = [list(map(str,input().split())) for _ in range(n)]
print(my_list)

def main():
    print("main")

if __name__ == "__main__":
    main()

# # import sys

# # data = []
# # n = int(sys.stdin.readline())
# # for i in range(n):
# #     data.append(list(map(int,sys.stdin.readline().split())))

