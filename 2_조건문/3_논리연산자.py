# 논리연산자를 사용해봅시다.

a, b , c= input("a, b, c\n").split()

int(a)
int(b)
int(c)

if a < b and a < c:
    print(f"{a}는 가장 작습니다.")

if a < b or a < c:
    print(f"{a}보다 큰 수가 하나 이상 존재합니다.")

if not a:   # 0을 제외한 모든 수는 true입니다.
    print(f"{a}는 0입니다.")
