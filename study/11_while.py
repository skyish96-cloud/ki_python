# while 문
# - 종료 조건에 따라 참이면 실행 거짓이면 종료
# - for문 달리 시작, 종료, 증감이 없다.
# - while 조건에 의해 처리 된다.

# 시작값 - while문 외부에 지정
# 시작값이 지정되지 않으면 예외 발생
i = 0

# 종료 조건식
while i < 5: # 참이면 실행 거짓이면 종료
    print(f"{i} 번째 실행")

    # 증감값 - while문 내부에 지정 (종료를 위해서 작성)
    # 증감값이 없거나 잘못 지정되면 무한반복됨
    # Ctrl + c 를 누르면 종료
    i += 1

print("while문 종료")

i = 1
odd, even = 0, 0

while i <= 10:
    if i % 2 == 0:
        even += i
    else :
        odd += i
    i += 1
print(f"짝수의 합 : {even}, 홀수의 합 : {odd}")

# while문법에서 다른 언어에서는 사용하지 않는 else가 있다.
i = 0

while i < 3:
    print(i)
    i+=1
else:
    print(f"while 문 종료 된 후 {i}")

# break 문 : 이 키워드를 만나면 while, for문은 종료 된다.
i = 0
while True: # 무한반복
    print("a")
    if i == 3:
        break
    i += 1

# continue문 : 이 키워드를 만나면 처음으로 돌아간다.
i = 0
while i < 10:
    i += 1
    if i % 5 == 0:
        continue
    print(i)

# break 문은 하나의 while문 또는 for 문만 종료된다.
print()
for i in range(5):
    for j in range(5):
        if i == 2:
            break;
        print(f"{i+j}")