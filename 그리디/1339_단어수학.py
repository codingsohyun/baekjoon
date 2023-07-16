import sys
input = sys.stdin.readline

list_N = []
list_dic = {}

N = int(input())

for i in range(N):
    list_N.append(list(input().rstrip()))
# print(list_N)

for i in range(N):
    for j in range(len(list_N[i])):
        if list_N[i][j] in list_dic:
            list_dic[list_N[i][j]] += 10 ** (len(list_N[i])-j-1)
        else:
            list_dic[list_N[i][j]] = 10 ** (len(list_N[i])-j-1)

list_dic = sorted(list_dic.values(), reverse = True)

sum = 0
m = 9

for value in list_dic:
    sum += value * m
    m -= 1

print(sum)

