# if ~ elif ~ else 문
# if 문의 조건이 참일 때는 종속코드 실행하고
# 거짓일 때는 elif 조건을 참일 때 종속코드 실행하고
# elif 조건도 거짓이면 else 의 종속 코드 실행한다.
# - elif 는 원하는 만큼 만들 수 있음
# - elif 안에 if문도 추가할 수 있음
# - else 문은 생략이 가능

# 1. 아이디, 비밀번호를 저장
save_id = 'hong'
save_pw = '1234'

# 2. 아이디, 비밀번호를 입력 받기
input_id = input("아이디 입력 : ")
input_pw = input("비밀번호 입력 : ")

# 조건 1. 아이디와 비밀번호가 같을 때
if save_id == input_id and save_pw == input_pw:
    print("로그인에 성공했습니다.")
# 조건 2. 아이디는 같지만 비밀번호가 틀릴 때
elif save_id == input_id and save_pw != input_pw:
    print("비밀번호가 틀립니다.")
# 조건 3. 아이디가 틀릴때
elif save_id != input_id :
    print("아이디가 존재하지 않습니다.")