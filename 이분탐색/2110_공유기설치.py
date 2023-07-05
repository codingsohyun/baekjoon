import sys
input = sys.stdin.readline

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= C:
            global ans
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

len_arr = []
N, C = map(int, input().split())

for i in range(N):
    length = int(input())
    len_arr.append(length)

len_sort = sorted(len_arr)

start = 1
end = len_sort[-1] - len_sort[0]
ans = 0

binary_search(len_sort, start, end)
print(ans)

# print(len_sort)

