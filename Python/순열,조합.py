#-*- encoding: utf-8 -*-
import itertools

chars = ['A', 'B', 'C']

# permutation
# 순열이란 몇 개를 골라 순서를 고려해 나열한 경우의 수를 말한다. 즉, 서로 다른 n 개 중 r 개를 골라 순서를 정해 나열하는 가짓수이며 순열이라는 의미의 영어 ‘Permutation’의 첫 글자 P를 따서 nPr로 표시한다.

p = itertools.permutations(chars, 2)
print(list(p))

# combination
# 조합이란 서로 다른 n개 중에서 r개(n≥r) 취하여 조를 만들 때, 이 하나하나의 조를 n개 중에서 r개 취한 조합이라고 한다

c = itertools.combinations(chars, 2)
print(list(c))

import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
