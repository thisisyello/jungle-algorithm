'''
문제 설명
2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 내용을 골드바흐의 추측이라고 합니다.
주어진 짝수 n을 두 소수의 합으로 나타내세요.
가능한 조합이 여러 개라면, 두 소수의 차이가 가장 작은 조합을 출력해야 합니다.
작은 소수를 먼저 출력합니다.
예를 들어 10은 다음과 같이 나타낼 수 있습니다.
3 + 7
5 + 5
두 소수의 차이가 더 작은 조합은 5 + 5입니다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어집니다.
그다음 T개의 줄에 짝수 n이 하나씩 주어집니다.
n은 4 이상 10,000 이하입니다.
예시:
3
8
10
16

출력
각 테스트 케이스마다 조건을 만족하는 두 소수를 공백으로 구분해 출력합니다.
작은 소수를 먼저 출력합니다.
예시:
3 5
5 5
5 11
'''

import sys
input = sys.stdin.readline

t = int(input())
# ----- 에라토스테네스의 체
is_prime = [True] * 10001
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(10000 ** 0.5) + 1): # 제곱근까지만 해도 충분하기에
    if is_prime[i]:
        for j in range(i * i, 10001, i):
            is_prime[j] = False
# 에라토스테네스의 체 -----

for _ in range(t):
    num = int(input())

    a, b = num // 2, num // 2

    while not (is_prime[a] and is_prime[b]):
        a -= 1
        b += 1

    print(a, b)
    

