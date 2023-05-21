import sys

N = int(sys.stdin.readline().rstrip())

array = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    array.append([x,y])

s_array = sorted(array)

for i in range(N):
    print(s_array[i][0], s_array[i][1])

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
#
# array = []
# for _ in range(N) :
#     array.append(list(map(int, input().split())))
#
# array.sort(key = lambda x: (x[0],x[1]))
#
# for i in range(N):
#     print(array[i][0], array[i][1])
#
# arr = sorted(arr, key= lambda y: y[1])
# arr = sorted(arr, key= lambda x: x[0])
#
# for x in arr:
#     print(*x)
#
# arr.sort(key=lambda a : (a[0], a[1]))
#
# for i in range(0, N):
#     print(*arr[i])