import sys
input = sys.stdin.readline

N = int(input())
list_N = list(map(int, input().split()))

M = int(input())
list_M = list(map(int, input().split()))

# print(list_N, list_M)

dic = dict()

for i in list_N:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# print(dic)

for i in range(M):
    if list_M[i] in dic:
        print(dic[list_M[i]], end=' ')
    else :
        print(0, end=' ')