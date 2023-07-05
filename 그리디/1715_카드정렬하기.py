# import sys
# input = sys.stdin.readline
#
# arr = []
# N = int(input())
#
# for i in range(N) :
#     arr.append(int(input()))
#
# arr.sort()
#
# sum = 0
# for i in range(N-1):
#         sum += arr[i] + arr[i+1]
#         arr[i+1] = sum
#
# print(sum)

import sys
import heapq
input = sys.stdin.readline

arr = []
N = int(input())
for _ in range(N):
    heapq.heappush(arr, int(input()))

sum = 0
if len(arr) == 1:
    print(sum)
else:
    while len(arr) > 1:
        num1 = heapq.heappop(arr)
        num2 = heapq.heappop(arr)
        sum += num1 + num2
        heapq.heappush(arr, num1 + num2)
    print(sum)
