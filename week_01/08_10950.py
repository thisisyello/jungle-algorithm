'''
문제 설명
두 정수 A와 B를 입력받아 A + B를 출력하세요.
이 계산을 여러 번 반복합니다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어집니다.
그다음 T개의 줄에 두 정수 A와 B가 공백으로 구분되어 주어집니다.
예시:
5
1 1
2 3
3 4
9 8
5 2

출력
각 테스트 케이스마다 A + B의 결과를 한 줄에 하나씩 출력합니다.
예시:
2
5
7
17
7
'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)