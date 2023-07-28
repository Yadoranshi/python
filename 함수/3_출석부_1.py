def add_student(attendance, student):
    if student in attendance:
        
    attendance.append(student)
    return

def remove_student(attendance, student):
    attendance.remove(student)
    return


attendance = []

add_student(attendance, ['유규민','17번','남자'])
add_student(attendance, ['유규민','17번','남자'])
remove_student(attendance, ['유규민', '17번', '남자'])
print(attendance)
