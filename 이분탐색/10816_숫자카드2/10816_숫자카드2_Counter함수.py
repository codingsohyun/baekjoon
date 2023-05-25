from collections import Counter

import sys
input = sys.stdin.readline

N = int(input())
list_N = list(map(int, input().split()))

M = int(input())
list_M = list(map(int, input().split()))

# print(list_N, list_M)

count = Counter(list_N)
for x in list_M:
    if x in count:
        print(count[x], end=' ')
    else:
        print(0, end=' ')

