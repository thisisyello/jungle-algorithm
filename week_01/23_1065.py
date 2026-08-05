'''
문제 설명
어떤 양의 정수 X의 각 자릿수가 등차수열을 이루면, 그 수를 한수라고 합니다.
예를 들어:
123 → 1, 2, 3의 차이가 일정하므로 한수
135 → 1, 3, 5의 차이가 일정하므로 한수
124 → 차이가 일정하지 않으므로 한수가 아님
1부터 N까지의 수 중 한수의 개수를 구하세요.
한 자리 수와 두 자리 수는 비교할 자릿수 차이가 부족하므로 모두 한수로 봅니다.

제한
N <= 1000

입력
첫째 줄에 자연수 N이 주어집니다.
예시:
110

출력
1보다 크거나 같고 N보다 작거나 같은 한수의 개수를 출력합니다.
예시:
99
'''

import sys
input = sys.stdin.readline

n = int(input())

if n < 100:
    print(n)
else:
    count = 99

    for i in range(100, n + 1):
        ones = i % 10
        tens = (i % 100) // 10
        hundreds = i // 100

        if (ones - tens) == (tens - hundreds):
            count += 1

    print(count)