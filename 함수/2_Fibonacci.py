# 재귀함수를 이용해 n 번째 피보나치 수를 찾아보겠습니다.

def fibonacci(n):
    if(n == 0):
        return 0
    elif n == 1 or n==2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))