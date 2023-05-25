import sys

input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if array[mid] == target:
        return dic.get(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

N = int(input())
list_N = sorted(list(map(int, input().split())))

M = int(input())
list_M = list(map(int, input().split()))

dic = {}
#dic = dict()

for x in list_N:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

for i in list_M:
    print(binary_search(list_N, i, 0, len(list_N)-1), end=' ')