from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    print(cnt)
    print(cnt.values())
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    print(answer)

    c = []
    for name, kind in clothes:
        print(name,kind)
        c.append([name,kind])
    print(c)

    a =[]
    a = [kind for name,kind in clothes]
    print(Counter(a))

    print(reduce(lambda x, y: x*(y+1),[1,2],1))
clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
solution(clothes)

# print(collections.Counter(clothes))
# b = list(zip(*a))[0]
# print(list(zip(*clothes))[1])
#
# b = [i[1] for i in clothes]
# print(b)
