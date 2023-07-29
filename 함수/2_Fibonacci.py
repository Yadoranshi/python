# 재귀함수를 이용해 n 번째 피보나치 수를 찾아보겠습니다.

# n >= 2일 경우 n 번째 피보나치 수는 n-1 번째 피보나치 수와 n-2 번째 피보나치 수의 합이라는 성질을 이용했습니다.
def fibonacci(n):
    if(n == 0):
        return 0
    elif n == 1 or n==2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))

# 재귀함수는 직관적으로 이해하기 힘든 면이 있어 문제를 직접 풀어보며 익히는 것이 좋습니다.
# 이 장에서는 "재귀함수라는 것이 있구나" 정도로 마치겠습니다.
# https://www.acmicpc.net/problem/17478 <- 추천 문제