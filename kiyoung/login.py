id = 'hong'
password = '1234'
id_chk=input('아이디 입력 :').strip()
if id_chk == id:
    pwd_chk=input('비밀번호 입력 :')
    if pwd_chk == password:
        print(f'{id_chk} 님 로그인에 성공했습니다.')
    else:
        print(' 비밀번호가 맞지 않습니다.')
else:
    print(' 등록되지 않은 아이디 입니다.')




