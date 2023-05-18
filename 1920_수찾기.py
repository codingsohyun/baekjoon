# num1을 list로 하면 시간 초과 에러남

import sys

N = int(sys.stdin.readline())
num1 = set(map(int, sys.stdin.readline().split()))  #탐색 시간을 줄이기 위해 set으로 받음

# print(num1)

M = int(sys.stdin.readline())
num2 = list(map(int, sys.stdin.readline().split()))

for i in num2:
    if i not in num1:
        print('0')
    else:
        print('1')

