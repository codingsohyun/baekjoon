import sys
input = sys.stdin.readline

N, K = map(int, input().split())

price=[]
for i in range(N):
    price.append(int(input()))

price_s = sorted(price, reverse=True)

count=0
for s in price_s:
    while K > 0:
        if s <= K:
            K -= s
            count += 1
        else: break

print(count)

