# input() : 사용자에게 값을 입력받기 위한 함수
# print(end="") : end 옵션은 출력 후 마무리를 지정하는 옵션
# - 기본값은 "\n"
print("숫자 입력 : ", end="")
# input() 에서 입력 받은 값은 저장을 위해서 변수를 사용함
num = input()
print(f"입력 받은 값 : {num}")

# input("출력할 내용")
# 출력할 내용을 출력하고 입력받을 수 있다.
name = input("이름 입력 : ")
age = input("나이 입력 : ")
print(f"{name} 님의 나이는 {age} 살 입니다.")

# input() 로 받은 모든 데이터의 자료형은 문자열이다.
num1 = input("정수 입력 : ")
print(type(num1))

num1 = input("첫번째 정수 입력 : ")
num2 = input("두번째 정수 입력 : ")
print(f"{num1} + {num2} = {int(num1) + int(num2)}")

# Cast 연산자
# - 값의 데이터 자료형을 원하는 자료형으로 변경한다.
num = 10
print(type(float(num)))
print(type(str(num)))
num = 1.23
print(type(int(num)))
print(type(str(num)))
num = "123"
print(type(int(num)))
print(type(float(num)))

# 형변환에서 주의할 점은 숫자로 된 문자열은 형변환이 가능
# 하지만 문자가 표함된 문자열은 형변환이 불가능하다.
# num = "a"
# print(type(int(num)))
# print(type(float(num)))

num1 = int(input("정수 입력 : "))
print(f"num1 : {num1}, type : {type(num1)}")
flt1 = float(input("실수 입력 : "))
print(f"flt1 : {flt1}, type : {type(flt1)}")

num = "123"
num_int = int(num)
print(type(num))




