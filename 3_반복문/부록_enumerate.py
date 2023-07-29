# enumerate를 배웁니다.

# enumerate를 이용해서 리스트의 원소를 인덱스와 함께 튜플로 묶을 수 있습니다.
l = list(range(30))
print(l, '\n')

enu = enumerate(l)
print(list(enu), '\n')

# 인덱스를 몇부터 시작할지 정할 수 있습니다.
enu = enumerate(l, start=1)
print(list(enu), '\n')

# 문자열도 가능합니다.

print(list(enumerate("hello")))

