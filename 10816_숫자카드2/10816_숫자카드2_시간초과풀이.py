import sys
input = sys.stdin.readline

N = int(input())
list_N = list(map(int, input().split()))

M = int(input())
list_M = list(map(int, input().split()))

# print(list_N, list_M)

array = []
total = 0
for x in list_M:
    if x in list_N:
        total = list_N.count(x)
        array.append(total)
    else:
        array.append(0)


print(*array)
