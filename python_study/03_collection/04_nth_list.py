# 이차원 list
# - list 안에 list 가 값으로 되어 있는 list 를 의미

ls = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(ls)
print(type(ls))
print(len(ls)) # 행의 크기를 출력
print(len(ls[0])) # 열의 크기를 출력
print(ls[0])
print(ls[0][0])
print(ls[0][1])
print(ls[0][2])

# 이차원 for문 출력 - indexing
for i in range(len(ls)):
    for j in range(len(ls[i])):
        print(ls[i][j])

# 슬라이싱
print(ls[0:2])

ls1 = ['a','b','c']
print(len(ls1))
print(len(ls1[0]))

student = []
# 입력
stu1 = ['홍길동', '종로구']
student.append(stu1)
stu2 = ['이순신', '강남구']
student.append(stu2)
print(student)

# 수정
for i in range(len(student)):
    if student[i][0] == '이순신':
        student[i] = ['김유신', '동작구']

print(student)

# 삭제
for i in range(len(student)):
    if student[i][0] == '김유신':
        del(student[i])
print(student)

# 전체 삭제
student.clear()
print(student)