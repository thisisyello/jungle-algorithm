'''
문제 설명
정수 N이 주어졌을 때, N!을 출력하세요.
팩토리얼은 다음과 같이 계산합니다.
N! = N x (N - 1) x (N - 2) x ... x 2 x 1
예를 들어:
5! = 5 x 4 x 3 x 2 x 1 = 120
또한 0!은 1입니다.

입력
첫째 줄에 0보다 크거나 같은 정수 N이 주어집니다.
예시:
10

출력
N!을 출력합니다.
예시:
3628800
'''

import sys
input = sys.stdin.readline

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(input())

print(factorial(n))