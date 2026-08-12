'''
문제 설명
정수 N개로 이루어진 배열 A가 주어집니다.
배열의 순서를 적절히 바꿔서 다음 식의 값을 최대한 크게 만들어야 합니다.
|A[0] - A[1]|
+ |A[1] - A[2]|
+ ...
+ |A[N-2] - A[N-1]|
즉, 배열을 어떤 순서로 배치하느냐에 따라 인접한 숫자들의 차이의 합이 달라지고, 그중 최댓값을 구하는 문제입니다.

입력
첫째 줄에 N이 주어집니다.
둘째 줄에 N개의 정수가 공백으로 구분되어 주어집니다.

예시:
6
20 1 15 8 4 10
제한
N ≤ 8
각 원소의 절댓값 ≤ 100

출력
주어진 식의 최댓값을 출력합니다.
예시:
62
'''

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
answer = 0

for per in permutations(a):
    result = 0
    
    for i in range(n - 1):
        result += abs(per[i] - per[i + 1])

    answer = max(answer, result)

print(answer)