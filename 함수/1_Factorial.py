#팩토리얼 연산을 함수로 만들어보겠습니다.

def factorial(n):   #n을 매개변수로 가지는 함수 factorial입니다.
    ret = 1
    for i in range(1, n+1):
        ret *= i
        
    return ret  #최종적으로 ret에 저장된 값을 return하며 함수는 종료됩니다.

n = int(input())
print(factorial(n)) #factorial이 return하는 값을 출력하겠군요.