# if 문
# - 조건이 참일때는 if문 종속코드를 실행하고
# - 그렇지 않으면 그냥 넘어 간다.
num1 = 10
num2 = 15

if num1 > num2 : # 이 조건이 참일때
    print("num1 이 크다.")

if num2 > num1 : # 위 조건이 거짓일 때 실행할 if문
    print("num2 가 크다.")

print("if문 종료")

num = int(input("정수 입력 : "))

if num%2 == 0:
    print(f"입력한 {num}은 짝수 입니다.")
if num%2 == 1:
    print(f"입력한 {num}은 홀수 입니다.")