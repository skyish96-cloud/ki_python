# 변수 이름 작명 규칙
# 알파벳(대소문자), 숫자, 언더바(_) 구성
# 대소문자 구분 가능
# 변수이름 시작은 숫자로 할 수 없다.
# 키워드도 사용 가능하나 가능하면 사용 안하는걸 권장
# 공백이나 언더바(_)를 제외한 기호는 사용할 수 없다.
# =====================================
# 관례
# 한글은 안되나요? 됩니다. 하지만 권장하지 않는다.
# 변수나 함수는 시작 영문자를 대문자로 쓰지 않는다.
# - 클래스만 대문자로 시작하기 때문이다.
# 상수형변수는 모든 변수이름을 대문자로 한다.
var_1 = 100
Var_1 = 200
VAr_1 = 300
PI = 3.14
# 123ABC = 123 # 숫자로 시작할 수 없다.
# python 에서는 _ 를 많이 사용
car_speed = 100
# java 는 단어를 연결할때 대문자로 시작한다.
carSpeed = 100

# 변수 선언
# - 데이터 자료형을 지정하지 않고 선언 할 수 있다.
var = 10;
print("var 의 값 : %d"%(var))
print(type(var))
var = 1.234;
print("var 의 값 : %f"%(var))
print(type(var))
var = 'abcde';
print("var 의 값 : %s"%(var))
print(type(var))
var = True
print("var 의 값 :",var)
print(type(var))

# type() : 데이터 타입을 확인하는 함수
# int : 정수형 데이터 타입
# str : 문자열 데이터 타입
# float : 실수형 데이터 타입
# bool : 논리형 데이터 타입 (True, False)

# id() : 값을 참조하는 메모리의 영역 위치를 확인하는 함수
num1 = 100
print(id(num1))
num2 = 100
print(id(num2))
num2 = 200
print(id(num2))
num2 = 100
print(id(num1))

# round() : 소수점을 지정해서 출력 해 주는 함수
# - 반올림
num = 123.456789
print(round(num, 1))
print(round(num, 3))
print(round(num, 4))
print(round(num, -1))
print(round(num, -2))



