# # 함수 선언(define)
# def toaster(bread):
#     print(f'{bread}이 구워지고 있다.')
#     return f'구워진 {bread}'
#     pass
#
# # 함수 사용
# dish = toaster('식빵')
# print(dish)
# #dish의 역활은 상태를 확인하기 위해서이다.

# def 함수명 (매개변수):
# 수행할 내용
# return 반환값

# 반환타입:O 매개변수:O (커피머신)(자판기)
def coffee_brewer(coffeebean):
    print(f'{coffeebean} 원두가 추출되고 있다.')
    return f'{coffeebean} 아메리카노가 나왔습니다.'
cup = coffee_brewer('과테말라산')
print(cup)
#def coffee_brewer(coffeebean): (선언: 만들어만 놓았지 누가 사용한건 아님)
# 매개변수는 coffeebean
# print(f'{coffeebean} 원두가 추출되고 있다.') return은 반환타입 (실제로 밖으로 나오는 값)
# return f'{coffeebean} 아메리카노가 나왔습니다.' (실질적인 동작이 아님, 사람 눈에만 보이는 것이다.)

# 사용
# cup = coffee_brewer('과테말라산') (return으로 나온 값을 cup에 담는다.)
# print(cup) (cup 안의 값을 출력
# print coffee_brewer('coffeebean') (커피머신에서 나온 값을 바로 출력)

# 반환타입:O 매개변수:X (수도꼭지)()
def faucet():
    return f'지하수가 나온다'
print(faucet())

def 번호표기계():
    return f'번호표가 나온다.'
print(번호표기계())

# 반환타입:X 매개변수:O (쓰레기통)
def wastebasket(can):
    print(f'쓰레기통에 깡통을 버린다.')
wastebasket('깡통')

def 저금통(coin):
    print(f'{coin}원 저축')

#저금통(500)
#저금통에는 return이 없는데 저금통 실행 후 나온 값을 출력하려고 하니
#None이 출력되는 것
print(저금통(100))

# 반환타입:X 매개변수:X (온도계)(스트레스볼?)
def thermometer():
    print('온도가 측정된다.')
thermometer()

def 호출벨():
    print('호출벨이 울린다.')
호출벨()
