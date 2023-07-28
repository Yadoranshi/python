#팩토리얼 연산을 함수로 만들어보겠습니다.

def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

n = int(input())
print(factorial(n))