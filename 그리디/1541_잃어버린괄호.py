import sys
input = sys.stdin.readline

total = 0
num = []
exp = input().split('-')
# print(exp)
for i in exp:
    math = i.split('+')
    # print(math)
    for j in math:
        # print(j)
        total += int(j)
    num.append(total)
n = num[0]

for i in range(1, len(num)):
    n -= num[i]
print(n)




