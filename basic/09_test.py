# import random

# number = random.randint(1,31)
# print(f'내 마음속 숫자:{number}')
# running = True

# 입력받은 값을 정술(int)로 변환하야 guess에 대입
# guess = int(input('1~31 중 내가 생각한 숫자는?'))
# print(f'입력받은 숫자{guess}')

#  while running:
#    pass

#조건은
# 1.입력값이 생각값과 같을때
# 2. 입력값이 생각값보다 작을때
# 3. 입력값이 생각값보다 클때

import random

number = random.randint(1,31)
#number에 random.randint(1,31)이 코드를 넣어서 랜덤하게 뽑아서 number에 대입.
# 1이하 또는 31이상을 쳤을때도 인식이 되는 이유는? 범위 내 숫자만 되게 하는 방법이 궁금
print(f'내 마음속 숫자:{number}')
running = True #running 다음에 false가 아닌 true가 들어가는 이유는?
               # 구조 : while 조건문은 조건문이 참(true)일 때만 반복문 내부의 문장들이 실행됩니다.
               # 거짓(flase)이 들어가면 조건문의 조건인 참(true)의 반복문이 깨져서 정지한다.

# while은 오른쪽에 있는 조건 결과가 true일 경우 반복되는 구문
# running이 초기에 true이므로 무조건 실행되는 구조
while running:
    guess = int(input('1~31 중 내가 생각한 숫자는?')) # 입력받은 값을 정술(int)로 변환하야 guess에 대입
    print(f'입력받은 숫자{guess}')
    # 이곳에 입력값의 최소와 최대를 설정하면 그 범위를 초과할 수 없다.
    if number == guess:
    # 만약 if 내 마음속의 숫자(number)와 내가 입력한 숫자(guess)가 같다.(기준이 되는 곳은 왼쪽에 넣는다.)
        print('정답입니다.')
        running = False # running 변수는 flase 값으로 바뀌게 된다.
    elif number > guess:
    # 만약이 아니라면 elif를 사용하여 이곳에 해당하는지 확인한다.
    # 내 마음속 숫자가 내가 입력한 숫자보다 크다면(기준이 되는 곳은 왼쪽에 넣는다.)
        print('내가 생각한 숫자보다 작습니다.')
    elif number < guess:
    # 만약과 첫번째 elif가 아니라면 이곳에 해당하는지 확인하기 위해서 사용
    #내 마음속 숫자가 내가 입력한 숫자보다 작을때(기준이 되는 곳은 왼쪽에 넣는다.)
        print('내가 생각한 숫자보다 큽니다.')
