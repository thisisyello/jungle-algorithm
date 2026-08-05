'''
문제 설명
주어진 수 N개 중에서 소수의 개수를 구하세요.
소수는 1보다 큰 자연수 중에서, 1과 자기 자신으로만 나누어떨어지는 수입니다.
예를 들어:
1 3 5 7
1은 소수가 아닙니다.
3, 5, 7은 소수입니다.
따라서 소수의 개수는 3개입니다.

입력
첫째 줄에 수의 개수 N이 주어집니다.
둘째 줄에 N개의 자연수가 공백으로 구분되어 주어집니다.
예시:
4
1 3 5 7

출력
주어진 수들 중 소수의 개수를 출력합니다.
예시:
3
'''

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        count += 1

print(count)