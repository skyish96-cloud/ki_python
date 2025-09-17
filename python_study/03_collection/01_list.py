# list
# - 데이터의 목록을 다루는 자료형
# - [](대활고)를 이용해서 자료형을 구분
# - list에는 데이터의 형식과 상관없이 모두 포함 할 수 있다
# - index 번호(첨자)를 이용하여 데이터를 호출할 수 있다.

# [] 로 list 변수를 구분한다.

ls = [] # list 인 변수로 사용 가능
# 자료형과 상관없이 데이터를 저장할 수 있다.
ls = [1, 'hello', 1.234, [1,2,3]]

print(ls)
print(type(ls))

# indexing
print(ls[0])
print(ls[1])
print(ls[2])
print(ls[3])

# list 의 값을 변경할 때도 index 번호를 이용해서 변경할 수 있다.
ls = [0,0,0,0]

ls[0] =int(input("첫번째 정수 입력 :"))
ls[1] = int(input("두번째 정수 입력 :"))
ls[2] = int(input("세번째 정수 입력 :"))

print(ls)

sum = ls[0] + ls[1] + ls[2]
print(sum)

################ list의  for 문 사용
ls = [0,0,0,]
sum = 0
for i in range(len(ls)):
    ls[i] = int (input(f"{i + 1}번째 정수 입력 : "))
    sum += ls[i]

print(sum)

ls = [100, 200, 300]
sum=0
for i in ls:
    sum+= i
print(sum)