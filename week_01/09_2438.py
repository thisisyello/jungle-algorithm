'''
문제 설명
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, 이런 식으로 N번째 줄에는 별 N개를 출력하세요.

입력
첫째 줄에 정수 N이 주어집니다.
예시:
5

출력
첫째 줄부터 N번째 줄까지 별을 하나씩 늘려가며 출력합니다.
예시:
*
**
***
****
*****
'''

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    print(f"{'*' * (i + 1)}")