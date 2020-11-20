# import statistics
import numpy as np

def solution(citations):
    answer = 0
    print(sorted(citations),int(np.median(citations)))
    # a = statistics.median(citations)
    # print(a)
    return answer

citations = [3, 0, 6, 2, 1, 5]
solution(citations)

[12, 11, 10, 9, 8, 1] 5
[6, 6, 6, 6, 6, 1] 5
[4, 4, 4] 3
[4, 4, 4, 5, 0, 1, 2, 3] 4
[10, 11, 12, 13] 4
[3, 0, 6, 1, 5] 3
[0, 0, 1, 1] 1
[0, 1] 1
[10, 9, 4, 1, 1] 3
