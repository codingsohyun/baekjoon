import sys
input = sys.stdin.readline

N = int(input())

array = []
for i in range(N):
    array.append(int(input()))

s_array = sorted(array)

for i in range(N):
    print(s_array[i])
