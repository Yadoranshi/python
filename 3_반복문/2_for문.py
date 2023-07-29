#for문에 대해 배웁니다.

print("0~9 출력")
for i in range(10):
    print(i, end= " ") # end=" "를 통해 마지막에 개행문자가 아닌 공백을 출력
print('\n\n')

l = [10, 2, -1, 601, 0]

#list를 출력하기
print("list 출력")
for i in l: 
    print(i, end = " ")
print('\n\n')

#index와 함께 출력하기
print("index와 함께 list 출력")
for idx, value in enumerate(l): 
    print(idx, value)
print('\n\n')

#문자열도 활용할 수 있습니다.
print('문자열 활용')
for i in "hello": 
    print(i)
print('\n\n')

# 특정 문자가 처음 나오는 인덱스 출력하기
print('\'l\'이 처음 나오는 인덱스') # 따옴표를 다룰 떄는 (\')를 활용한다
for idx, value in enumerate("hello"): # 'l'이 처음 등장하는 index 출력하기
    if value == 'l':
        print(idx)
        break   # break를 이용해 for문을 탈출
print('\n\n')

# 홀수만 출력하기
print('홀수만 출력하기')
for i in range(20):    
    if i%2 == 0:
        continue    # continue를 이용해 다음 반복으로 건너뛰기
    print(i, end = ' ')