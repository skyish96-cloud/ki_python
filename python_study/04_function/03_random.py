# random : 0~1 사이의 난수를 생성하는 모듈
import random

# random.random() : 0~1 사이의 난수 생성
print(random.random())


# random.randint(a,b) : a이상 b이하의 정수 중 난수 생성
print(random.randint(1,10))

# random.randrange(start, end-1, step)
print(random.randrange(1,11,3))

# random.choice(data) : data 중 하나를 랜덤으로 선택
print(random.choice([1,2,3]))

# random.sample(data, k) : data 에서 k 개를 랜덤으로 선택
print(random.sample([1,2,3,4,5],2))

# random.seed(data) : 시드를 data로 고정
# - 데이터 분석에서 고정된 난수를 얻고 싶을 때 사용

random.seed(2)
print(random.randint(1,10))