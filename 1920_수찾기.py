# 시간 초과 에러남

import sys

N = int(sys.stdin.readline())
num1 = list(map(int, sys.stdin.readline().split()))

# print(num1)

M = int(sys.stdin.readline())
num2 = list(map(int, sys.stdin.readline().split()))

for i in num1:
    if i not in num2:
        print('0')
    else:
        print('1')
