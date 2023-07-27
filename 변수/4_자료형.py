# 모든 변수는 각 값에 해당하는 자료형(type)을 가지고 있습니다.
# python 에는 여러 자료형이 존재합니다.
# int : 정수, float : 실수, str : 문자열, list : 리스트 ..

# int : 정수를 가진 변수는 int 자료형이 됩니다.
a = 3
b = 4
a = b + 4
print(a, type(a))

# float : 3.14 와 같은 실수는 float 이며 실수와 연산한 값 또한 실수가 됩니다.
# 실수 * 정수 : 실수
r = 2
pi = 3.14
# 실수 * 정수 * 정수 = 실수
area = pi * r * r
print(area, type(area))

# str : string 의 약자로 문자열을 나타냅니다.
# 문자열은 ' 나 "로 덮어야 합니다.
s1 = '안녕하세요'
s2 = " 반갑습니다."

# 문자열 + 문자열, 즉 문자열끼리의 덧셈은 두 문자열을 이어줍니다.
print(s1 + s2)

# 문자열 * n 는 해당 문자열을 n 만큼 반복합니다.
print('a' * 10)