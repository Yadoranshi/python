# while문에 대해 배웁니다.

i = 0
print("0부터 9까지 출력")
while i < 10:
    print(i, end = ' ')
    i += 1
print('\n\n')

print("\'l\'이 처음 나오는 인덱스")
string = "hello"
i = 0 # i가 10이었다는 사실을 잊으면 안되겠죠?
while i < len(string):
    if string[i] == 'l':
        print(i)
        break
    i += 1
print()

print("홀수만 출력")
i = 0
while i < 30:
    if i % 2 == 0:
        i += 1
        continue
    i += 1
    print(i)
print('\n\n')