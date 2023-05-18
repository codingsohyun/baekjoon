import sys
input = sys.stdin.readline  #시간초과 문제 해결

# N = int(input())
N = input()
N = int(N)

array = []
for i in range(N):
    [x, y] = map(int, input().split())
    array.append([x,y]) #배열에 요소 추가

s_array = sorted(array) #배열 요소 정렬

# print(s_array)

for i in range(N):
    print(s_array[i][0], s_array[i][1])

