# range에 대해 배워봅시다.
# range를 이용해서 정수 범위를 표현할 수 있습니다.

print(range(100))  # range는 실제로 100개의 정수를 할당하지 않는다.
print(list(range(100)))  # [0, 100) 범위의 정수
print()
nums = range(100)

print(f"10 in nums?: {10 in nums}")
print(f"100 in nums?: {100 in nums}")

print(f"range(10, 30): {list(range(10, 30))}") # [10, 30) 범위의 정수
print(f"range(1, 100, 2): {list(range(1, 100, 5))}")    # 5가 공차

print(f"range(10, 0): {list(range(100, 0))}") # 의도한대로 작동하지 않는다.
print(f"range(10, 0, -1): {list(range(10, 0, -1))}") # 의도한대로 작동한다.

