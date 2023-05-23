import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
# print(tree)

def bs(arr, tar, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return bs(arr, tar, start, mid-1)
    else:
        return bs(arr, tar, mid+1, end)

