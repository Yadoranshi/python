# if문에 대해 배우겠습니다.

x = int(input())

if x < 10:  # 조건식이 참일 경우에만 아래의 코드를 동작합니다.
    print("x는 10보다 작다.")
elif x == 10:   # 앞서 등장했던 if, elif의 조건식이 참이라면 elif는 조건식의 참/거짓 여부와 상관없이 동작하지 않습니다.
    print("x는 10이다.")
else:   # 앞서 등장했던 if, elif의 조건식이 모두 거짓일 경우 아래의 코드를 동작합니다.
    print("x는 10보다 크다.")


x = int(input())

if x < 10:
    if x > 5:
        print("x는 5보다 크고 10보다 작다.")
elif x > 10:
    if x < 15:
        print("x는 10보다 크고 15보다 작다.")
else:
    print ("x는 10이다.")
