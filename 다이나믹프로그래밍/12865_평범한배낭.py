import sys

N, K = map(int, input().split()) #아이템의 개수, 배낭의 용량
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))  #아이템 무게, 가치 입력

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] #현재 무게
        value = stuff[i][1]  #현재 가치

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])  #최대 가치