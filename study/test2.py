while True:
    try:
        text = input('값을 넣으면 숫자로 변환됩니다.')
        num = int(text)
        print(f'당신이 입력한 값 :{num} 이 숫자로 변환 되었습니다.')
        break
    except ValueError:
        print(f'{text}는 숫자가 아닙니다.')








while True:
    try:
        print('숫자를 입력하세요.')
        num = int(input())
        print(f'입력한 숫자는 :{num} 입니다.')
        break
    except ValueError:
        print('숫자가 아닙니다. 숫자를 다시 입력하세요.')
        break



# 만약 숫자가 아닌 것이 입력되면?
# 오류는 내보내서 숫자를 다시 입력하도록 한다
# 만약에 맞는 숫자를 입력한다면?




MAX_TRY = 3   # 최대 시도 횟수
count = 0     # 시도 횟수 기록

while count < MAX_TRY:
    try:
        print('숫자를 입력하세요.')
        num = int(input())
        print(f'입력한 숫자는 : {num} 입니다.')
        break  # 숫자 입력 성공 → 반복 종료
    except ValueError:
        count += 1
        print(f'숫자가 아닙니다. 다시 입력하세요. (남은 기회: {MAX_TRY - count})')

if count == MAX_TRY:
    print("입력 기회를 모두 사용했습니다. 프로그램을 종료합니다.")