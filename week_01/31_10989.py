'''
문제 설명
N개의 수가 주어집니다.
이 수들을 오름차순으로 정렬한 뒤 한 줄에 하나씩 출력하세요.

입력
첫째 줄에 수의 개수 N이 주어집니다.
둘째 줄부터 N개의 줄에 정수가 하나씩 주어집니다.
예시:
10
5
2
3
1
4
2
3
5
1
7

제한
N ≤ 10,000,000
입력값 ≤ 10,000

출력
입력으로 주어진 수를 오름차순으로 정렬해서 한 줄에 하나씩 출력합니다.
예시:
1
1
2
2
3
3
4
5
5
7
'''

import sys
input = sys.stdin.readline

n = int(input())
count= [0] * 10001
numbers = []

for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):
    for _ in range(count[i]):
        print(i)