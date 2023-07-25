import sys
input = sys.stdin.readline

n = int(input())

weights = []
sum = []
for i in range(n):
    weights.append(int(input()))

weights.sort(reverse=True)

for i in range(n):
    sum.append(weights[i]*(i+1))

print(max(sum))
