import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree_list = [int(N) for N in input().split()]

start = 0
end = max(tree_list)

result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in tree_list:
        if x>mid:
            total += x-mid
    if total < M:
        end = mid-1
    else:
        result = mid
        start = mid + 1

print(result)

