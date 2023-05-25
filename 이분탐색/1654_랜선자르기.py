import sys
input = sys.stdin.readline

K, N = map(int, input().split())

array = []
for i in range(K):
    array.append(int(input()))
# print(array)

start, end = 1, max(array)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(K):
        cnt += array[i] // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)


