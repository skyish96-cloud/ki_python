# for : 조건에 의해서 정해진 횟수를 반복하는 반복문
# - 반복횟수가 정해져 있는 유한 반복

# range() : 범위를 지정하는 함수
# range(시작값, 끝값, 증감값)
# 시작값 ~ 끝값-1 까지 진행

# for 다음 변수 i 는 range() 에서 값을 하나씩 처리하는 변수
for i in range(1, 10, 1):
    print(i)

# 증감값은 기본값이 1 이다.
for i in range(1, 10):
    print(i)

# 시작값은 기본값이 0 이다.
for i in range(5): # 0 ~ 4 까지 출력
    print(i)

# range(시작값 = 0, 끝값, 증감값 = 1)
# for i in range(5, 2): range(시작값, 끝값) 으로 이해
# 0 으로 시작한다고 해서 첫 번째 옵션 값을
#   끝값으로 지정할 수 없다.
# 끝값과 증감값만 변경한다 하더라도
#   첫번째 옵션 값은 시작값으로 지정해야 한다.
for i in range(0, 5, 2):
    print(i)

# 증감값을 - 로 할 경우 시작값은 큰값으로 시작해야 한다.
for i in range(5, 0, -1):
    print(i)

# for 문에서 사용하고자 하는 변수는 반드시 for문 밖에서
#   초기화 해야 한다.
sum = 0
for i in range(5):
    sum += i
print(sum)

# in 연산자 : list 나 문자열의 값이 있는지 비교하는 연산자
# - range() 함수는 범위를 생성
# - in 은 값이 있는 상태에서 비교하는 것
ls = [1,2,3,4,5]

if 1 in ls:
    print("1이 포함되어 있음")

# list 는 인덱스 번호라는 것이 있는데 0 부터 시작한다.
for i in ls:
    print(i)
for i in range(len(ls)):
    print(ls[i])

str = "abcde"

if "ab" in str:
    print("ab 가 포함 되어 있음")
if "ce" in str:
    print("ce 가 포함 되어 있음")

# print("내용", end="")
# end는 출력 후 실행할 내용을 추가 하는 옵션
print("abcd", end="eeeee")
print("abcd", end="\t")
print("ddd")

sum = 0
start = int(input("시작값 입력 : "))
end = int(input("끝값 입력 : "))
grow = int(input("증감값 입력 : "))

for i in range(start, end+1, grow):
    sum += i
print(f"{start} 부터 {end} 까지의 합 : {sum}")