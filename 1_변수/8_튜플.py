# 튜플에 대해 배웁니다.
# 튜플은 리스트와 비슷하게 여러 값을 다룹니다.
# 그러나 튜플은 원소를 생성, 삭제, 수정할 수 없다는 점에서 리스트와 다릅니다.

# 튜플을 선언할 때는 소괄호를 사용합니다. 
nums = (10, 20, 30)
print(nums)

# 리스트와 마찬가지로 인덱스로 원소에 접근할 수 있습니다.
print(nums[0])
print(nums[1])
print(nums[2])

# 튜플의 덧셈입니다.
nums = nums + (40, 50)
print(nums)

# 튜플의 원소는 모든 타입이 가능합니다.
tup = ((10, 20), [30, 20], '나는 망고', False)