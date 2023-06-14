import sys
input = sys.stdin.readline

T = int(input())    #테스트 케이스 수
for i in range(T):
    N = int(input())  # 지원자의 숫자
    ppl_list = [0]*N
    for j in range(N):
        S, M = map(int, input().split())
        ppl_list[j] = [S, M]

    ppl_sort = sorted(ppl_list, key = lambda x : x[0])
    hired = 1
    man = ppl_sort[0][1]
    for j in range(1,N) :
        if ppl_sort[j][1] < man :
            man = ppl_sort[j][1]
            hired += 1

    print(hired)





