# from 모듈 import 함수
# 사용할 함수를 미리 불러놓고 사용하는 방법
from oper import sum
print(f'sum() 함수실행 : {sum(5,10)}')

# import 모듈
# 일단 모듈로 불러놓고 모듈로부터 원하는 함수를 사용하는 방법

# 1. oper이라는 이름의 모듈을 불러옴
import oper
print(f'minus() 함수실행 : {oper.minus(10,5)}')

# 2. oper에 op라는 별칭을 준다.
import oper as op
print(f'minus() 함수실행 : {op.minus(10,5)}')

# 변수도 불러올 수 있다.
print(f'field1 : {op.field1} / field2 : {op.field2}')
