# while문을 활용해 숫자맞히기 게임을 만들겠습니다.

import random   # 무작위 정수값을 사용하기 random 모듈을 import합니다.

target_num = random.randint(1, 100) # randint함수를 이용해 무작위 정수를 생성합니다.

print("무작위 숫자를 맞혀보세요!")
print("범위는 [1,100]입니다.")
print('-1로 기권할 수 있습니다.')

while True:
    guess = int(input())
    if guess == -1:
        print("기권하셨습니다.")
        break
    elif guess == target_num:
        print("정답입니다!")
        break
    elif guess < target_num:
        print("정답보다 작습니다.")
    else:   # guess > target_num
        print("정답보다 큽니다.")