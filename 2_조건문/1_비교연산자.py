# 비교연산자에 대해 배우겠습니다.

# 비교연산자는 값을 비교하여 참/거짓을 반환합니다.
# 직접 값을 입력하여 알아봅시다.
a,b= input('a b를 입력하세요\n').split()
a = int(a)
a = int(b)

print(f"{a} < {b}: {a < b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} <= {b}: {a <= b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
