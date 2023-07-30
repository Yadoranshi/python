# 지금까지 배운 내용으로 간단한 출석부 프로그램을 만들어보겠습니다.

students = [['유규민', '17번', '남자'], ['박준혁', '13번', '남자'], ['윤해온', '20번', '남자']]

print(f'학생 1 이름 : {students[0][0]}')
print(f'학생 1 번호 : {students[0][1]}')
print(f'학생 1 성별 : {students[0][2]}')
print()

print(f'학생 2 이름 : {students[0][0]}')
print(f'학생 2 번호 : {students[0][1]}')
print(f'학생 2 성별 : {students[0][2]}')
print()

print(f'학생 3 이름 : {students[0][0]}')
print(f'학생 3 번호 : {students[0][1]}')
print(f'학생 3 성별 : {students[0][2]}')
print()
# 딕셔너리를 이용한 코드는 이렇습니다.

students = []
students.append({'이름':'유규민', '번호':17, '성별':'남자', '성적':{'수학':100, '한국사':50}})
students.append({'이름':'박준혁', '번호':13, '성별':'남자', '성적':{'수학':90, '한국사':30}})
students.append({'이름':'윤해온', '번호':20, '성별':'남자', '성적':{'수학':50, '한국사':50.1}})

print(f'학생 1 이름 : {students[0]["이름"]}')
print(f'학생 1 번호 : {students[0]["번호"]}')
print(f'학생 1 성별 : {students[0]["성별"]}')
print(f'학생 1 수학 성적 : {students[0]["성적"]["수학"]}')
print(f'학생 1 한국사 성적 : {students[0]["성적"]["한국사"]}')
print()

print(f'학생 2 이름 : {students[1]["이름"]}')
print(f'학생 2 번호 : {students[1]["번호"]}')
print(f'학생 2 성별 : {students[1]["성별"]}')
print(f'학생 2 수학 성적 : {students[1]["성적"]["수학"]}')
print(f'학생 2 한국사 성적 : {students[1]["성적"]["한국사"]}')
print()

print(f'학생 3 이름 : {students[2]["이름"]}')
print(f'학생 3 번호 : {students[2]["번호"]}')
print(f'학생 3 성별 : {students[2]["성별"]}')
print(f'학생 3 수학 성적 : {students[2]["성적"]["수학"]}')
print(f'학생 3 한국사 성적 : {students[2]["성적"]["한국사"]}')
