import sys
 
N = int(sys.stdin.readline())
stack = []

for i in range(N):
    input_order = sys.stdin.readline().split()
    order = input_order[0]
    print(order)
