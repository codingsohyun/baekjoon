import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
list = [0]

for i in A :
    if list[-1] < i:
        list.append(i)
    else:
        left = 0
        right = len(list)

        while left < right:
            mid = (left + right) // 2
            if list[mid] < i:
                left = mid + 1
            else:
                right = mid
        list[right] = i

print(len(list)-1)