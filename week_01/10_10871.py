'''
문제 설명
정수 N개로 이루어진 수열과 기준값 X가 주어집니다.
수열에서 X보다 작은 수만 입력된 순서대로 출력하세요.

입력
첫째 줄에 정수 N과 X가 공백으로 구분되어 주어집니다.
둘째 줄에 수열을 이루는 N개의 정수가 주어집니다.
예시:
10 5
1 10 4 9 2 3 8 5 7 6

출력
수열에서 X보다 작은 수를 입력된 순서대로 출력합니다.
예시:
1 4 2 3
'''

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int,input().split()))

for i in arr:
    if i < x:
        print(i, end = " ")