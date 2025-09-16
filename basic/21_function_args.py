# 인자값으로 아무것도 들어오지 않았을 경우 에러를 방지하기 위해 기본값 설정이 가능
def plus(num=0): # 2개의 사용 위치
    result = num + 5
    return result

print(plus(5)) #10
print(plus()) # plus() missing 1 required positional argument: 'num'
# plus(num)을 0으로 설정
# print(plus(5))는 plus(num=0)의 값을 5로 만들고 +5를해서 10의 값을 프린트
# print(plus())는 plus(num=0)에 +5를해서 5의 값을 프린트


# 인자값의 종류를 tuple(수정이 불가능한 List형태)로만 받겠다.
# return은 함수 한 곳에 무조건 하나
def tuple_args(*numbers):
    print(numbers)
    total = 0
    for num in numbers:
        total += num
    return total

# # 이 방식은 사용자가 인자값의 갯수를 자유롭게 정해서 넣을 수 있다.
print(tuple_args(1,2,3,4,5))
# total의 값을 0으로 설정하고 numbers의 값을 (1,2,3,4,5)로 설정한다.
# total 값에 num의 값을 더하고 tuple_args를 넣어 수정이 불가능한 리스트형태로 출력함

# **는 매개변수를 사전형태로 받겠다.
def dic_args(**dic):
    # 1 .dic에서 값만 빼온다.
    values = dic.values() # values 값만 리스트처럼 빼온다.
    print(values)
    # 2.이 값들을 하나씩 더해 누적시킨다.
    total = 0 # 토탈 값 = 0
    for v in values: # values에서 나온 각각의 v의 값을 구한다.
        print(v)
        total += (v) # total = 0에서 v의 값을 더한다.
    #3. 누적시킨 값을 밖으로 return 한다.
    return total # total += (v)이 값으 프린트한다.
    print(dic)
# values = dic.values() 밸류의 값을 리스트처럼 빼온다.
# total의 값을 0으로 설정하고 dic에서 밸류값을 for v in values: 로 설정하고 프린트한다.
# print(v) 밸류의 값을 각각 프린트한다.

# 위 함수를 실행하면 입력된 값들의 합산이 반환되도록 하세요
result = dic_args(kim=50, lee=100, park=70, na=90)
print(result) # (50+100+70+90 = 310)
# 모든 밸류의 값을 다 더한다.



