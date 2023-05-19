#이분탐색으로 풀어보기
import sys

def binary_search(array, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

N = int(sys.stdin.readline())
num1 = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

M = int(sys.stdin.readline())
num2 = list(map(int, sys.stdin.readline().rstrip().split()))

for i in num2:
    print(binary_search(num1, i, 0, N-1))

# for i in num2:
#     if binary_search(num1, i, 0, N-1):
#         print(1)
#     else:
#         print(0)

N = int(input())
array = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in check:
    result = binary_search(sorted(array), i, 0, N - 1)
    if result != None:
        print(1)
    else:
        print(0)