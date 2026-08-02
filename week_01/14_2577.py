'''
문제 설명
세 개의 자연수 A, B, C를 곱한 결과에 0부터 9까지의 숫자가 각각 몇 번 사용되었는지 구하세요.
예를 들어 세 수를 곱한 결과가 다음과 같다면:
17037300
각 숫자가 등장한 횟수를 세어야 합니다.

입력
첫째 줄에 자연수 A가 주어집니다.
둘째 줄에 자연수 B가 주어집니다.
셋째 줄에 자연수 C가 주어집니다.
예시:
150
266
427

출력
첫째 줄에는 숫자 0이 사용된 횟수, 둘째 줄에는 숫자 1이 사용된 횟수를 출력합니다.
이와 같은 방식으로 숫자 9까지의 사용 횟수를 총 10줄에 걸쳐 출력합니다.
예시:
3
1
0
2
0
0
0
2
0
0
'''

import sys
input = sys.stdin.readline

result = 1
counts = [0] * 10

for _ in range(3):
    num = int(input())
    result *= num

for char in str(result):
    counts[int(char)] += 1

for i in range(10):
    print(counts[i])
