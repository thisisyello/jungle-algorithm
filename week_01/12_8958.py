'''
문제 설명
OX 퀴즈의 결과가 문자열로 주어집니다.
O는 정답입니다.
X는 오답입니다.
연속해서 맞힌 O는 점수가 1점씩 증가합니다.
X가 나오면 연속 점수는 다시 초기화됩니다.
예를 들어:
OOXXOXXOOO
점수는 다음과 같습니다.
1 + 2 + 0 + 0 + 1 + 0 + 0 + 1 + 2 + 3
따라서 총점은 10점입니다.

입력
첫째 줄에 테스트 케이스의 개수가 주어집니다.
그다음 줄부터 각 테스트 케이스의 OX 퀴즈 결과가 문자열로 주어집니다.
예시:
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX

출력
각 테스트 케이스의 총점을 한 줄에 하나씩 출력합니다.
예시:
10
9
7
55
30
'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    count = 0
    score = 0
    result = input()

    for i in result:
        if i == "O":
            count += 1
        else:
            count = 0
        score += count

    print(score)