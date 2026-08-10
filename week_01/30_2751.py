'''
문제 설명
N개의 수가 주어집니다.
이 수들을 오름차순으로 정렬한 뒤 한 줄에 하나씩 출력하세요.
29번과 거의 같아 보이지만, 이번에는 입력 개수가 훨씬 많아서 입출력 속도를 신경 써야 합니다.

입력
첫째 줄에 수의 개수 N이 주어집니다.
N ≤ 1,000,000
둘째 줄부터 N개의 줄에 정수가 하나씩 주어집니다.
예시:
5
5
4
3
2
1

출력
오름차순으로 정렬한 결과를 한 줄에 하나씩 출력합니다.
예시:
1
2
3
4
5
'''

import sys
input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    num = int(input())
    numbers.append(num)

numbers.sort()

print('\n'.join(map(str, numbers)))
