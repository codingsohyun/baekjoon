import sys

input = sys.stdin.readline

n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fibonacci(n):
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 1
