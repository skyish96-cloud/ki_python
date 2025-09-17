# function(함수)
# - 함수는 특정한 기능을 가진 코드의 집합을 의미
# - 함수 이름으로 호출하여 기능을 사용할 수 있다.
#   - 함수이름뒤에 () 이 사용되면 함수
#   - 없으면 변수
# - 함수 생성시 def 함수이름: 으로 함수를 지정할 수 있다.
# - 매개변수와 반환값의 유무에 따라 함수를 구분할 수 있다.

# 함수의 종류
# 1. 매개변수와 반환값이 없는 함수
# 2. 매개변수는 있고 반환값이 없는 함수
# 3. 매개변수는 없고 반환값이 있는 함수
# 4. 매개변수와 반환값이 있는 함수

# 함수를 사용하는 이유
# - 재사용성이 좋다.
# - 유지 보수 및 관리가 편하다.

# 일반적으로 사용하는 방법
# num1 = int(input('첫번째 정수 입력 : '))
# num2 = int(input('두번째 정수 입력 : '))
# num3 = int(input('세번째 정수 입력 : '))

# sum = num1 + num2 + num3
# print(f'총합 : {sum}')

# 함수 생성 방법
# def 함수이름 :
# def add():
#     num1 = int(input('첫번째 정수 입력 : '))
#     num2 = int(input('두번째 정수 입력 : '))
#     num3 = int(input('세번째 정수 입력 : '))

#     sum = num1 + num2 + num3
#     print(f'총합 : {sum}')

# add()
# 함수이름 호출
# 주의점 : 함수는 맨 위에 작성하는 걸 원칙으로 한다.
# - 함수가 정의된 후에 사용이 가능하기 때문이다.

# 함수 안에 사용되는 변수는 함수가 종료되면 사라진다 ex)num
# def int_input(sub): # sub = 매개변수
#     num =int(input(f'{sub} 정수 입력 : '))
#     return num # return = 반환값
# def add():
#     num1 = int_input('첫번째') #'첫번째' = 매개값
#     num2 = int_input('두번째')
#     num3 = int_input('세번째')
#     sum = num1 + num2 + num3
#     print(f'총합 : {sum}')

# add()


# def int_input(sub): # sub = 매개변수
#     num =int(input(f'{sub} 정수 입력 : '))
#     return num # return = 반환값
# def add():
#     sum = int_input('첫번째') #'첫번째' = 매개값
#     sum = int_input('두번째')
#     sum = int_input('세번째')
#     print(f'총합 : {sum}')

# add()


# def int_input(sub): # sub = 매개변수
#     num =int(input(f'{sub} 정수 입력 : '))
#     return num # return = 반환값
# def add():
#     sum = 0
#     sub_ls = ['첫번째', '두번째', '세번째']
#     for i in sub_ls:
#         sum += int_input(i)
#     print(f'총합 : {sum}')

# add()

# def int_input(sub): # sub = 매개변수
#     return int(input(f'{sub} 정수 입력 : '))

# def add():
#     sum = 0
#     sub_ls = ['첫번째', '두번째', '세번째']
#     for i in sub_ls:
#         sum += int_input(i)
#     print(f'총합 : {sum}')

# add()


# def int_input(sub): # sub = 매개변수
#     return int(input(f'{sub} 정수 입력 : '))

# def add():
#     sum = 0
#     #sub_ls = ['첫번째', '두번째', '세번째']
#     for i in range(3):
#         sum += int_input(f'{(i+1)}번째')
#     print(f'총합 : {sum}')

# add()

# 매개변수 없고 반환값 없는 함수
def menu():
    print('1. 더하기')
    print('2. 빼기')


# 매개변수 없고 반환값 있는 함수
def menu_num():
    return input('메뉴 선택 :')


def num_input():
    return int(input('정수 입력:'))


# 매개변수 있고 반환값 있는 함수
def operation(oper, num1, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    else:
        return None


# 매개변수 있고 반환값 없는 함수
def output(result):
    print(f'결과값 : {result}')


menu()
menu_num = menu_num()
num1 = num_input()
num2 = num_input()
if menu_num == '1':
    oper = '+'
else:
    oper = '-'
print(menu_num)
result = operation(oper, num1, num2)
print(result)
output(result)