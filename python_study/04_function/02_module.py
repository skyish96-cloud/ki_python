# Module (모듈)
# - 내장함수가 아닌 기능들을 python 에서 사용할 수 있도록 만든 파일
# - 파일안에는 함수, 변수 도는 클래스도 포함되어 있다.
# - 이 파일들은 호출 하여 사용할 수 있다.
# - 기본 키워드는 import 다.
# - 사용자가 직접 정의한 파일도 호출 할 수 있다.

# import 는 파일에 있는 모든 기능을 호출해서 사용한다는 의미
import calc

# 사용할 때는 파일이름.변수 로 호출
# calc.py 파일에 잇는 변수를 호출
print(calc.PI)

# 사용할 때는 파일이름.함수() 로 호출
# calc.py 파일에 있는 함수 호출
calc.add(10,5)
calc.minus(10,5)

# 별칭을 사용하는 경우도 있다.
# import 파일이름 as 별칭
import calc as c

print(c.PI)
c.add(10,5)
c.minus(10,5)

# 단일 기능 또는 변수만 호출
# from 파일명 import 변수 또는 함수명
from calc import add
from calc import minus
from calc import PI
print(PI)
add(10,5)
minus(10,5)

# 단일 기능 또는 변수는 별칭을 사용할 수 있다.
# from 파일명 import 변수 또는 함수명 as 별칭
from calc import add as a
from calc import minus as m
from calc import PI as P

print(P)
a(10,5)
m(10,5)
