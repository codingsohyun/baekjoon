import sys
N = int(sys.stdin.readline())   #시간초과 문제 해결

array = []
for i in range(N):
    [age, name] = input().split()
    array.append([age, name])

s_array = sorted(array)

# print(s_array)

for i in range(N):
    print(s_array[i][0], s_array[i][1])