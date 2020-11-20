def solution(logs):
    answer = []
    return answer
logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]

def process(logs):
    exam = []
    list_a = [1,2,2,2]
    list_b = []

    for i in range(len(logs)):
        exam_log = logs[i].split( )
        print(exam_log)

        # for j in list_a:
        #     line = []
        #     for x in range(j):
        #         line.append(exam_log)
        #     list_b.append(line)
        # print(list_b)

# process(logs)


def solution(n, board):
    answer = 0
    k = 1
    count = 0
    for x in range(n*n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == k:
                    count += i+j+1
                    print("key",board[i][j],k,count)
                    k+=1
    return answer

board = [[3, 5, 6], [9, 2, 7], [4, 1, 8]]
n = 3
solution(n, board)
