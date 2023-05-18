import sys
input = sys.stdin.readline  #시간초과 문제 해결

# N = int(input())
N = input()
N = int(N)

array = []
for i in range(N):
    [x, y] = map(int, input().split())
    array.append([y,x]) #배열에 요소 추가

# print(array)

# s_array = sorted(array, key = lambda x : x[0]) #배열 요소 정렬
s_array = sorted(array)

# print(s_array)

for i in range(N):
    print(s_array[i][1], s_array[i][0])

