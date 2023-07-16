import sys
input = sys.stdin.readline

package =[]
single = []

N,M = map(int, input().split())

for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)

min_package = min(package)

price = 0
while N > 0:
    if N >= 6:
        min_single = min(single)*6
        N -= 6
    else:
        min_single = min(single)*N
        N -= N

    if min_single < min_package:
        price += min_single
    else:
        price += min_package

print(price)
