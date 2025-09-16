# 파이썬에서는 def를쓰면 된다.
# def은 선언이다.
#JAVA와 다르다.

# 함수 선언(define)
def toaster(bread):
    print(f'{bread}이 구워지고 있다.')
    return f'구워진 {bread}'
    pass

# 함수 사용
dish = toaster('식빵')
print(dish)
#dish의 역활은 상태를 확인하기 위해서이다.




