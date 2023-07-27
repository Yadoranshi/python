# Dictionary / 사전 타입에 대해 설명합니다.
# 사전 타입은 key : value 형태의 원소를 가지는 타입입니다.
# 아레 예시는 box 안에 어떤 음식이 몇개 있는지 저장합니다.

# 예제 1
box = { 'Apple' : 3, 'Potato' : 4, 'Banana' : 1 }

# 배열과 같이 [] 를 사용하지만, [] 안에 key 값을 넣으면 해당 key에 맞는 value를 반환합니다.
appleCount = box['Apple']   # 3
PotatoCount = box['Potato'] # 4

print(f'사과 개수 : {appleCount}')
print(f'감자 개수 : {PotatoCount}')