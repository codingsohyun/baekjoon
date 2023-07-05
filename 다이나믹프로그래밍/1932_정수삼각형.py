import sys
input = sys.stdin.readline

N = int(input())

arr=[]
for i in range(N):
    arr.append(list(map(int, input().split())))

# print(arr)

for i in range(1, N):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i - 1][j]
        elif j == len(arr[i]) - 1:
            arr[i][j] = arr[i][j] + arr[i - 1][j - 1]
        else:
            arr[i][j] = max(arr[i - 1][j - 1], arr[i - 1][j]) + arr[i][j]
print(max(arr[N - 1]))

