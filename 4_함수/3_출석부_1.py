#함수를 이용해 출석부를 구현해보겠습니다.

def add_student(attendance, student):
    if student in attendance:
        return
    attendance.append(student)

def print_attendance(attendance):
    for i in range(len(attendance)):
        print(f"학생 {i + 1} 이름 : {attendance[i]['이름']}")
        print(f"학생 {i + 1} 번호 : {attendance[i]['번호']}")
        print(f"학생 {i + 1} 성별 : {attendance[i]['성별']}")
        print(f"학생 {i + 1} 수학 성적: {attendance[i]['성적']['수학']}")
        print(f"학생 {i + 1} 한국사 성적: {attendance[i]['성적']['한국사']}")
        print()

def average(attendance, subject):
    num_of_students = len(attendance)
    sum = 0
    for i in range(num_of_students):
        sum += attendance[i]['성적'][subject]
    return sum/num_of_students


attendance = []
#add_student라는 이름을 지어줌으로써 이 코드가 어떤 작업을 하는지 명시했습니다.
add_student(attendance, {'이름':'유규민', '번호':17, '성별':'남자', '성적':{'수학':100, '한국사':50}}) 
add_student(attendance, {'이름':'유규민', '번호':17, '성별':'남자', '성적':{'수학':100, '한국사':50}})
add_student(attendance, {'이름':'유내온', '번호':20, '성별':'남자', '성적':{'수학':50, '한국사':50}})
add_student(attendance, {'이름':'박준혁', '번호':0, '성별':'남자', '성적':{'수학':90, '한국사':50}})

print_attendance(attendance)   #이제 단 한 줄로 출석부의 내용을 출력할 수 있습니다!
print(average(attendance, '수학')) #복잡한 연산도 한결 보기 편해졌군요!