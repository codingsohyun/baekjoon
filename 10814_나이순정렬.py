import sys
input = sys.stdin.readline  #시간초과 문제 해결

# N = int(input())
N = input()
N = int(N)

array = []
for i in range(N):
    [age, name] = input().split()
    array.append([int(age), i, name])

# print(array)

s_array = sorted(array)

# print(s_array)

for i in range(N):
    print(s_array[i][0], s_array[i][2])